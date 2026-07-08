#!/bin/bash
# instalar-sync-marco.command - Instalador standalone do sync do vault (macOS).
# Roda de QUALQUER pasta (Downloads, Desktop...). Acha o vault sozinho,
# destrava o git, sobe o que so existe neste Mac, baixa o resto e instala
# o sync automatico de 5 min.
# Como rodar: abre o Terminal, digita  bash  (com espaco), arrasta este
# arquivo pra janela e aperta Enter.

falha() {
    echo ""
    echo "PROBLEMA: $1"
    echo "Manda um print desta janela pro Wilson."
    exit 1
}

command -v git >/dev/null 2>&1 || falha "git nao esta instalado. Roda no Terminal: xcode-select --install  e depois roda este arquivo de novo."

# --- 1. Acha a pasta do vault (repo Foryou-Brain) ---
# Pode existir mais de uma copia do repo; o vault VIVO e o que tem o
# .obsidian/workspace.json mais recente (Obsidian atualiza sempre que usado).
echo "[1/5] Procurando a pasta do vault neste Mac (pode demorar 1-2 min)..."
VAULT=""
MELHOR=0
for d in "$HOME/Desktop" "$HOME/Documents" "$HOME/Downloads" "$HOME"; do
    [ -d "$d" ] || continue
    while IFS= read -r cfg; do
        if grep -q "Foryou-Brain" "$cfg" 2>/dev/null; then
            CAND="$(dirname "$(dirname "$cfg")")"
            WS="$CAND/.obsidian/workspace.json"
            if [ -f "$WS" ]; then USO=$(stat -f %m "$WS" 2>/dev/null || echo 1); else USO=0; fi
            if [ "$USO" -gt "$MELHOR" ] || [ -z "$VAULT" ]; then
                MELHOR=$USO
                VAULT="$CAND"
            fi
        fi
    done < <(find "$d" -maxdepth 5 \( -path "$HOME/Library" -o -name node_modules \) -prune -o -type f -path "*/.git/config" -print 2>/dev/null)
done
[ -n "$VAULT" ] || falha "Nao achei a pasta do vault (Foryou-Brain) neste Mac."
echo "Vault encontrado: $VAULT"
cd "$VAULT" || falha "Nao consegui entrar na pasta do vault."

# --- 2. Destrava e salva o que so existe aqui ---
echo "[2/5] Destravando e salvando o que so existe neste Mac..."
[ -f .git/MERGE_HEAD ] && git merge --abort
git add -A
git commit -m "vault: sync inicial deste PC" >/dev/null 2>&1

# --- 3. Baixa o que esta no GitHub ---
echo "[3/5] Baixando o que esta no GitHub..."
git pull origin main --no-rebase --no-edit
if [ -f .git/MERGE_HEAD ]; then
    CONFLITOS=$(git diff --name-only --diff-filter=U)
    REAIS=$(echo "$CONFLITOS" | grep -v -E '^\.smart-env/|^\.obsidian/graph\.json$|^\.obsidian/workspace\.json$|\.tmp(\.|$)' || true)
    if [ -n "$REAIS" ]; then
        git merge --abort
        falha "Conflito em notas reais: $REAIS - nada foi perdido, precisa resolver manual."
    fi
    echo "$CONFLITOS" | while read -r f; do
        [ -n "$f" ] && git rm --cached --ignore-unmatch -r -- "$f" >/dev/null 2>&1
    done
    git commit --no-edit >/dev/null 2>&1
fi

# --- 4. Sobe ---
echo "[4/5] Subindo pro GitHub..."
git push origin main
git fetch origin >/dev/null 2>&1
AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null)
if [ "${AHEAD:-0}" -gt 0 ]; then
    echo ""
    echo "O push falhou - quase sempre e login do GitHub sem permissao de escrita."
    echo "Resolve assim: roda 'gh auth login' no Terminal (ou loga no GitHub Desktop)."
    echo "Depois roda este arquivo de novo (pode repetir a vontade, e seguro)."
    exit 1
fi

# --- 5. Instala o sync automatico (a cada 5 min) ---
echo "[5/5] Instalando o sync automatico..."
SYNC="$VAULT/_Sistema/Scripts/sync-vault.sh"
[ -f "$SYNC" ] || falha "O pull nao trouxe _Sistema/Scripts/sync-vault.sh."
chmod +x "$SYNC"
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
        <string>$SYNC</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF
launchctl load "$PLIST"
bash "$SYNC"

echo ""
echo "TUDO PRONTO. O vault agora sincroniza sozinho a cada 5 minutos, mesmo com o Obsidian fechado."
echo "Ultimo commit: $(git log -1 --pretty=format:'%h %s')"
echo ""
echo "Se um dia aparecer 'VAULT SYNC TRAVADO - LEIA.txt' na sua Mesa/Desktop, avisa o Wilson no mesmo dia."
