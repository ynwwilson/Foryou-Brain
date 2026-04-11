"""
consolidar_obsidian.py
Organização automática do vault Obsidian — Jarvis / ForYou Code

Regras:
- Nunca deleta nada
- Faz backup antes de mover
- Classifica arquivos da Inbox por tags, nome e conteúdo
- Usa Haiku para classificação incerta (barato)
- Seguro para rodar via cron todo dia

Uso:
    python consolidar_obsidian.py                  # modo normal
    python consolidar_obsidian.py --dry-run        # simula sem mover nada
    python consolidar_obsidian.py --no-ai          # só regras, sem API
"""

import os
import re
import json
import shutil
import logging
import argparse
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO — ajuste se necessário
# ---------------------------------------------------------------------------

# Caminho absoluto do vault. Mude se o vault mudar de lugar.
VAULT_PATH = Path(r"C:\Users\ynwwi\Projects\jarvis\stark\Stark")

# Pasta de entrada — agentes e humano depositam aqui
INBOX = VAULT_PATH / "Inbox"

# Destinos possíveis
DESTINOS = {
    "Projetos":              VAULT_PATH / "Projetos",
    "Knowledge":             VAULT_PATH / "Knowledge",
    "Referências":           VAULT_PATH / "Referências",
    "Sessões":               VAULT_PATH / "Sessões",
    "Agentes/memória":       VAULT_PATH / "Agentes" / "memória",
    "Atlas":                 VAULT_PATH / "Atlas",
    "Arquivo":               VAULT_PATH / "Arquivo",
}

# Backup diário — nunca apagar esta pasta
BACKUP_BASE = VAULT_PATH / "Memória_Longo_Prazo"

# Modelo barato para classificação via API (só quando --no-ai não está ativo)
MODELO_CLASSIFICACAO = "claude-haiku-4-5-20251001"

# ---------------------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------------------

LOG_FILE = VAULT_PATH / "consolidar_obsidian.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# REGRAS DE CLASSIFICAÇÃO — sem IA (rápido e gratuito)
# ---------------------------------------------------------------------------

# Palavras-chave no nome do arquivo → destino
REGRAS_NOME = [
    (r"\b(sessao|sessão|session|diario|diário|daily)\b", "Sessões"),
    (r"\b(projeto|project)\b",                           "Projetos"),
    (r"\b(decisao|decisão|decision)\b",                  "Agentes/memória"),
    (r"\b(conhecimento|knowledge|processo|precific)\b",  "Knowledge"),
    (r"\b(referencia|referência|manual|padrao|padrão|doc)\b", "Referências"),
    (r"\b(atlas|mapa|funil|canvas)\b",                   "Atlas"),
    (r"\b(agente|agent|memoria|memória|context|feedback)\b", "Agentes/memória"),
]

# Tags YAML no frontmatter → destino
REGRAS_TAG = {
    "tipo/sessao":      "Sessões",
    "tipo/projeto":     "Projetos",
    "tipo/conhecimento":"Knowledge",
    "tipo/referencia":  "Referências",
    "tipo/decisao":     "Agentes/memória",
    "tipo/tarefa":      "Projetos",
}


def classificar_por_regras(caminho: Path) -> str | None:
    """
    Tenta classificar o arquivo usando regras determinísticas.
    Retorna o nome do destino ou None se não conseguiu classificar.
    """
    nome = caminho.stem.lower()

    # 1. Tenta pelo nome do arquivo
    for padrao, destino in REGRAS_NOME:
        if re.search(padrao, nome, re.IGNORECASE):
            return destino

    # 2. Tenta pelas tags YAML no frontmatter
    try:
        conteudo = caminho.read_text(encoding="utf-8", errors="ignore")
        tags = extrair_tags(conteudo)
        for tag in tags:
            if tag in REGRAS_TAG:
                return REGRAS_TAG[tag]
    except Exception:
        pass

    return None  # não conseguiu classificar


