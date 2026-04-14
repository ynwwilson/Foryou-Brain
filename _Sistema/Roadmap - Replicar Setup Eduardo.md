---
date: 2026-04-14
tags: [roadmap, sistema, eduardo, setup]
---

# Roadmap — Replicar Setup Completo no PC do Eduardo

> Vault Eduardo: `C:\Users\eduar\Foryou-Brain`
> API Key Obsidian: `7b03eb071579b195785f1802576b81ffefd389b5845a21b463c3aa12fa4e8bb3`

---

## ✅ ETAPA 1 — Obsidian: plugins e configurações — CONCLUÍDA

Todos plugins ativados, obsidian-git configurado, API Key obtida.

---

## ✅ ETAPA 2 — Pré-requisitos — CONCLUÍDA

Node v24.14.1 · npm 11.11.0 · git 2.53.0 · pastas criadas.

---

## ✅ ETAPA 3 — Session Saver + Hooks + Claude Code + pm2 — CONCLUÍDA

Rodar cada bloco no PowerShell em sequência.

### 3.1 — Criar config.json

```powershell
$config = @'
{
  "vaultPath": "C:/Users/eduar/Foryou-Brain",
  "author": "Eduardo",
  "tools": {
    "claude1":       { "folder": "Claude 1",    "name": "Claude"      },
    "claude-nova":   { "folder": "Claude Nova", "name": "Claude Nova" },
    "codex":         { "folder": "Codex",       "name": "Codex"       },
    "antigravity":   { "folder": "Antigravity", "name": "Antigravity" }
  },
  "codexSessionsPath": "C:/Users/eduar/.codex/sessions",
  "antigravityBrainPath": "C:/Users/eduar/.gemini/antigravity/brain",
  "heartbeatMaxAge": 120000,
  "maxTextLength": 800,
  "maxExchanges": 15,
  "catchUpDays": 7,
  "nodePath": "C:/Program Files/nodejs/node.exe"
}
'@
New-Item -Path "C:\Users\eduar\.session-saver" -ItemType Directory -Force
Set-Content -Path "C:\Users\eduar\.session-saver\config.json" -Value $config -Encoding UTF8
Write-Host "config.json criado"
```

### 3.2 — Copiar hooks do vault e instalar dependências

```powershell
# Pull do vault primeiro para garantir scripts atualizados
cd "C:\Users\eduar\Foryou-Brain"
git pull

# Copiar hooks
Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\session-saver.js" "C:\Users\eduar\.claude\hooks\" -Force
Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\codex-watcher.js" "C:\Users\eduar\.claude\hooks\" -Force
Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\antigravity-watcher.js" "C:\Users\eduar\.claude\hooks\" -Force
Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\package.json" "C:\Users\eduar\.claude\hooks\" -Force

# Instalar dependências
cd "C:\Users\eduar\.claude\hooks"
npm install
Write-Host "hooks instalados"
```

### 3.3 — Criar settings.json Claude 1

```powershell
$settings = @'
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "\"C:/Program Files/nodejs/node.exe\" C:/Users/eduar/.claude/hooks/session-saver.js"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "\"C:/Program Files/nodejs/node.exe\" C:/Users/eduar/.claude/hooks/session-saver.js"
          }
        ]
      }
    ]
  },
  "permissions": {
    "allow": ["Bash(*)"]
  },
  "mcpServers": {
    "obsidian": {
      "command": "C:\\Users\\eduar\\Foryou-Brain\\.obsidian\\plugins\\mcp-tools\\bin\\mcp-server.exe",
      "args": [],
      "env": {
        "OBSIDIAN_API_KEY": "7b03eb071579b195785f1802576b81ffefd389b5845a21b463c3aa12fa4e8bb3"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\eduar\\Foryou-Brain"]
    }
  }
}
'@
New-Item -Path "C:\Users\eduar\.claude" -ItemType Directory -Force
Set-Content -Path "C:\Users\eduar\.claude\settings.json" -Value $settings -Encoding UTF8
Write-Host "settings.json Claude 1 criado"
```

### 3.4 — Criar settings.json Claude Nova

```powershell
New-Item -Path "C:\Users\eduar\.claude-nova" -ItemType Directory -Force
Set-Content -Path "C:\Users\eduar\.claude-nova\settings.json" -Value $settings -Encoding UTF8
Write-Host "settings.json Claude Nova criado"
```

### 3.5 — Criar CLAUDE.md Claude 1

