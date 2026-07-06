---
type: api-docs
project: Totus Cenografia IA
tags: [backend, api, totus, python]
---

# Backend API (FastAPI Python serverless)

## Estrutura de arquivos

`C:\Users\ynwwi\Projects\totus-cenografia-ia\api\`

```
api/
├── index.py          ← FastAPI app + todas as rotas (~700 linhas)
├── _config.py        ← Settings via os.getenv
├── _database.py      ← psycopg2 + queries Neon
├── _agent.py         ← TotusAgent (Claude + BATCH_WINDOW + extraction)
├── _persona.py       ← SYSTEM_PROMPT (37 seções)
├── _auth.py          ← JWT + bcrypt
├── _whatsapp.py      ← WhatsAppManager (Meta API + Evolution fallback)
├── _chatwoot.py      ← Chatwoot client (contact, conv, msg sync)
├── _redis.py         ← Upstash REST client (BATCH_WINDOW, locks, dedup)
├── _guardrails.py    ← Sanitize reply + slice em 5 partes
├── _anthropic.py     ← Cliente HTTP direto (substitui SDK pesado)
├── __init__.py       ← (vazio)
└── requirements.txt  ← 6 deps Python
```

## Endpoints da API (27 rotas)

### Públicos

| Método | Rota | Função |
|---|---|---|
| GET | `/api` | Root info |
| GET | `/api/health` | Health básico |
| GET | `/api/health/full` | Health detalhado (Neon, Anthropic, Redis, Chatwoot) |
| GET | `/api/welcome` | Mensagem de boas-vindas |
| GET | `/api/webhook/message` | Verify webhook Meta (handshake) |
| POST | `/api/webhook/message` | Recebe payload Meta OU formato simples |
| POST | `/api/webhook/chatwoot` | Detecta humano respondendo → desativa IA |
| GET\|POST | `/api/cron/follow-up` | Cron (validado por `CRON_SECRET`) |

### Auth

| Método | Rota | Função |
|---|---|---|
| POST | `/api/auth/login` | Retorna JWT |
| GET | `/api/auth/me` | Valida token, retorna user |

### Protegidos (exigem JWT)

| Método | Rota | Função |
|---|---|---|
| GET | `/api/conversations` | Listar conversas (filtro por status) |
| GET | `/api/conversations/{phone}` | Histórico + mensagens |
| POST | `/api/messages/send` | Enviar mensagem manual |
| GET | `/api/leads` | Listar leads (filtro level) |
| GET | `/api/leads/summary` | Contagem cold/warm/hot |
| GET | `/api/leads/{lead_id}/profile` | Profile completo com 4 tabs |
| POST | `/api/whatsapp/connect` | Iniciar sessão WhatsApp |
| GET | `/api/whatsapp/status` | Status conexão |
| POST | `/api/whatsapp/disconnect` | Desconectar |
| GET\|PUT | `/api/settings` | Configurações IA |
| GET\|POST\|PUT\|DELETE | `/api/products` | CRUD catálogo |
| GET | `/api/follow-ups` | Fila aprovação |
| POST | `/api/follow-ups/{id}/approve` | Aprovar e enviar |
| POST | `/api/follow-ups/{id}/reject` | Rejeitar (com motivo opcional) |
| GET\|PUT | `/api/brain/draft` | Rascunho da IA |
| GET | `/api/brain/current` | Versão ativa |
| GET | `/api/brain/versions` | Histórico de versões |
| POST | `/api/brain/publish` | Publicar nova versão |
| POST | `/api/brain/rollback/{id}` | Restaurar versão |
| GET | `/api/ai/status` | Status global da IA |
| POST | `/api/ai/toggle` | Liga/desliga IA global |
| POST | `/api/conversations/{phone}/automation` | Toggle IA por conversa |
| GET | `/api/dashboard/stats` | KPIs consolidados |

## Dependências Python (`api/requirements.txt`)

```
fastapi==0.115.0
psycopg2-binary==2.9.9
httpx==0.27.2
pydantic==2.9.2
bcrypt==4.2.0
PyJWT==2.9.0
```

> ⚠️ **Removidos** intencionalmente: `anthropic` (SDK pesado, substituído por `_anthropic.py` HTTP direto), `python-dotenv` (não usado em prod), `pydantic-settings`, `mangum`. Motivo: bundle estourava 250MB.

## Padrões importantes

### `_agent.process_with_batch_window`

Fluxo principal usado pelo webhook (espelho do `webhook.ts` do Rodrigo):

```python
async def process_with_batch_window(user_message, contact_phone, contact_name, message_id):
    # 1. Dedup
    if await redis.is_duplicate(message_id): return {status: duplicate}
    # 2. Rate limit
    if await redis.is_rate_limited(phone): return {status: rate_limited}
    # 3. Enfileira mensagem
    await redis.enqueue_message(phone, msg)
    # 4. Lock (NX EX 60s)
    if not await redis.acquire_lock(phone): return {status: queued}
    
    try:
        # 5. AGUARDA 10s + drena todas msgs acumuladas
        messages = await redis.drain_queue(phone)
        combined = "\n".join(messages)
        
        # 6. Sync incoming Chatwoot
        await chatwoot.sync_message(phone, name, combined, "incoming")
        
        # 7. Verifica toggles + business hours
        if not db.is_ai_active(): return ai_paused
        if db.is_conversation_automation_disabled(): return ai_paused_conv
        if not db.is_within_business_hours(): return off_hours
        
        # 8. Claude responde com 37-sec persona
        response = anthropic.messages.create(...)
        
        # 9. Guardrails: remove emojis/clichês + slice em até 5 partes
        prepared = prepare_for_sending(response.text)
        
        # 10. Detecta aprovação humana necessária
        if is_financial or is_critical:
            db.create_follow_up(...)
            return approval_pending
        
        # 11. Envia + sync Chatwoot OUT
        for part in prepared["parts"]:
            db.save_message(conv_id, "assistant", part)
            await chatwoot.sync_message(phone, name, part, "outgoing")
        
        # 12. Lead extraction + sentiment (background)
        ...
    
    finally:
        await redis.release_lock(phone)