def extrair_tags(conteudo: str) -> list[str]:
    """Extrai tags do frontmatter YAML."""
    match = re.match(r"^---\s*\n(.*?)\n---", conteudo, re.DOTALL)
    if not match:
        return []

    frontmatter = match.group(1)
    # Formato: tags: [tag1, tag2] ou tags:\n  - tag1
    lista = re.findall(r"tags:\s*\[([^\]]+)\]", frontmatter)
    if lista:
        return [t.strip().strip('"').strip("'") for t in lista[0].split(",")]

    itens = re.findall(r"^\s*-\s*(.+)$", frontmatter, re.MULTILINE)
    return [i.strip() for i in itens if i.strip()]


# ---------------------------------------------------------------------------
# CLASSIFICAÇÃO VIA IA (Haiku — só quando necessário)
# ---------------------------------------------------------------------------

def classificar_com_ia(caminho: Path) -> str:
    """
    Usa Claude Haiku para classificar arquivo que as regras não conseguiram.
    Retorna nome do destino.
    """
    try:
        import anthropic
    except ImportError:
        log.warning("anthropic não instalado. Usando 'Arquivo' como fallback.")
        return "Arquivo"

    try:
        conteudo = caminho.read_text(encoding="utf-8", errors="ignore")
        # Envia só os primeiros 500 chars para economizar tokens
        preview = conteudo[:500].strip()

        client = anthropic.Anthropic()
        destinos_validos = list(DESTINOS.keys())

        resposta = client.messages.create(
            model=MODELO_CLASSIFICACAO,
            max_tokens=50,
            system=f"""Você classifica arquivos Markdown de um vault Obsidian.
Responda APENAS com um dos destinos válidos (sem explicação, sem pontuação):
{chr(10).join(destinos_validos)}""",
            messages=[{
                "role": "user",
                "content": f"Nome do arquivo: {caminho.name}\n\nConteúdo (início):\n{preview}"
            }]
        )

        destino = resposta.content[0].text.strip()

        if destino in DESTINOS:
            log.info(f"  [IA] Classificou como: {destino}")
            return destino
        else:
            log.warning(f"  [IA] Resposta inválida '{destino}'. Usando 'Arquivo'.")
            return "Arquivo"

    except Exception as e:
        log.error(f"  [IA] Erro: {e}. Usando 'Arquivo' como fallback.")
        return "Arquivo"


# ---------------------------------------------------------------------------
# BACKUP
# ---------------------------------------------------------------------------

def fazer_backup(dry_run: bool = False) -> Path:
    """
    Copia o estado atual da Inbox para Memória_Longo_Prazo/YYYY-MM-DD/
    Retorna o caminho do backup criado.
    """
    hoje = datetime.now().strftime("%Y-%m-%d")
    backup_dir = BACKUP_BASE / hoje

    arquivos = list(INBOX.glob("*.md"))
    if not arquivos:
        log.info("Inbox vazia — backup ignorado.")
        return backup_dir

    log.info(f"Backup de {len(arquivos)} arquivo(s) → {backup_dir}")

    if not dry_run:
        backup_dir.mkdir(parents=True, exist_ok=True)
        for arq in arquivos:
            destino_backup = backup_dir / arq.name
            # Se já existe no backup, adiciona timestamp
            if destino_backup.exists():
                ts = datetime.now().strftime("%H%M%S")
                destino_backup = backup_dir / f"{arq.stem}_{ts}{arq.suffix}"
            shutil.copy2(arq, destino_backup)
            log.info(f"  Backup: {arq.name}")

    return backup_dir


# ---------------------------------------------------------------------------
# MOVE ARQUIVOS
# ---------------------------------------------------------------------------

def mover_arquivo(arq: Path, destino_nome: str, dry_run: bool = False) -> bool:
    """
    Move arquivo da Inbox para a pasta destino.
    Se já existir arquivo com mesmo nome, adiciona timestamp.
    """
    pasta_destino = DESTINOS[destino_nome]

    if not dry_run:
        pasta_destino.mkdir(parents=True, exist_ok=True)

    destino_final = pasta_destino / arq.name

    # Evita sobrescrever arquivo existente
    if destino_final.exists():
        ts = datetime.now().strftime("%H%M%S")
        destino_final = pasta_destino / f"{arq.stem}_{ts}{arq.suffix}"

    if dry_run:
        log.info(f"  [DRY RUN] Moveria: {arq.name} → {destino_nome}/")
    else:
        shutil.move(str(arq), str(destino_final))
        log.info(f"  Movido: {arq.name} → {destino_nome}/")

    return True


