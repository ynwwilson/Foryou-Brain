#!/bin/bash
# instalar-sync.command - Instalador do sync automatico do vault (Marco / macOS).
# Duplo clique aqui. Roda uma vez e pronto.
# Faz tudo: sobe o que so existe neste Mac, baixa o resto, resolve conflito
# de cache sozinho e troca o agendador antigo (so pull) pelo sync completo.
cd "$(dirname "$0")/../.." || exit 1
VAULT="$(pwd)"
echo "Vault: $VAULT"
echo ""

falha() {
    echo ""
    echo "PROBLEMA: $1"
    echo "Manda um print desta janela pro Wilson."
    read -r -p "Enter pra fechar"
    exit 1
}

command -v git >/dev/null 2>&1 || falha "git nao esta instalado. Roda no Terminal: xcode-select --install  e depois roda este instalador de novo."

# Merge antigo pendente? Aborta (volta ao estado anterior, nada se perde).
[ -f .git/MERGE_HEAD ] && git merge --abort

# 1. Commita o que so existe neste Mac
echo "[1/5] Salvando o que so existe neste Mac..."
git add -A
git commit -m "vault: sync inicial deste PC" >/dev/null 2>&1

# 2. Baixa o remoto
echo "[2/5] Baixando o que esta no GitHub..."
git pull origin main --no-rebase --no-edit
if [ -f .git/MERGE_HEAD ]; then
    CONFLITOS=$(git diff --name-only --diff-filter=U)
    REAIS=$(echo "$CONFLITOS" | grep -v -E '^\.smart-env/|^\.obsidian/graph\.json$|^\.obsidian/workspace\.json$|\.tmp(\.|$)' || true)
    if [ -n "$REAIS" ]; then
        git merge --abort
        falha "Conflito em notas reais (mesma nota editada em 2 PCs): $REAIS - nada foi perdido, so precisa resolver manualmente."
    fi
    # Conflito so em arquivos de cache: resolve tirando do git (arquivo continua no disco)
    echo "$CONFLITOS" | while read -r f; do
        [ -n "$f" ] && git rm --cached --ignore-unmatch -r -- "$f" >/dev/null 2>&1
    done
    git commit --no-edit >/dev/null 2>&1
fi

# 3. Sobe
echo "[3/5] Subindo pro GitHub..."
git push origin main
git fetch origin >/dev/null 2>&1
AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null)
if [ "${AHEAD:-0}" -gt 0 ]; then
    echo ""
    echo "O push falhou - quase sempre e login do GitHub sem permissao de escrita."
    echo "Resolve assim: roda 'gh auth login' no Terminal (ou loga no GitHub Desktop)."
    echo "Depois roda este instalador de novo (pode rodar quantas vezes quiser)."
    read -r -p "Enter pra fechar"
    exit 1
fi

# 4. Prepara o script de sync
echo "[4/5] Preparando o script de sync..."
chmod +x "$VAULT/_Sistema/Scripts/sync-vault.sh"

# 5. Troca o agendador antigo (so pull) pelo sync completo
echo "[5/5] Instalando o sync automatico (a cada 5 min)..."
PLIST="$HOME/Library/LaunchAgents/com.foryou.vaultsync.plist"
launchctl unload "$PLIST" 2>/dev/null
mkdir -p "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.foryou.vaultsync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>$VAULT/_Sistema/Scripts/sync-vault.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF
launchctl load "$PLIST"

# Teste real
bash "$VAULT/_Sistema/Scripts/sync-vault.sh"

echo ""
echo "TUDO PRONTO. O vault agora sincroniza sozinho a cada 5 minutos, mesmo com o Obsidian fechado."
echo "Ultimo commit: $(git log -1 --pretty=format:'%h %s')"
echo ""
echo "Se um dia aparecer 'VAULT SYNC TRAVADO - LEIA.txt' na sua Mesa/Desktop, avisa o Wilson no mesmo dia."
read -r -p "Enter pra fechar"
exit 0
