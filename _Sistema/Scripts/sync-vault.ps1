# sync-vault.ps1 - Sincroniza o vault com o GitHub (pull + commit + push).
# Agendar a cada 5 min via Task Scheduler (Windows). Roda em silencio;
# se travar, cria um arquivo de alerta no Desktop.
$ErrorActionPreference = 'Continue'
$vault = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $vault

$alertFile = Join-Path ([Environment]::GetFolderPath('Desktop')) 'VAULT SYNC TRAVADO - LEIA.txt'
function Alert($msg) {
    $texto = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm')] $msg`r`n" +
             "Abra o terminal na pasta do vault e siga: _Sistema/Runbook - Destravar sync do vault (2026-07-06).md`r`n" +
             "(no vault o arquivo usa travessao no nome)"
    $texto | Out-File -FilePath $alertFile -Encoding utf8
}

# Outro processo git ativo (ex.: obsidian-git)? Sai sem fazer nada.
if (Test-Path (Join-Path $vault '.git\index.lock')) { exit 0 }

# Merge travado de execucao anterior? Alerta e sai.
if (Test-Path (Join-Path $vault '.git\MERGE_HEAD')) { Alert 'Merge com conflito pendente.'; exit 1 }

git fetch origin 2>&1 | Out-Null

# 1. Commita mudancas locais
git add -A 2>&1 | Out-Null
$pending = git status --porcelain
if ($pending) {
    git commit -m "vault: auto-sync $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ($env:COMPUTERNAME)" 2>&1 | Out-Null
}

# 2. Integra o remoto (merge). Conflito -> aborta, alerta, mantem tudo local intacto.
git pull origin main --no-rebase --no-edit 2>&1 | Out-Null
if (Test-Path (Join-Path $vault '.git\MERGE_HEAD')) {
    git merge --abort 2>&1 | Out-Null
    Alert 'Pull gerou conflito (mesma nota editada em 2 PCs). Sync pausado ate resolver manualmente.'
    exit 1
}

# 3. Sobe
git push origin main 2>&1 | Out-Null

# 4. Confere se subiu mesmo (push silenciosamente rejeitado = commits presos)
git fetch origin 2>&1 | Out-Null
$ahead = [int](git rev-list --count origin/main..HEAD)
if ($ahead -gt 0) {
    Alert "Push falhou ($ahead commits presos). Causas comuns: credencial sem permissao de escrita ou secret bloqueado pelo GitHub."
    exit 1
}

# Tudo certo - limpa alerta antigo se existir
if (Test-Path $alertFile) { Remove-Item $alertFile -Force }
exit 0
