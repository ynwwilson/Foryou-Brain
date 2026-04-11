# OpenClaw Intel — 2026-03-26

> Extraído automaticamente dos grupos Telegram OpenClaw / Bruno Okamoto

## Grupo OpenClaw / Bruno Okamoto

# Insights OpenClaw — Extração de Inteligência

## 🧠 Configuração de Memória (`memorySearch`)

### Bloco completo recomendado para `openclaw.json`:
```json
"memorySearch": {
  "experimental": {
    "sessionMemory": true
  },
  "historySize": 8,
  "softMatchThreshold": 0.72,
  "hardMatchThreshold": 0.88,
  "contextRetention": "12h",
  "indexOnStart": true
}
```

### O que cada campo faz:
| Campo | Função |
|---|---|
| `sessionMemory` | Lembra contexto da sessão ativa sem indexar em disco |
| `historySize` | Janela de 8 itens recentes na busca |
| `softMatchThreshold: 0.72` | Limiar mínimo para match — evita falsos positivos |
| `hardMatchThreshold: 0.88` | Limiar para match forte/confiável |
| `contextRetention: "12h"` | Histórico expira em 12h — útil para conversas longas |
| `indexOnStart: true` | Reindexa memórias importantes ao iniciar o agente |

### Boas práticas de memória:
- Ativar `sessionMemory` **apenas em agentes que realmente precisam** — evita inflação de custo
- Rodar `openclaw memory index` sempre que atualizar `memory/pending.md` ou `memory/decisions.md`
- Usar `contextRetention` para ampliar janela histórica **sem mexer em `contextTokens`**

---

## 🏗️ Arquitetura: Agente vs. Skill

### Quando usar **Skill**:
- Padronizar processos repetíveis (ex: ritual de leitura antes de tarefas)
- Qualquer agente já treinado usa automaticamente via trigger
- Mais leve, fácil de manter

### Quando criar um **Agente dedicado**:
- Fluxo com muito estado ou lembretes recorrentes
- Monitoramento em tempo real (loop, watchdog, cron)
- Integração pesada com APIs que exige autonomia
- Execução sem trigger humano

> **Decisão padrão:** skill + script enquanto não há necessidade de execução autônoma. Agente só quando aparecer requisito de monitoramento automático.

---

## 🔧 Comandos Essenciais

### Descobrir chatId de grupos:
```bash
# Telegram
openclaw channels list --channel telegram --json \
  | jq -r '.[] | select(.name=="<nome-do-grupo>") | .chatId'

# WhatsApp
openclaw channels list --channel whatsapp --json \
  | jq -r '.[] | select(.name=="<nome-do-grupo>") | .chatId'
```

### Configurações de segurança (isolar agente de grupo):
```bash
openclaw config set channels.telegram.groupPolicy allowlist
openclaw config set channels.whatsapp.groupPolicy allowlist
openclaw config set tools.web.search.enabled false
openclaw config set tools.web.fetch.enabled false
```

### Reiniciar gateway após mudanças:
```bash
openclaw gateway restart
```

### Localizar workspace:
```bash
cd /root/.openclaw/workspace
```

---

## 📁 Estrutura de Arquivos Relevante

```
/root/.openclaw/workspace/
├── AGENTS.md                          # Instruções globais + regras fixas
├── memory/
│   ├── pending.md
│   └── decisions.md
├── references/
│   └── procedimentos/
│       └── ritual-de-leitura.md       # Checklist de execução
├── agents/
│   ├── work-group/SOUL.md             # Prompt do agente de grupo
│   └── web-assist/SOUL.md             # Prompt do sub-agente web
└── scripts/
    ├── setup-memoria-first.sh
    ├── ritual-reminder.sh
    └── get-group-id.sh
```

---

## 🤖 Padrão de SOUL para Agente de Grupo Interno

```markdown
# SOUL — Agente do Grupo Interno
Antes de responder:
1. Consulte `tools.memory.search("grupo interno", limit=3)` e leia os resultados.
2. Se não estiver claro, abra `memory/grupo-interno.md` e use de lá.
3. Só após esgotar a memória local considere a web.
4. Se recorrer à web, explique no chat por quê.
```

### Sub-agente Web (isolado):
```markdown
# SOUL — Sub-agente Web
Só use quando a memória não resolver.
Use tools.web_search ou tools.web_fetch.
Resuma a fonte e explique ao agente principal por que precisou da web.
```

---

## ⚠️ Bugs / Limitações Conhecidas

| Problema | Detalhe |
|---|---|
| **Campos não reconhecidos** | Versão `2026.3.22` não suporta alguns campos do `memorySearch` — remover campos não reconhecidos antes de aplicar |
| **Process failed** | `mild-rook` falhou silenciosamente — sempre monitorar com `openclaw logs --follow` |
| **Arquivos criados pelo bot ficam no workspace do servidor** | Usuário não tem acesso direto — precisa de SSH ou pedir conteúdo via chat |

---

## 🔄 Padrão de Ritual / Checklist de Execução

### Script `ritual-reminder.sh`:
- Limpa tela, imprime `ritual-de-leitura.md`, aguarda ENTER
- Rodar antes de qualquer tarefa complexa
- Fixar instrução no `AGENTS.md`: "execute `./scripts/ritual-reminder.sh` antes de tarefas importantes"

### Automação via alias:
```bash
alias ritual='./scripts/ritual-reminder.sh'
```
> Adicionar ao `.bashrc` do agente ou no topo do `AGENTS.md`

---

## 💡 Meta-insight

> **O bot confirma ter feito coisas que o usuário não consegue verificar.** Documentar *onde* os arquivos estão e *como acessar* é tão importante quanto criar os arquivos. Sempre perguntar: "Como acesso isso?" e registrar a resposta no `README` ou `AGENTS.md`.

---

