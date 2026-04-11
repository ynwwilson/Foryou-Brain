# Infraestrutura Borda-Nuvem Jarvis

> LEIA ESTE ARQUIVO ANTES DE TOCAR EM QUALQUER CONFIGURAÇÃO.
> Esta é a única verdade sobre como o Jarvis funciona. Não crie alternativas.

---

## Sistema oficial

O Jarvis usa **OpenClaw** como motor. Não existe sistema Python alternativo ativo. O `bot/` foi movido para `legacy/`.

---

## Arquitetura

```
Telegram → VPS Gateway (72.60.9.212:18789) → SSH Tunnel → Wilson-PC Node
```

- **VPS**: gateway OpenClaw rodando como processo permanente na porta 18789
- **PC**: node OpenClaw conecta ao gateway via SSH tunnel (porta local 18790 → VPS 18789)
- **Telegram**: gerenciado pelo gateway da VPS (token: 8312200804, allowFrom: 5340740837)

---

## Componentes ativos no PC (Wilson-PC)

| Componente | Localização | Como sobe |
|---|---|---|
| SSH Tunnel | `C:\Users\ynwwi\.openclaw\ssh-tunnel.cmd` | Scheduled Task "OpenClaw SSH Tunnel" — logon, sem delay |
| Node | `C:\Users\ynwwi\.openclaw\node-loop.cmd` | Scheduled Task "OpenClaw Node" — logon, delay 30s |

**Regra:** só estas 2 Scheduled Tasks. Qualquer outra task de tunnel ou gateway é duplicata e deve ser deletada.

---

## Configurações críticas

### exec-approvals.json (`C:\Users\ynwwi\.openclaw\exec-approvals.json`)
- `security` deve ser `"full"` — nunca `"none"` (inválido, tratado como deny) nem `"allowlist"` sem paths corretos
- `ask` deve ser `"off"`
- Este arquivo é regenerado pelo node ao iniciar — verificar após restart

### openclaw.json PC (`C:\Users\ynwwi\.openclaw\openclaw.json`)
- `telegram.enabled` = false no PC — **correto**, Telegram é gerenciado pela VPS, não pelo node
- `gateway.mode` = "local"
- Node conecta em `127.0.0.1:18790`

### openclaw.json VPS (`/root/.openclaw/openclaw.json`)
- `telegram.enabled` = true
- `channels.telegram.allowFrom` = ["5340740837"] (ID do Mestre)
- Gateway bind em `0.0.0.0:18789`

### Claude Code workspace (`.claude/settings.json`)
- Localização: `C:\Users\ynwwi\Projects\jarvis\stark\Stark\.claude\settings.json`
- Contém `Bash(*)` liberado — necessário para execução de comandos pelo agente

---

## Skills do agente (PC)

Localização: `C:\Users\ynwwi\Projects\jarvis\stark\Stark\skills\`

| Skill | Função |
|---|---|
| `computer/` | Screenshot, click, digitação via pyautogui |
| `obsidian/` | Acesso ao vault Stark |
| `cloudflare-dns/` | Gerenciamento DNS |
| `postgres/` | Banco de dados |

Uso correto dos scripts:
```bash
python skills/computer/scripts/screenshot.py
python skills/computer/scripts/click.py 960 540
```

---

## O que NÃO fazer (histórico de erros)

1. **Não criar novos scripts de tunnel** — o único é `ssh-tunnel.cmd`, gerenciado pelo OpenClaw
2. **Não criar Scheduled Tasks de gateway no PC** — gateway só roda na VPS
3. **Não usar `security: "none"` no exec-approvals** — é inválido
4. **Não rodar `bot/main.py` ou `bot/main_new.py`** — conflito 409 com o token Telegram do OpenClaw
5. **Não rodar `openclaw configure` sem necessidade** — reseta configurações e desativa Telegram no PC
6. **Não iniciar múltiplos processos node** — o node-loop.cmd já gerencia restart automático

---

## Diagnóstico rápido

Se Jarvis não responde:
1. Verificar tunnel: `netstat -ano | findstr 18790` — deve ter LISTENING
2. Verificar node: buscar processo `entry.js node` rodando
3. Verificar VPS: `ss -tn | grep 18789` — deve ter ESTAB
4. exec-approvals: confirmar `security: "full"`

Se tunnel não sobe:
```
Start-ScheduledTask "OpenClaw SSH Tunnel"
# aguardar 35s
Start-ScheduledTask "OpenClaw Node"
```
