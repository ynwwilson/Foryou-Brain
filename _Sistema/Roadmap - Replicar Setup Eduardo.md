---
date: 2026-04-14
tags: [roadmap, sistema, eduardo, setup]
---

# Roadmap — Replicar Setup Completo no PC do Eduardo

> Base: setup Wilson funcionando 100% em 2026-04-14.
> Vault Eduardo: `C:\Users\eduar\Foryou-Brain`
> Ferramentas: Claude 1, Claude Nova (Codex e Antigravity quando instalar)

---

## ✅ ETAPA 1 — Obsidian: plugins e configurações — CONCLUÍDA

### ✅ 1.1 Plugins ativados
Todos os plugins ativados: obsidian-git, Local REST API, Dataview, Smart Connections, MCP Tools, Style Settings, Icon Folder, Banners, Open in Terminal.

### ✅ 1.2 obsidian-git configurado
Auto save: 10min · Auto push: 5min · Auto pull: 5min · Pull on startup: ✅

### ✅ 1.3 API Key do Local REST API obtida
```
7b03eb071579b195785f1802576b81ffefd389b5845a21b463c3aa12fa4e8bb3
```

---

## ✅ ETAPA 2 — Node.js — CONCLUÍDA

- Node v24.14.1 ✅
- npm 11.11.0 ✅
- git 2.53.0 ✅
- Pastas `~/.claude/hooks` e `~/.session-saver/cache` criadas ✅

---

## ⚠️ ETAPA 3 — Session Saver: criar arquivos — EM ANDAMENTO

### 3.1 Criar config.json

No PowerShell, rodar o bloco completo:

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
```

Verificar:
```powershell
cat C:\Users\eduar\.session-saver\config.json
```

### 3.2 Copiar os hooks

```powershell
New-Item -Path "C:\Users\eduar\.claude\hooks" -ItemType Directory -Force
New-Item -Path "C:\Users\eduar\.session-saver\cache" -ItemType Directory -Force

Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\session-saver.js" "C:\Users\eduar\.claude\hooks\"
Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\codex-watcher.js" "C:\Users\eduar\.claude\hooks\"
Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\antigravity-watcher.js" "C:\Users\eduar\.claude\hooks\"
Copy-Item "C:\Users\eduar\Foryou-Brain\_Sistema\Scripts\package.json" "C:\Users\eduar\.claude\hooks\"
```

> Se os scripts não estiverem em `_Sistema/Scripts/`, copiar manualmente do PC do Wilson.

### 3.3 Instalar dependências

```powershell
cd C:\Users\eduar\.claude\hooks
npm install
```

---

## ETAPA 4 — Claude Code: configurar hooks

### 4.1 Criar settings.json do Claude 1

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
    "allow": [
      "Bash(*)"
    ]
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
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\eduar\\Foryou-Brain"
      ]
    }
  }
}
'@
New-Item -Path "C:\Users\eduar\.claude" -ItemType Directory -Force
Set-Content -Path "C:\Users\eduar\.claude\settings.json" -Value $settings -Encoding UTF8
```

### 4.2 Criar settings.json do Claude Nova

```powershell
New-Item -Path "C:\Users\eduar\.claude-nova" -ItemType Directory -Force
Set-Content -Path "C:\Users\eduar\.claude-nova\settings.json" -Value $settings -Encoding UTF8
```

### 4.3 Criar CLAUDE.md do Claude 1

```powershell
$claudeMd = @'
## Auto-Context de Sessão

Ao iniciar qualquer sessão, leia as últimas 30 linhas da nota mais recente em:
`C:/Users/eduar/Foryou-Brain/Claude 1/Sessões/Eduardo/`

Para encontrar a nota mais recente: é o arquivo `.md` com o nome mais alto em ordem alfabética (os nomes começam com data `YYYY-MM-DD HHhMM`). Ignore a pasta `_completo/`.

Se a pasta estiver vazia ou não existir, ignore silenciosamente e continue normalmente.
'@
Set-Content -Path "C:\Users\eduar\.claude\CLAUDE.md" -Value $claudeMd -Encoding UTF8
```

### 4.4 Criar CLAUDE.md do Claude Nova

