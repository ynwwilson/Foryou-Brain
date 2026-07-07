# sync-vault.ps1 - Sincroniza o vault com o GitHub (pull + commit + push).
# Agendar a cada 5 min via Task Scheduler (Windows). Roda em silencio;
# se travar, cria um arquivo de alerta no Desktop.
$ErrorActionPreference = 'Continue'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
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

# 0.5 Redige secrets em notas alteradas ANTES de commitar.
# Transcripts de sessao salvos pelos watchers costumam conter API keys;
# 1 token real bloqueia o push do vault inteiro (GitHub Push Protection).
# Originais vao pro Cofre Local (gitignored).
$secretPatterns = [ordered]@{
    'ANTHROPIC'   = 'sk-ant-[A-Za-z0-9\-_]{16,}'
    'OPENAI'      = 'sk-proj-[A-Za-z0-9\-_]{16,}|sk-[A-Za-z0-9]{40,}'
    'GITHUB'      = 'ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|gho_[A-Za-z0-9]{30,}'
    'APIFY'       = 'apify_api_[A-Za-z0-9]{20,}'
    'SENTRY'      = 'sntry[us]?s?_[A-Za-z0-9=+/\._\-]{30,}'
    'GROQ'        = 'gsk_[A-Za-z0-9]{20,}'
    'CLOUDFLARE'  = 'cfat_[A-Za-z0-9\-_]{20,}'
    'VERCEL'      = 'vcp_[A-Za-z0-9]{20,}'
    'GOOGLE'      = 'AIza[0-9A-Za-z\-_]{30,}'
    'SLACK'       = 'xox[baprs]-[A-Za-z0-9\-]{10,}'
    'AWS'         = 'AKIA[0-9A-Z]{16}'
    'STRIPE'      = '[sp]k_live_[A-Za-z0-9]{20,}'
    'SUPABASE'    = 'sbp_[A-Za-z0-9]{30,}'
    'HUGGINGFACE' = 'hf_[A-Za-z0-9]{30,}'
    'REPLICATE'   = 'r8_[A-Za-z0-9]{30,}'
    'RESEND'      = 're_[A-Za-z0-9]{20,}_[A-Za-z0-9]{5,}'
    'FALAI'       = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}:[0-9a-f]{16,}'
    'TELEGRAM'    = '\b\d{8,10}:AA[A-Za-z0-9_\-]{30,}'
    'JWT'         = 'eyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}'
}
$mudados = git -c core.quotepath=false status --porcelain 2>$null |
    ForEach-Object { ($_.Substring(3).Trim('"')) -replace '^.* -> ', '' } |
    Where-Object { $_ -like '*.md' -and $_ -notlike '_Sistema/Cofre Local/*' }
foreach ($rel in $mudados) {
    $p = Join-Path $vault ($rel -replace '/', '\')
    if (-not (Test-Path -LiteralPath $p)) { continue }
    try { $text = [System.IO.File]::ReadAllText($p) } catch { continue }
    $orig = $text
    $achados = New-Object System.Collections.Generic.List[string]
    foreach ($k in $secretPatterns.Keys) {
        $rx = [regex]$secretPatterns[$k]
        foreach ($m in $rx.Matches($text)) { $achados.Add("- **$k** em ``$rel``: ``$($m.Value)``") }
        $text = $rx.Replace($text, "[REDACTED-$k]")
    }
    if ($text -ne $orig) {
        [System.IO.File]::WriteAllText($p, $text)
        $cofre = Join-Path $vault '_Sistema\Cofre Local'
        if (-not (Test-Path $cofre)) { New-Item -ItemType Directory -Path $cofre | Out-Null }
        $log = Join-Path $cofre 'segredos-redigidos-auto.md'
        [System.IO.File]::AppendAllText($log, "`r`n## $(Get-Date -Format 'yyyy-MM-dd HH:mm')`r`n" + ($achados -join "`r`n") + "`r`n")
    }
}

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