```

### Guardrails (`_guardrails.py`)

```python
EMOJI_RE = r"[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E0-\U0001F1FF]"
CLICHE_RE = r"^\s*(perfeito|otimo|ótimo|entendo|claro|certo|com certeza|...)"

def sanitize_reply(text):
    text = EMOJI_RE.sub("", text)       # tira emojis
    text = MARKDOWN_RE.sub("", text)    # tira ** _ `
    text = BULLET_RE.sub("", text)      # tira bullets
    text = CLICHE_RE.sub("", text)      # tira "Perfeito,", "Entendo,", etc no início
    text = INTERNAL_LINK_RE.sub("", text)  # tira links localhost/supabase/vercel
    return normalized_text

def slice_into_messages(text, max_parts=5):
    # Divide por \n\n em até 5 mensagens curtas
    parts = text.split("\n\n")
    return parts[:max_parts]
```

### Redis (`_redis.py`)

Constantes (espelho do Rodrigo):
```python
PREFIX = "totus:"
BATCH_WINDOW_SEC = 10
LOCK_TTL = 60        # SET NX EX 60s
QUEUE_TTL = 180      # 3x lock para evitar expirar
DEDUP_TTL = 60       # ignora mesma msg id por 60s
RATE_WINDOW = 60
RATE_LIMIT = 10      # max 10 msgs/min/phone
```

## Como rodar local

```bash
cd C:\Users\ynwwi\Projects\totus-cenografia-ia
python -m venv venv
venv\Scripts\activate
pip install -r api/requirements.txt
# Setar env vars manualmente
$env:ANTHROPIC_API_KEY = "sk-ant-..."
$env:DATABASE_URL = "postgresql://..."
$env:UPSTASH_REDIS_REST_URL = "..."
$env:UPSTASH_REDIS_REST_TOKEN = "..."
$env:CHATWOOT_URL = "..."
$env:CHATWOOT_USER_TOKEN = "..."
$env:CHATWOOT_ACCOUNT_ID = "1"
$env:CHATWOOT_INBOX_ID = "1"
$env:JWT_SECRET = "qualquer-string-longa"

# Rodar uvicorn (FastAPI dev)
cd api
uvicorn index:app --reload --port 8000
```
