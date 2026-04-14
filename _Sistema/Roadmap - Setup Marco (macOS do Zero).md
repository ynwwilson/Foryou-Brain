---
date: 2026-04-14
tags: [roadmap, sistema, marco, setup, macos]
---

# Roadmap — Setup Completo Marco (macOS do Zero)

> Username: `marcoant` · Vault: `/Users/marcoant/Foryou-Brain`
> Base: setup Wilson funcionando 100% em 2026-04-14.

---

## PRÉ-REQUISITOS — verificar antes de começar

```bash
xcode-select --version   # se não tiver: xcode-select --install
brew --version           # se não tiver: instalar Homebrew abaixo
node --version           # precisa ser v18+
git --version
```

### Instalar Homebrew (se não tiver)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Após instalar, adicionar ao PATH (MacBook Air com Apple Silicon):

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
source ~/.zshrc
```

### Instalar Node.js (se não tiver)

```bash
brew install node
node --version   # confirmar v18+
```

---

## ETAPA 1 — Git: clonar o vault

```bash
cd ~
git clone https://github.com/ynwwilson/Foryou-Brain.git
```

Vault ficará em `/Users/marcoant/Foryou-Brain`.

### Configurar credenciais git

```bash
git config --global user.name "Marco"
git config --global user.email "SEU_EMAIL_AQUI"
git config --global credential.helper osxkeychain
```

Testar autenticação:

```bash
cd ~/Foryou-Brain
git pull
```

Se pedir login: usar usuário e **Personal Access Token** do GitHub (não senha).
Gerar token em: GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic) → Generate → marcar `repo`.

---

## ETAPA 2 — Obsidian: abrir vault e ativar plugins

1. Abrir Obsidian
2. `Open folder as vault` → selecionar `/Users/marcoant/Foryou-Brain`
3. Quando perguntar sobre plugins: **Trust and enable**

### 2.1 Ativar plugins

`Settings → Community Plugins → Turn on community plugins`

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

### 2.2 Configurar obsidian-git

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

### 2.3 Pegar a API Key do Local REST API

`Settings → Local REST API` → copiar o valor de **API Key**

Guardar — vai usar na Etapa 5.

---

## ETAPA 3 — Claude Code: instalar e resolver OAuth

### 3.1 Instalar

```bash
npm install -g @anthropic-ai/claude-code
```

### 3.2 Resolver o problema do OAuth (não pedir API key)

O problema anterior era o Claude abrindo direto para API key em vez do browser. Resolver assim:

```bash
# Limpar qualquer config anterior
rm -rf ~/.claude

# Rodar claude pela primeira vez — vai abrir o browser para login
claude
```

Se ainda abrir pedindo API key em vez do browser:

```bash
claude auth login
```

Isso força o fluxo OAuth pelo browser. Logar com a conta Claude Pro do Marco.

### 3.3 Instalar Claude Nova (segunda conta)

```bash
# Claude Nova usa pasta separada
mkdir -p ~/.claude-nova

# Instalar em pasta separada não é necessário — é a mesma CLI
# A separação é feita via configuração, não instalação
```

> Claude Nova é a mesma CLI (`claude`), rodando com configs em `~/.claude-nova/`.
> Para usar Claude Nova: `claude --config-dir ~/.claude-nova`

---

## ETAPA 4 — Session Saver: criar arquivos

### 4.1 Criar pastas

```bash
mkdir -p ~/.claude/hooks
mkdir -p ~/.session-saver/cache
mkdir -p ~/.claude-nova
```

### 4.2 Criar config.json

Criar `/Users/marcoant/.session-saver/config.json`:

```json
{
  "vaultPath": "/Users/marcoant/Foryou-Brain",
  "author": "Marco",
  "tools": {
    "claude1":       { "folder": "Claude 1",    "name": "Claude"      },
    "claude-nova":   { "folder": "Claude Nova", "name": "Claude Nova" },
    "codex":         { "folder": "Codex",       "name": "Codex"       },
    "antigravity":   { "folder": "Antigravity", "name": "Antigravity" }
  },
  "codexSessionsPath": "/Users/marcoant/.codex/sessions",
  "antigravityBrainPath": "/Users/marcoant/.gemini/antigravity/brain",
  "heartbeatMaxAge": 120000,
  "maxTextLength": 800,
  "maxExchanges": 15,
  "catchUpDays": 7,
  "nodePath": "/opt/homebrew/bin/node"
}
```

> Confirmar o caminho do Node com `which node` antes de usar.

### 4.3 Copiar os hooks

Copiar do PC do Wilson (ou do vault `_Sistema/Scripts/` se estiver salvo lá) para `~/.claude/hooks/`:

- `session-saver.js`
- `codex-watcher.js`
- `antigravity-watcher.js`
- `package.json`

```bash
# Ou copiar direto do vault já clonado (se os scripts estiverem lá)
cp ~/Foryou-Brain/_Sistema/Scripts/session-saver.js ~/.claude/hooks/
cp ~/Foryou-Brain/_Sistema/Scripts/codex-watcher.js ~/.claude/hooks/
cp ~/Foryou-Brain/_Sistema/Scripts/antigravity-watcher.js ~/.claude/hooks/
cp ~/Foryou-Brain/_Sistema/Scripts/package.json ~/.claude/hooks/
```

### 4.4 Instalar dependências

```bash
cd ~/.claude/hooks
npm install
```

---

## ETAPA 5 — Claude Code: configurar hooks e MCP

### 5.1 Descobrir caminho do Node

```bash
which node
# Retorna algo como /opt/homebrew/bin/node
```

### 5.2 Criar settings.json do Claude 1

Criar `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/opt/homebrew/bin/node /Users/marcoant/.claude/hooks/session-saver.js"
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
            "command": "/opt/homebrew/bin/node /Users/marcoant/.claude/hooks/session-saver.js"
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
      "command": "/Users/marcoant/Foryou-Brain/.obsidian/plugins/mcp-tools/bin/mcp-server",
      "args": [],
      "env": {
        "OBSIDIAN_API_KEY": "COLAR_A_KEY_DO_PASSO_2.3_AQUI"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/marcoant/Foryou-Brain"
      ]
    }
  }
}
```

### 5.3 Criar settings.json do Claude Nova

Criar `~/.claude-nova/settings.json` com o mesmo conteúdo acima.

### 5.4 Criar CLAUDE.md do Claude 1

Criar `~/.claude/CLAUDE.md`:

```markdown
## Auto-Context de Sessão

