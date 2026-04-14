---
date: 2026-04-14
tags: [roadmap, sistema, eduardo, setup]
---

# Roadmap — Replicar Setup Completo no PC do Eduardo

> Base: setup Wilson funcionando 100% em 2026-04-14.
> Vault Eduardo: `C:\Users\eduar\Foryou-Brain`
> Ferramentas: Claude 1, Claude Nova (Codex e Antigravity quando instalar)

---

## PRÉ-REQUISITOS — verificar antes de começar

No terminal do Eduardo, confirmar que tem:

```powershell
node --version    # precisa ser v18+
npm --version
git --version
```

Se Node não estiver instalado: https://nodejs.org (baixar LTS)

---

## ETAPA 1 — Obsidian: plugins e configurações

O vault já está clonado em `C:\Users\eduar\Foryou-Brain`.

### 1.1 Ativar plugins

`Settings → Community Plugins → Turn on community plugins` (se ainda não estiver ligado)

Em `Installed plugins`, ativar **todos**:

| Plugin | Função |
|--------|--------|
| obsidian-git | Sync automático com GitHub |
| Local REST API | Conexão com Claude via MCP |
| Dataview | Queries nas notas |
| Smart Connections | Busca semântica |
| MCP Tools | Servidor MCP interno |
| Style Settings | Estilos customizados |
| Icon Folder | Ícones nas pastas |
| Banners | Banners nas notas |
| Open in Terminal | Abrir terminal na pasta |

### 1.2 Configurar obsidian-git

`Settings → Obsidian Git`:

| Configuração | Valor |
|---|---|
| Auto save interval | 10 min |
| Auto push interval | 5 min |
| Auto pull interval | 5 min |
| Pull on startup | ✅ ativado |
| Pull before push | ✅ ativado |
| Commit message | `vault: auto-sync {{date}}` |
| Date format | `YYYY-MM-DD HH:mm:ss` |
| Sync method | Merge |

### 1.3 Pegar a API Key do Local REST API

`Settings → Local REST API` → copiar o valor de **API Key**

Vai precisar dela na Etapa 4 (MCP do Claude).

---

## ETAPA 2 — Session Saver: criar arquivos

### 2.1 Criar pasta dos hooks

```powershell
mkdir C:\Users\eduar\.claude\hooks
mkdir C:\Users\eduar\.session-saver\cache
```

### 2.2 Criar config.json

Criar arquivo `C:\Users\eduar\.session-saver\config.json`:

```json
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
```

> **Atenção:** confirmar o caminho do Node com `where node` antes de usar.

### 2.3 Copiar os hooks

Copiar os 3 arquivos do PC do Wilson para `C:\Users\eduar\.claude\hooks\`:

- `session-saver.js`
- `codex-watcher.js`
- `antigravity-watcher.js`

Esses arquivos leem o `config.json`, então nada dentro deles precisa ser alterado.

### 2.4 Criar package.json e instalar dependências

Criar `C:\Users\eduar\.claude\hooks\package.json`:

```json
{
  "name": "session-saver-hooks",
  "version": "1.0.0",
  "description": "Claude Code hooks + session watchers",
  "main": "session-saver.js",
  "dependencies": {
    "chokidar": "^3.6.0"
  }
}
```

Instalar:

```powershell
cd C:\Users\eduar\.claude\hooks
npm install
```

---

## ETAPA 3 — Claude Code: configurar hooks

### 3.1 Descobrir caminho do Node

```powershell
where node
```

Vai retornar algo como `C:\Program Files\nodejs\node.exe`. Usar esse caminho nos próximos arquivos.

### 3.2 Criar settings.json do Claude 1

Criar `C:\Users\eduar\.claude\settings.json`:

```json
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
  }
}
```

### 3.3 Criar pasta e settings.json do Claude Nova

```powershell
mkdir C:\Users\eduar\.claude-nova
```

Criar `C:\Users\eduar\.claude-nova\settings.json` com o mesmo conteúdo do 3.2 acima.

### 3.4 Criar CLAUDE.md do Claude 1

Criar `C:\Users\eduar\.claude\CLAUDE.md`:

```markdown
## Auto-Context de Sessão