```powershell
$claudeMd = @'
## Auto-Context de Sessão

Ao iniciar qualquer sessão, leia as últimas 30 linhas da nota mais recente em:
`C:/Users/eduar/Foryou-Brain/Claude 1/Sessões/Eduardo/`

Para encontrar a nota mais recente: é o arquivo `.md` com o nome mais alto em ordem alfabética (os nomes começam com data `YYYY-MM-DD HHhMM`). Ignore a pasta `_completo/`.

Se a pasta estiver vazia ou não existir, ignore silenciosamente e continue normalmente.
'@
Set-Content -Path "C:\Users\eduar\.claude\CLAUDE.md" -Value $claudeMd -Encoding UTF8
Write-Host "CLAUDE.md Claude 1 criado"
```

### 3.6 — Criar CLAUDE.md Claude Nova

```powershell
$claudeNovaMd = @'
## Auto-Context de Sessão

Ao iniciar qualquer sessão, leia as últimas 30 linhas da nota mais recente em:
`C:/Users/eduar/Foryou-Brain/Claude Nova/Sessões/Eduardo/`

Para encontrar a nota mais recente: é o arquivo `.md` com o nome mais alto em ordem alfabética (os nomes começam com data `YYYY-MM-DD HHhMM`). Ignore a pasta `_completo/`.

Se a pasta estiver vazia ou não existir, ignore silenciosamente e continue normalmente.
'@
Set-Content -Path "C:\Users\eduar\.claude-nova\CLAUDE.md" -Value $claudeNovaMd -Encoding UTF8
Write-Host "CLAUDE.md Claude Nova criado"
```

### 3.7 — Registrar watchers no pm2

```powershell
pm2 start "C:/Users/eduar/.claude/hooks/codex-watcher.js" --name codex-watcher --interpreter "C:/Program Files/nodejs/node.exe"
pm2 start "C:/Users/eduar/.claude/hooks/antigravity-watcher.js" --name antigravity-watcher --interpreter "C:/Program Files/nodejs/node.exe"
pm2 save
pm2 list
```

Resultado esperado: `codex-watcher` e `antigravity-watcher` com status `online`.

---

## ✅ ETAPA 4 — Task Scheduler: pm2 no boot — CONCLUÍDA

Abrir PowerShell como **Administrador** e rodar tudo de uma vez:

```powershell
New-Item -Path "C:\pm2-startup" -ItemType Directory -Force
Set-Content -Path "C:\pm2-startup\pm2-resurrect.bat" -Value "@echo off`r`n`"C:\Program Files\nodejs\node.exe`" `"C:\Users\eduar\AppData\Roaming\npm\node_modules\pm2\bin\pm2`" resurrect" -Encoding ASCII

$action = New-ScheduledTaskAction -Execute "C:\pm2-startup\pm2-resurrect.bat"
$trigger = New-ScheduledTaskTrigger -AtLogOn -User "eduar"
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit 0
Register-ScheduledTask -TaskName "PM2 Auto Start" -Action $action -Trigger $trigger -Settings $settings -RunLevel Highest -Force

Get-ScheduledTask -TaskName "PM2 Auto Start"
```

Resultado esperado: `TaskName: PM2 Auto Start` com `State: Ready`.

---

## ✅ ETAPA 5 — Windows Defender: exclusões — CONCLUÍDA

Abrir PowerShell como **Administrador**:

```powershell
Add-MpPreference -ExclusionPath "C:\Users\eduar\.claude"
Add-MpPreference -ExclusionPath "C:\Users\eduar\.claude-nova"
Add-MpPreference -ExclusionPath "C:\Users\eduar\.session-saver"
Add-MpPreference -ExclusionPath "C:\Users\eduar\AppData\Roaming\npm"
Add-MpPreference -ExclusionProcess "node.exe"
Add-MpPreference -ExclusionProcess "pm2"
Write-Host "Exclusões adicionadas"
```

---

## ✅ ETAPA 6 — Teste final — CONCLUÍDA

```powershell
# Abrir Claude e testar
claude
```

1. Digitar qualquer mensagem
2. Fechar com `/exit`
3. Verificar nota criada:

```powershell
ls "C:\Users\eduar\Foryou-Brain\Claude 1\Sessões\Eduardo\"
```

Deve aparecer um arquivo `.md`. Se aparecer → tudo funcionando.

---

## ✅ SETUP COMPLETO — 2026-04-14

Sessões salvando corretamente em `Claude Nova/Sessões/Eduardo/` e `Claude 1/Sessões/Eduardo/`.
MCP Tools gerencia conexão com Obsidian automaticamente — aviso de "Local REST API" é ruído, não erro.

---

## RESUMO

| Item | Valor |
|---|---|
| Vault | `C:/Users/eduar/Foryou-Brain` |
| Author | `Eduardo` |
| Node | `C:/Program Files/nodejs/node.exe` |
| API Key Obsidian | `7b03eb07...` (já embutida nos comandos) |
| MCP Tools exe | `C:\Users\eduar\Foryou-Brain\.obsidian\plugins\mcp-tools\bin\mcp-server.exe` |