# ---------------------------------------------------------------------------
# RELATÓRIO
# ---------------------------------------------------------------------------

def salvar_relatorio(resultados: list[dict], dry_run: bool = False):
    """Salva relatório da consolidação na Inbox (para revisão humana)."""
    if dry_run:
        return

    hoje = datetime.now().strftime("%Y-%m-%d")
    rel_path = INBOX / f"{hoje}_relatorio-consolidacao.md"

    total = len(resultados)
    por_destino: dict[str, int] = {}
    sem_classificar = 0

    for r in resultados:
        dest = r.get("destino", "?")
        por_destino[dest] = por_destino.get(dest, 0) + 1
        if dest == "Arquivo" and r.get("metodo") == "fallback":
            sem_classificar += 1

    linhas = [
        f"---",
        f"tags: [tipo/sessao, consolidacao]",
        f"data: {hoje}",
        f"---",
        f"",
        f"# Relatório de Consolidação — {hoje}",
        f"",
        f"**Total processado:** {total}",
        f"**Sem classificação clara (foram para Arquivo):** {sem_classificar}",
        f"",
        f"## Por destino",
        f"",
    ]
    for dest, qtd in sorted(por_destino.items()):
        linhas.append(f"- **{dest}:** {qtd} arquivo(s)")

    linhas += ["", "## Detalhes", ""]
    for r in resultados:
        status = "✅" if r["sucesso"] else "❌"
        linhas.append(f"{status} `{r['arquivo']}` → **{r['destino']}** ({r['metodo']})")

    rel_path.write_text("\n".join(linhas), encoding="utf-8")
    log.info(f"Relatório salvo: {rel_path.name}")


# ---------------------------------------------------------------------------
# LOOP PRINCIPAL
# ---------------------------------------------------------------------------

def consolidar(dry_run: bool = False, usar_ia: bool = True):
    log.info("=" * 60)
    log.info(f"Iniciando consolidação — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info(f"Modo: {'DRY RUN' if dry_run else 'REAL'} | IA: {'SIM' if usar_ia else 'NÃO'}")
    log.info("=" * 60)

    # Garante que as pastas existem
    for pasta in DESTINOS.values():
        if not dry_run:
            pasta.mkdir(parents=True, exist_ok=True)
    if not dry_run:
        BACKUP_BASE.mkdir(parents=True, exist_ok=True)

    # Lista arquivos da Inbox (só .md, ignora relatórios de consolidação)
    arquivos = [
        a for a in INBOX.glob("*.md")
        if "relatorio-consolidacao" not in a.name
    ]

    if not arquivos:
        log.info("Inbox vazia. Nada a fazer.")
        return

    log.info(f"Encontrados {len(arquivos)} arquivo(s) na Inbox.")

    # Backup antes de mover
    fazer_backup(dry_run)

    resultados = []

    for arq in arquivos:
        log.info(f"Processando: {arq.name}")

        # Tenta classificar por regras (grátis)
        destino = classificar_por_regras(arq)
        metodo = "regra"

        if destino is None and usar_ia:
            # Fallback para IA (Haiku — barato)
            log.info(f"  Regras não classificaram. Usando IA...")
            destino = classificar_com_ia(arq)
            metodo = "ia-haiku"
        elif destino is None:
            destino = "Arquivo"
            metodo = "fallback"

        sucesso = mover_arquivo(arq, destino, dry_run)

        resultados.append({
            "arquivo": arq.name,
            "destino": destino,
            "metodo": metodo,
            "sucesso": sucesso,
        })

    # Salva relatório
    salvar_relatorio(resultados, dry_run)

    log.info("=" * 60)
    log.info(f"Consolidação concluída. {len(resultados)} arquivo(s) processados.")
    log.info("=" * 60)


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Consolida arquivos da Inbox do vault Obsidian"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula sem mover nada (recomendado na primeira execução)"
    )
    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="Não usa API da Anthropic. Só regras determinísticas."
    )
    args = parser.parse_args()

    consolidar(
        dry_run=args.dry_run,
        usar_ia=not args.no_ai,
    )
