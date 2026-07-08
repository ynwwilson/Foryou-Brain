<# :
@echo off
rem instalar-sync-eduardo.bat - Instalador standalone do sync do vault (Windows).
title Instalador Sync Vault ForYou
powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ([IO.File]::ReadAllText('%~f0'))"
pause
exit /b
#>
# ============================================================
# PowerShell daqui pra baixo. Roda de QUALQUER pasta (Downloads,
# Desktop...). Acha o vault sozinho, destrava o git, sobe o que
# so existe neste PC, baixa o resto e instala o sync de 5 min.
# ============================================================
$ErrorActionPreference = 'Continue'

function Falha($msg) {
    Write-Host ""
    Write-Host "PROBLEMA: $msg" -ForegroundColor Red
    Write-Host "Manda um print desta janela pro Wilson."
}

git --version *> $null
if ($LASTEXITCODE -ne 0) { Falha "git nao esta instalado. Baixar em https://git-scm.com/download/win , instalar e rodar este arquivo de novo."; return }

# --- 1. Acha a pasta do vault (repo Foryou-Brain) ---
# Pode existir mais de uma copia do repo no PC; o vault VIVO e o que tem
# o .obsidian/workspace.json mais recente (Obsidian atualiza sempre que usado).
Write-Host "[1/5] Procurando a pasta do vault neste PC (pode demorar 1-2 min)..."
$candidatos = New-Object System.Collections.Generic.List[object]
foreach ($tenta in @(
    @("$env:USERPROFILE\Desktop", 3),
    @("$env:USERPROFILE\Documents", 4),
    @("$env:USERPROFILE\Downloads", 3),
    @("$env:USERPROFILE\OneDrive\Desktop", 3),
    @("$env:USERPROFILE\OneDrive\Documents", 4),
    @("$env:USERPROFILE", 4)
)) {
    $root = $tenta[0]; $depth = $tenta[1]
    if (-not (Test-Path $root)) { continue }
    $dirs = @(Get-Item $root -ErrorAction SilentlyContinue) + @(Get-ChildItem -Path $root -Directory -Recurse -Depth $depth -ErrorAction SilentlyContinue)
    foreach ($d in $dirs) {
        if ($d.FullName -match 'node_modules|\\AppData\\|\$Recycle') { continue }
        $cfg = Join-Path $d.FullName '.git\config'
        if ((Test-Path $cfg) -and (Select-String -Path $cfg -Pattern 'Foryou-Brain' -Quiet)) {
            $ws = Join-Path $d.FullName '.obsidian\workspace.json'
            $mtime = if (Test-Path $ws) { (Get-Item $ws).LastWriteTime } else { [datetime]::MinValue }
            if (-not ($candidatos | Where-Object { $_.Path -eq $d.FullName })) {
                $candidatos.Add([pscustomobject]@{ Path = $d.FullName; Uso = $mtime })
            }
        }
    }
}
if ($candidatos.Count -eq 0) { Falha "Nao achei a pasta do vault (Foryou-Brain) neste PC."; return }
$vault = ($candidatos | Sort-Object Uso -Descending | Select-Object -First 1).Path
if ($candidatos.Count -gt 1) {
    Write-Host "Achei $($candidatos.Count) copias do repo; usando a mais usada no Obsidian:"
    $candidatos | Sort-Object Uso -Descending | ForEach-Object { Write-Host "  - $($_.Path) (uso: $($_.Uso))" }
}
Write-Host "Vault encontrado: $vault" -ForegroundColor Green
Set-Location $vault

# --- 2. Destrava e salva o que so existe aqui ---
Write-Host "[2/5] Destravando e salvando o que so existe neste PC..."
if (Test-Path '.git\MERGE_HEAD') { git merge --abort }
git add -A
git commit -m "vault: sync inicial deste PC" 2>$null | Out-Null

# --- 3. Baixa o que esta no GitHub ---
Write-Host "[3/5] Baixando o que esta no GitHub..."
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
        Falha "Conflito em notas reais: $($reais -join ', '). Nada foi perdido - precisa resolver manual."
        return
    }
    foreach ($f in $conflitos) { git rm --cached --ignore-unmatch -r -- $f | Out-Null }
    git commit --no-edit | Out-Null
}

# --- 4. Sobe ---
Write-Host "[4/5] Subindo pro GitHub..."
git push origin main
git fetch origin 2>&1 | Out-Null
$ahead = [int](git rev-list --count origin/main..HEAD)
if ($ahead -gt 0) {
    Write-Host ""
    Write-Host "O push falhou - quase sempre e login do GitHub sem permissao de escrita." -ForegroundColor Yellow
    Write-Host "Resolve assim: abre o GitHub Desktop e loga, OU roda 'gh auth login' no PowerShell."
    Write-Host "Depois roda este arquivo de novo (pode repetir a vontade, e seguro)."
    return
}

# --- 5. Instala o sync automatico (a cada 5 min) ---
Write-Host "[5/5] Instalando o sync automatico..."
$syncScript = Join-Path $vault '_Sistema\Scripts\sync-vault.ps1'
if (-not (Test-Path $syncScript)) { Falha "O pull nao trouxe _Sistema\Scripts\sync-vault.ps1."; return }
schtasks /create /f /tn "VaultSyncFull" /sc minute /mo 5 /tr "powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File \`"$syncScript\`"" | Out-Null
if ($LASTEXITCODE -ne 0) { Falha "Nao consegui criar a tarefa agendada. Botao direito neste arquivo > Executar como administrador."; return }
schtasks /run /tn "VaultSyncFull" | Out-Null

Write-Host ""
Write-Host "TUDO PRONTO. O vault agora sincroniza sozinho a cada 5 minutos, mesmo com o Obsidian fechado." -ForegroundColor Green
Write-Host "Ultimo commit: $(git log -1 --pretty=format:'%h %s')"
Write-Host ""
Write-Host "Se um dia aparecer 'VAULT SYNC TRAVADO - LEIA.txt' na sua Area de Trabalho, avisa o Wilson no mesmo dia."