```powershell
$claudeNovaMd = @'
## Auto-Context de Sessão

Ao iniciar qualquer sessão, leia as últimas 30 linhas da nota mais recente em:
`C:/Users/eduar/Foryou-Brain/Claude Nova/Sessões/Eduardo/`

Para encontrar a nota mais recente: é o arquivo `.md` com o nome mais alto em ordem alfabética (os nomes começam com data `YYYY-MM-DD HHhMM`). Ignore a pasta `_completo/`.

Se a pasta estiver vazia ou não existir, ignore silenciosamente e continue normalmente.
'@
Set-Content -Path "C:\Users\eduar\.claude-nova\CLAUDE.md" -Value $claudeNovaMd -Encoding UTF8
```

---

## ETAPA 5 — pm2: watchers em background

### 5.1 Instalar pm2

```powershell
npm install -g pm2
```

### 5.2 Registrar os watchers

```powershell
pm2 start "C:/Users/eduar/.claude/hooks/codex-watcher.js" --name codex-watcher --interpreter "C:/Program Files/nodejs/node.exe"
pm2 start "C:/Users/eduar/.claude/hooks/antigravity-watcher.js" --name antigravity-watcher --interpreter "C:/Program Files/nodejs/node.exe"
pm2 save
```

### 5.3 Verificar

```powershell
pm2 list
```

Os dois devem aparecer como `online`.

---

## ETAPA 6 — Task Scheduler: pm2 sobe no boot

### 6.1 Criar script de boot

```powershell
New-Item -Path "C:\pm2-startup" -ItemType Directory -Force
Set-Content -Path "C:\pm2-startup\pm2-resurrect.bat" -Value "@echo off`r`n`"C:\Program Files\nodejs\node.exe`" `"C:\Users\eduar\AppData\Roaming\npm\node_modules\pm2\bin\pm2`" resurrect" -Encoding ASCII
```

### 6.2 Registrar no Task Scheduler

Abrir PowerShell como **Administrador** e rodar:

```powershell
$action = New-ScheduledTaskAction -Execute "C:\pm2-startup\pm2-resurrect.bat"
$trigger = New-ScheduledTaskTrigger -AtLogOn -User "eduar"
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit 0
Register-ScheduledTask -TaskName "PM2 Auto Start" -Action $action -Trigger $trigger -Settings $settings -RunLevel Highest -Force
```

### 6.3 Verificar

```powershell
Get-ScheduledTask -TaskName "PM2 Auto Start"
```

---

## ETAPA 7 — Windows Defender: exclusões

```powershell
Add-MpPreference -ExclusionPath "C:\Users\eduar\.claude"
Add-MpPreference -ExclusionPath "C:\Users\eduar\.claude-nova"
Add-MpPreference -ExclusionPath "C:\Users\eduar\.session-saver"
Add-MpPreference -ExclusionPath "C:\Users\eduar\AppData\Roaming\npm"
Add-MpPreference -ExclusionProcess "node.exe"
Add-MpPreference -ExclusionProcess "pm2"
```

---

## ETAPA 8 — Teste final

### 8.1 Abrir Claude e testar

```powershell
claude
```

1. Digitar qualquer coisa e responder
2. Fechar com `/exit`
3. Verificar: `ls "C:\Users\eduar\Foryou-Brain\Claude 1\Sessões\Eduardo\"`

Deve aparecer uma nota `.md`.

### 8.2 Verificar sync com Wilson

1. Eduardo: Obsidian Git faz push automático em até 10 min
2. Wilson verifica no vault se a nota do Eduardo apareceu em `Claude 1/Sessões/Eduardo/`

---

## RESUMO DO QUE MUDA POR PC

| Item | Wilson | Eduardo |
|---|---|---|
| Vault path | `C:/Users/ynwwi/Projects/claude-novo/stark/Stark` | `C:/Users/eduar/Foryou-Brain` |
| Author | `Wilson` | `Eduardo` |
| Node path | `C:/Program Files/nodejs/node.exe` | `C:/Program Files/nodejs/node.exe` |
| API Key Obsidian | própria | `7b03eb07...` (já obtida) |
| MCP Tools | próprio exe | `C:\Users\eduar\Foryou-Brain\.obsidian\plugins\mcp-tools\bin\mcp-server.exe` |