Ao iniciar qualquer sessão, leia as últimas 30 linhas da nota mais recente em:
`/Users/marcoant/Foryou-Brain/Claude 1/Sessões/Marco/`

Para encontrar a nota mais recente: é o arquivo `.md` com o nome mais alto em ordem alfabética (os nomes começam com data `YYYY-MM-DD HHhMM`). Ignore a pasta `_completo/`.

Se a pasta estiver vazia ou não existir, ignore silenciosamente e continue normalmente.
```

### 5.5 Criar CLAUDE.md do Claude Nova

Criar `~/.claude-nova/CLAUDE.md` com o mesmo conteúdo, trocando:
- `Claude 1/Sessões/Marco/` → `Claude Nova/Sessões/Marco/`

---

## ETAPA 6 — pm2: watchers em background

### 6.1 Instalar pm2

```bash
npm install -g pm2
```

### 6.2 Registrar os watchers

```bash
pm2 start ~/.claude/hooks/codex-watcher.js --name codex-watcher --interpreter $(which node)
pm2 start ~/.claude/hooks/antigravity-watcher.js --name antigravity-watcher --interpreter $(which node)
pm2 save
```

### 6.3 Verificar

```bash
pm2 list
```

Os dois devem aparecer como `online`.

---

## ETAPA 7 — LaunchAgent: pm2 sobe no boot (macOS)

No Mac não existe Task Scheduler — usa-se LaunchAgent.

### 7.1 Descobrir caminho do pm2

```bash
which pm2
# Ex: /opt/homebrew/bin/pm2
```

### 7.2 Criar o plist

Criar `~/Library/LaunchAgents/com.foryou.pm2.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.foryou.pm2</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/node</string>
        <string>/opt/homebrew/lib/node_modules/pm2/bin/pm2</string>
        <string>resurrect</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/pm2-startup.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/pm2-startup-err.log</string>
</dict>
</plist>
```

> Ajustar o caminho do pm2 se `which pm2` retornar diferente de `/opt/homebrew/lib/node_modules/pm2/bin/pm2`.
> Verificar com: `ls /opt/homebrew/lib/node_modules/pm2/bin/pm2`

### 7.3 Ativar o LaunchAgent

```bash
launchctl load ~/Library/LaunchAgents/com.foryou.pm2.plist
```

### 7.4 Verificar

```bash
launchctl list | grep foryou
```

Deve retornar uma linha com `com.foryou.pm2`.

---

## ETAPA 8 — Auto-sync do vault (git pull automático)

O Obsidian Git já faz pull a cada 5 min quando o Obsidian está aberto.

Para pull automático mesmo com Obsidian fechado, criar um segundo LaunchAgent:

Criar `~/Library/LaunchAgents/com.foryou.vaultsync.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.foryou.vaultsync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/git</string>
        <string>-C</string>
        <string>/Users/marcoant/Foryou-Brain</string>
        <string>pull</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/vaultsync.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/vaultsync-err.log</string>
</dict>
</plist>
```

```bash
launchctl load ~/Library/LaunchAgents/com.foryou.vaultsync.plist
```

---

## ETAPA 9 — Teste final

### 9.1 Testar session-saver

```bash
echo '{"transcript_path":"/Users/marcoant/.claude/projects/teste/test.jsonl","session_id":"test-123","cwd":"/Users/marcoant"}' | node ~/.claude/hooks/session-saver.js
```

Não deve retornar erro.

### 9.2 Abrir Claude e testar

```bash
claude
```

1. Digitar qualquer coisa
2. Fechar com `/exit`
3. Verificar: `ls ~/Foryou-Brain/Claude\ 1/Sessões/Marco/`

Deve aparecer uma nota `.md`.

### 9.3 Verificar sync com Wilson

1. Marco: `git push` (ou Obsidian Git vai fazer automaticamente)
2. Wilson verifica no vault se a nota do Marco apareceu

---

## RESUMO COMPARATIVO

| Item | Wilson (Windows) | Eduardo (Windows) | Marco (macOS) |
|---|---|---|---|
| Vault | `C:/Users/ynwwi/Projects/claude-novo/stark/Stark` | `C:/Users/eduar/Foryou-Brain` | `/Users/marcoant/Foryou-Brain` |
| Author | `Wilson` | `Eduardo` | `Marco` |
| Node path | `C:/Program Files/nodejs/node.exe` | confirmar `where node` | `/opt/homebrew/bin/node` |
| Boot automático | Task Scheduler | Task Scheduler | LaunchAgent |
| Auto-sync vault | Task Scheduler | Task Scheduler | LaunchAgent |

---

## QUANDO INSTALAR CODEX E ANTIGRAVITY

Watchers já configurados. Quando Marco instalar:

- **Codex:** sessões em `/Users/marcoant/.codex/sessions` — detecta automaticamente
- **Antigravity:** brain em `/Users/marcoant/.gemini/antigravity/brain` — detecta automaticamente

Nenhuma configuração adicional necessária.
