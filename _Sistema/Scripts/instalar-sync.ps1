# instalar-sync.ps1 - Instalador do sync automatico do vault (Windows).
# Rodar UMA vez, com duplo clique no "instalar-sync.bat" desta mesma pasta.
# Faz tudo: sobe o que so existe neste PC, baixa o resto, resolve conflito
# de cache sozinho e instala a tarefa agendada (a cada 5 min).
$ErrorActionPreference = 'Continue'
$vault = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $vault
Write-Host "Vault: $vault"
Write-Host ""

function Falha($msg) {
    Write-Host ""
    Write-Host "PROBLEMA: $msg" -ForegroundColor Red
    Write-Host "Manda um print desta janela pro Wilson."
    Read-Host "Enter pra fechar"
    exit 1
}

git --version *> $null
if ($LASTEXITCODE -ne 0) { Falha "git nao esta instalado. Baixar em https://git-scm.com/download/win e rodar este instalador de novo." }

# Merge antigo pendente? Aborta (volta ao estado anterior, nada se perde).
if (Test-Path '.git\MERGE_HEAD') { git merge --abort }

# 1. Commita o que so existe neste PC
Write-Host "[1/4] Salvando o que so existe neste PC..."
git add -A
git commit -m "vault: sync inicial deste PC" 2>$null | Out-Null

# 2. Baixa o remoto
Write-Host "[2/4] Baixando o que esta no GitHub..."
git pull origin main --no-rebase --no-edit
if (Test-Path '.git\MERGE_HEAD') {
    $conflitos = @(git diff --name-only --diff-filter=U)
    $reais = @($conflitos | Where-Object {
        $_ -notmatch '^\.smart-env/' -and
        $_ -ne '.obsidian/graph.json' -and
        $_ -ne '.obsidian/workspace.json' -and
        $_ -notmatch '\.tmp(\.|$)'
    })
    if ($reais.Count -gt 0) {
        git merge --abort
        Falha "Conflito em notas reais (mesma nota editada em 2 PCs): $($reais -join ', '). Nada foi perdido - so precisa resolver manualmente."
    }
    # Conflito so em arquivos de cache: resolve tirando do git (arquivo continua no disco)
    foreach ($f in $conflitos) { git rm --cached --ignore-unmatch -r -- $f | Out-Null }
    git commit --no-edit | Out-Null
}

# 3. Sobe
Write-Host "[3/4] Subindo pro GitHub..."
git push origin main
git fetch origin 2>&1 | Out-Null
$ahead = [int](git rev-list --count origin/main..HEAD)
if ($ahead -gt 0) {
    Write-Host ""
    Write-Host "O push falhou - quase sempre e login do GitHub sem permissao de escrita." -ForegroundColor Yellow
    Write-Host "Resolve assim: abre o GitHub Desktop e loga na sua conta, OU roda 'gh auth login' no terminal."
    Write-Host "Depois roda este instalador de novo (pode rodar quantas vezes quiser)."
    Read-Host "Enter pra fechar"
    exit 1
}

# 4. Instala a tarefa agendada (a cada 5 min)
Write-Host "[4/4] Instalando o sync automatico..."
$syncScript = Join-Path $vault '_Sistema\Scripts\sync-vault.ps1'
schtasks /create /f /tn "VaultSyncFull" /sc minute /mo 5 /tr "powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File \`"$syncScript\`"" | Out-Null
if ($LASTEXITCODE -ne 0) { Falha "Nao consegui criar a tarefa agendada. Fecha e roda de novo: botao direito no instalar-sync.bat > Executar como administrador." }
schtasks /run /tn "VaultSyncFull" | Out-Null

Write-Host ""
Write-Host "TUDO PRONTO. O vault agora sincroniza sozinho a cada 5 minutos, mesmo com o Obsidian fechado." -ForegroundColor Green
Write-Host "Ultimo commit: $(git log -1 --pretty=format:'%h %s')"
Write-Host ""
Write-Host "Se um dia aparecer 'VAULT SYNC TRAVADO - LEIA.txt' na sua Area de Trabalho, avisa o Wilson no mesmo dia."
Read-Host "Enter pra fechar"
exit 0
