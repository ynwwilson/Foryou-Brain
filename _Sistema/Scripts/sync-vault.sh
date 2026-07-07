#!/bin/bash
# sync-vault.sh - Sincroniza o vault com o GitHub (pull + commit + push).
# Agendar a cada 5 min via LaunchAgent (macOS). Roda em silencio;
# se travar, cria um arquivo de alerta no Desktop.
VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$VAULT" || exit 1

ALERT="$HOME/Desktop/VAULT SYNC TRAVADO - LEIA.txt"
alert() {
    printf '[%s] %s\nAbra o terminal na pasta do vault e siga: _Sistema/Runbook - Destravar sync do vault (2026-07-06).md\n' \
        "$(date '+%Y-%m-%d %H:%M')" "$1" > "$ALERT"
}

# Outro processo git ativo (ex.: obsidian-git)? Sai sem fazer nada.
[ -f .git/index.lock ] && exit 0

# Merge travado de execucao anterior? Alerta e sai.
[ -f .git/MERGE_HEAD ] && { alert "Merge com conflito pendente."; exit 1; }

git fetch origin >/dev/null 2>&1

# 1. Commita mudancas locais
git add -A >/dev/null 2>&1
if [ -n "$(git status --porcelain)" ]; then
    git commit -m "vault: auto-sync $(date '+%Y-%m-%d %H:%M:%S') ($(hostname -s))" >/dev/null 2>&1
fi

# 2. Integra o remoto (merge). Conflito -> aborta, alerta, mantem tudo local intacto.
git pull origin main --no-rebase --no-edit >/dev/null 2>&1
if [ -f .git/MERGE_HEAD ]; then
    git merge --abort >/dev/null 2>&1
    alert "Pull gerou conflito (mesma nota editada em 2 PCs). Sync pausado ate resolver manualmente."
    exit 1
fi

# 3. Sobe
git push origin main >/dev/null 2>&1

# 4. Confere se subiu mesmo
git fetch origin >/dev/null 2>&1
AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null)
if [ "${AHEAD:-0}" -gt 0 ]; then
    alert "Push falhou ($AHEAD commits presos). Causas comuns: credencial sem permissao de escrita ou secret bloqueado pelo GitHub."
    exit 1
fi

# Tudo certo - limpa alerta antigo se existir
rm -f "$ALERT"
exit 0