Ao iniciar qualquer sessão, leia as últimas 30 linhas da nota mais recente em:
`C:/Users/eduar/Foryou-Brain/Claude 1/Sessões/Eduardo/`

Para encontrar a nota mais recente: é o arquivo `.md` com o nome mais alto em ordem alfabética (os nomes começam com data `YYYY-MM-DD HHhMM`). Ignore a pasta `_completo/`.

Se a pasta estiver vazia ou não existir, ignore silenciosamente e continue normalmente.
```

### 3.5 Criar CLAUDE.md do Claude Nova

Criar `C:\Users\eduar\.claude-nova\CLAUDE.md` com o mesmo conteúdo, trocando apenas:
- `Claude 1/Sessões/Eduardo/` → `Claude Nova/Sessões/Eduardo/`

---

## ETAPA 4 — MCP Servers (Claude se conectar ao Obsidian)

Adicionar ao `C:\Users\eduar\.claude\settings.json` dentro de `"hooks": {...}`, no mesmo nível:

```json
"mcpServers": {
  "obsidian": {
    "command": "C:\\Users\\eduar\\Foryou-Brain\\.obsidian\\plugins\\mcp-tools\\bin\\mcp-server.exe",
    "args": [],
    "env": {
      "OBSIDIAN_API_KEY": "COLAR_A_KEY_DO_PASSO_1.3_AQUI"
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
```

> Substituir `COLAR_A_KEY_DO_PASSO_1.3_AQUI` pela API Key copiada no passo 1.3.

Fazer o mesmo no `C:\Users\eduar\.claude-nova\settings.json`.

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

Criar `C:\pm2-startup\pm2-resurrect.bat`:

```bat
@echo off
"C:\Program Files\nodejs\node.exe" "C:\Users\eduar\AppData\Roaming\npm\node_modules\pm2\bin\pm2" resurrect
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

Deve retornar `Ready`.

---

## ETAPA 7 — Windows Defender: exclusões

Para o pm2 e hooks não serem bloqueados:

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

### 8.1 Testar session-saver manualmente

```powershell
echo '{"transcript_path":"C:/Users/eduar/.claude/projects/teste/test.jsonl","session_id":"test-123","cwd":"C:/Users/eduar"}' | node "C:/Users/eduar/.claude/hooks/session-saver.js"
```

Não deve retornar erro.

### 8.2 Abrir Claude e testar

1. Abrir Claude 1 no terminal: `claude`
2. Digitar qualquer coisa e responder
3. Fechar com `/exit`
4. Verificar se apareceu nota em `C:\Users\eduar\Foryou-Brain\Claude 1\Sessões\Eduardo\`

### 8.3 Verificar sync com Wilson

1. Eduardo faz pull no Obsidian: `Ctrl+P → Obsidian Git: Pull`
2. Wilson verifica no vault se a nota do Eduardo apareceu

---

## RESUMO DO QUE MUDA POR PC

| Item | Wilson | Eduardo |
|---|---|---|
| Vault path | `C:/Users/ynwwi/Projects/claude-novo/stark/Stark` | `C:/Users/eduar/Foryou-Brain` |
| Author | `Wilson` | `Eduardo` |
| Node path | `C:/Program Files/nodejs/node.exe` | confirmar com `where node` |
| API Key Obsidian | própria | própria (passo 1.3) |

Tudo mais é idêntico.

---

## QUANDO INSTALAR CODEX E ANTIGRAVITY

Os watchers já estão configurados no pm2. Quando Eduardo instalar:

- **Codex:** sessões em `C:/Users/eduar/.codex/sessions` — watcher detecta automaticamente
- **Antigravity:** brain em `C:/Users/eduar/.gemini/antigravity/brain` — watcher detecta automaticamente

Nenhuma configuração adicional necessária.
