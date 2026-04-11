---
name: obsidian
description: Vault Obsidian de Mestre — cerebro de memoria estruturada. Usar para ler, criar e atualizar notas, buscar conhecimento e manter a memoria do sistema.
---

# Obsidian — Cerebro de Memoria

## Vault

**PC:** `C:\Users\ynwwi\Projects\jarvis\stark\Stark\`
**VPS:** `/root/stark/`

O vault E o workspace do OpenClaw. Todos os arquivos .md sao notas do Obsidian.

---

## Estrutura do Vault

```
/root/stark/
├── 🧠 Meu Cerebro.md     ← MOC — indice central, sempre ler primeiro
├── MEMORY.md              ← HOT layer — bootstrap de contexto
├── memory/                ← logs brutos + topic files
│   ├── YYYY-MM-DD.md     ← diarios diarios
│   ├── decisions.md       ← decisoes permanentes
│   ├── lessons.md         ← licoes aprendidas
│   ├── people.md          ← contatos
│   ├── projects.md        ← indice projetos
│   └── feedback/          ← feedbacks JSON para aprendizado
├── Pessoas/               ← notas estruturadas de pessoas
├── Projetos/              ← notas estruturadas de projetos
├── Decisoes/              ← decisoes com contexto
├── Licoes/                ← licoes aprendidas estruturadas
├── Diarios/               ← diarios estruturados
├── Templates/             ← templates de notas
└── scripts/
    └── memory_bridge.py   ← ponte HOT/WARM/COLD
```

---

## Como Usar o memory_bridge.py

```bash
# HOT — carrega MOC + MEMORY.md (sempre fazer isso primeiro)
python /root/stark/scripts/memory_bridge.py hot

# WARM — notas por tag
python /root/stark/scripts/memory_bridge.py warm foryoucode
python /root/stark/scripts/memory_bridge.py warm projeto

# WARM — diarios recentes
python /root/stark/scripts/memory_bridge.py warm --days 3

# COLD — busca full-text no vault inteiro
python /root/stark/scripts/memory_bridge.py cold "VPS configuracao"
python /root/stark/scripts/memory_bridge.py cold "ForYou Code stack"

# Stats do vault
python /root/stark/scripts/memory_bridge.py stats

# Salvar feedback
python /root/stark/scripts/memory_bridge.py feedback "usuario corrigiu X"
```

---

## Fluxo de Leitura (padrao)

1. `python /root/stark/scripts/memory_bridge.py hot` — carregar contexto base
2. Se precisar de mais detalhe: `cold "termo"` ou ler arquivo diretamente
3. Nunca adivinhar — sempre buscar antes de afirmar

## Fluxo de Escrita (padrao)

### Nova nota
```bash
cat > /root/stark/Projetos/Nome do Projeto.md << 'EOF'
---
title: "Nome"
type: projeto
created: 2026-03-26
tags: [projeto]
status: ativo
---

# Nome
...
EOF
```

### Atualizar nota existente
Ler o arquivo, editar o conteudo, salvar de volta.

### Novo diario
```bash
# Arquivo em memory/ (raw) E em Diarios/ (estruturado)
DATE=$(date +%Y-%m-%d)
echo "# $DATE\n\n## O que aconteceu\n-" >> /root/stark/memory/$DATE.md
```

### Nova licao
Criar em `Licoes/Titulo da Licao.md` com template de licao.
Adicionar link no MOC (`🧠 Meu Cerebro.md`).

---

## Regras

- Sempre ler o MOC antes de criar notas novas (evita duplicatas)
- Wikilinks: `[[Nome da Nota]]` para conectar notas
- Frontmatter YAML em todas as notas novas
- MEMORY.md: max 6KB, so o essencial
- MOC: max ~3000 chars, so links e resumos curtos
- Ao criar nota nova, adicionar link no MOC na secao certa
