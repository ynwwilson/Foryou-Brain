# HEARTBEAT.md — Checagem Periódica

> Rode a cada 4h durante horários ativos (6h-3h). Direto ao ponto.

## O que checar (nesta ordem)

### 1. Projetos Críticos (2 min)
- **Rainha da Aprovação** — em produção. Tem erros no Lovable Cloud? Alguém reclamou?
- **IA de Atendimento do Rodrigo** — em construção. Bloqueado em algo? Precisa de input?
- **Smartcell** — e-commerce Patos-PB. Progression ou parado?

Checar `memory/projects.md` e detalhes em `memory/projects/`. Se status é "bloqueado" ou "aguardando", avisar.

### 2. Pendências Abertas (1 min)
Ler `memory/pending.md`. Se tem algo marcado 🔴 (urgente), reportar direto.

### 3. Agenda do Dia (1 min)
Checar Google Calendar:
```
gog calendar events ynwwilson@gmail.com --from TODAY --to TOMORROW
```
- Compromissos próximos (próximas 4h)?
- Algo conflitando com ritmo de trabalho (reunião durante madrugada)?

### 4. Saúde do Stack (1 min)
- OpenClaw gateway rodando? (`openclaw gateway status`)
- Google Calendar integrado? (`gog auth list`)
- Crons executando? (`openclaw cron list` — algum com erro?)

### 5. Context Switch Alert (30s)
Se está em período produtivo (morning/afternoon/night) e tem muitas abas abertas em browsers, avisar que pode quebrar foco.

---

## Quando NÃO enviar nada
- Está fora dos horários configurados (12:00-13:30, 17:30-20:30, 03:00-06:00)
- Tudo ok + sem pendências + sem agenda urgente = responda `HEARTBEAT_OK`
- Não encha o Telegram com avisos pequenos — compile tudo em 1 msg

---

## Como formatar a resposta
Se tiver algo:
```
⚡ Stark — Heartbeat 4h

🔴 URGENTE: [coisa]
🟡 Aberto: [coisa]
📅 Agenda próximas 4h: [horários]
🔧 Sistema: [status]
```

Se não tiver nada relevante:
```
HEARTBEAT_OK
```

---

## Validação Antes de Enviar (Immune System)

Antes de qualquer ação que saia do workspace (message, email, API write):

- [ ] Revisar conteúdo — sem dados sensíveis, IDs, credenciais
- [ ] Checar URLs — válidas e seguras
- [ ] Validar destinatários — é realmente quem você quer?
- [ ] Confirmar contexto — faz sentido mandar agora?
- [ ] Se é ação crítica → tripla confirmação (vide AGENTS.md Red Lines)
