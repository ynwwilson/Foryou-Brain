# 📘 Manual Completo: IA de Atendimento (Totus AI)
**Guia para Replicar e Adaptar a IA do Rodrigo para Outras Empresas**

---

## 🎯 Visão Geral

A **Totus AI** é uma IA de atendimento via WhatsApp que:
- Recebe mensagens de clientes via WhatsApp
- Processa com Claude (Anthropic)
- Armazena histórico e leads em Supabase
- Responde automaticamente com tom e personalidade configuráveis
- Integra-se com Evolution API para gerenciar WhatsApp

**Stack Tecnológico:**
- **IA**: Claude Sonnet 4.6 (Anthropic API)
- **Backend**: Python + FastAPI
- **WhatsApp**: Evolution API (gerenciamento de instância)
- **Banco de Dados**: Supabase (PostgreSQL)
- **Frontend**: React + Lovable + TypeScript
- **Deploy**: Vercel (backend + frontend)

---

## 📊 Arquitetura de Alto Nível

```
┌─────────────────┐
│   Cliente WhatsApp
│   (via celular)
└────────┬────────┘
         │ mensagem
         ▼
┌─────────────────────────────────┐
│   Evolution API                 │
│   (gerencia WhatsApp)           │
└────────┬────────────────────────┘
         │ webhook POST
         ▼
┌──────────────────────────────────────────┐
│   Backend FastAPI                        │
│   - webhook/evolution (recebe eventos)   │
│   - /api/whatsapp/* (gerencia)           │
│   - agent.reply() (processa com Claude)  │
└────────┬─────────────────────────────────┘
         │ salva histórico + gera resposta
         ▼
┌──────────────────┐
│   Supabase DB    │
│   (histórico)    │
└──────────────────┘
         ▲
         │ fetch/insert
         │
┌──────────────────┐
│   Claude API     │
│   (processamento)│
└──────────────────┘
         ▲
         │ response
         │
└────────┬─────────────────────────────────┘
         │ send_text() via Evolution
         ▼
    Cliente WhatsApp
```

---

## 🔑 Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto `backend/` com:

```env
# Anthropic Claude API
ANTHROPIC_API_KEY=sk-ant-v0-XXXXXXXXXXXX

# Supabase (PostgreSQL)
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_SERVICE_KEY=eyJ0eXAiOiJKV1QiLCJhbGc...

# Evolution API (WhatsApp)
EVOLUTION_API_URL=http://72.60.9.212:8080
EVOLUTION_API_KEY=your-evolution-api-key
EVOLUTION_INSTANCE=totus  # nome da instância WhatsApp

# Webhook Secret (opcional)
WEBHOOK_SECRET=

# URL pública do backend (para auto-configuração do webhook)
BACKEND_URL=https://seu-backend.vercel.app

# Porta local (desenvolvimento)
PORT=8000
```

### 🔐 Onde Obter Cada Variável

| Variável | Onde Obter | Exemplo |
|----------|-----------|---------|
| `ANTHROPIC_API_KEY` | console.anthropic.com → API Keys | `sk-ant-v0-...` |
| `SUPABASE_URL` | Supabase Project → Settings → API | `https://abc123.supabase.co` |
| `SUPABASE_SERVICE_KEY` | Supabase Project → Settings → API (Service Role) | `eyJ0eXAiOiJKV1Q...` |
| `EVOLUTION_API_URL` | Servidor Evolution API ou fornecedor | `http://72.60.9.212:8080` |
| `EVOLUTION_API_KEY` | Configuração da Evolution API | Fornecido pelo servidor |
| `EVOLUTION_INSTANCE` | Qualquer nome que você quiser | `nomeda-empresa` |
| `BACKEND_URL` | URL do seu backend deployado no Vercel | `https://seu-projeto.vercel.app` |

---

## 🗄️ Estrutura do Banco de Dados (Supabase)

### Tabela: `conversations`
Armazena conversas com clientes.

```sql
CREATE TABLE conversations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  contact_phone TEXT UNIQUE NOT NULL,
  contact_name TEXT,
  lead_status TEXT DEFAULT 'novo',  -- novo, qualificado, convertido, descartado
  last_message_at TIMESTAMP DEFAULT now(),
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);
```

**Campos:**
- `id`: identificador único
- `contact_phone`: número WhatsApp (ex: "5585987654321")
- `contact_name`: nome do cliente
- `lead_status`: estágio do lead
- `last_message_at`: quando foi a última mensagem

---

### Tabela: `messages`
Armazena mensagens enviadas e recebidas.

```sql
CREATE TABLE messages (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
  sender TEXT NOT NULL,  -- "user" | "ai"
  content TEXT NOT NULL,
  media_url TEXT,  -- URL de mídia se houver
  created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_messages_conversation ON messages(conversation_id);
```

**Campos:**
- `id`: identificador único
- `conversation_id`: qual conversa essa mensagem pertence
- `sender`: quem enviou ("user" para cliente, "ai" para IA)
- `content`: texto da mensagem
- `media_url`: URL de imagem/vídeo (opcional)

---

### Tabela: `leads`
Extrai informações qualificadas dos clientes.

```sql
CREATE TABLE leads (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  phone TEXT UNIQUE NOT NULL,
  name TEXT,
  event_type TEXT,  -- casamento, corporativo, formatura, etc
  event_date TEXT,
  location TEXT,
  estimated_guests INTEGER,
  budget DECIMAL(10,2),
  reference_style TEXT,
  source TEXT DEFAULT 'whatsapp',
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);
```

**Campos:**
- `phone`: número único do cliente
- `name`: nome
- `event_type`: tipo de evento
- `event_date`: data estimada do evento
- `location`: local
- `estimated_guests`: quantas pessoas
- `budget`: orçamento (opcional)

---

### Tabela: `ai_settings`
Configurações personalizáveis da IA (painel de controle).

```sql
CREATE TABLE ai_settings (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  ai_name TEXT,  -- nome que a IA usa pra se apresentar
  tone_of_voice TEXT,  -- descrição do tom desejado
  custom_instructions TEXT,  -- instruções adicionais
  welcome_message TEXT,  -- mensagem de boas-vindas customizada
  business_description TEXT,  -- sobre a empresa
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);
```

---

### Tabela: `whatsapp_instance`
Status da conexão WhatsApp e QR code.

```sql
CREATE TABLE whatsapp_instance (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  instance_name TEXT UNIQUE NOT NULL,  -- nome da instância
  status TEXT DEFAULT 'disconnected',  -- connecting, connected, disconnected
  phone TEXT,  -- número conectado
  profile_name TEXT,  -- nome do perfil
  qr_code TEXT,  -- QR code base64 para conexão
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);
```

---

## 🧠 Persona & System Prompt

### Arquivo: `backend/persona.py`

Define a personalidade da IA. Customize para cada empresa:

```python
SYSTEM_PROMPT = """Você é a assistente virtual da [NOME DA EMPRESA].

## Sobre [NOME DA EMPRESA]
[DESCRIÇÃO DETALHADA DO NEGÓCIO]

## Sua personalidade
- Tom: [caloroso, profissional, criativo, etc]
- Idioma: português brasileiro
- Você representa uma empresa [premium/descontraída/etc] — transmita [confiança/diversão/etc]
- Seja consultiva: entenda a necessidade antes de oferecer solução

## Suas responsabilidades
1. **Atendimento inicial**: recepcionar o cliente, entender a necessidade
2. **Qualificação**: descobrir [dados relevantes para o negócio]
3. **Dúvidas frequentes**: responder sobre [serviços específicos]
4. **Encaminhamento**: quando necessário, passar para equipe comercial

## Fluxo de qualificação (faça naturalmente)
- Nome do cliente
- [Dado específico 1]
- [Dado específico 2]
- [Dado específico 3]

## Regras importantes
- Nunca confirme vendas — sempre direcione para equipe comercial
- Se não souber, diga: "Vou verificar com nossa equipe e te retorno!"
- Nunca invente preços ou prazos
- Mensagens curtas e diretas — WhatsApp não é e-mail
- Use emojis com moderação (1-2 por mensagem)
"""
```

---

## 🚀 Como Replicar para Outra Empresa

### Passo 1: Setup Inicial

```bash
# 1. Clone ou crie novo projeto
git clone <seu-repositório> ou
cd meu-novo-projeto-ia

# 2. Setup do backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Setup do frontend
cd ../
npm install
```

### Passo 2: Criar Conta Anthropic

1. Acesse [console.anthropic.com](https://console.anthropic.com)
2. Crie conta (use seu email)
3. Vá em **Settings → API Keys**
4. Clique **Create Key**
5. Copie e guarde com segurança (não é mostrada novamente)

**Custo**: ~$0.003 por 1K tokens de entrada, $0.015 por 1K de saída.

### Passo 3: Criar Projeto Supabase

1. Acesse [supabase.com](https://supabase.com)
2. Clique **New Project**
3. Selecione region (ex: São Paulo)
4. Defina senha (guarde!)
5. Aguarde criação (~1 min)
6. Vá em **Settings → Database**
7. Copie `Connection String` (URL e Service Role Key)

**Passo importante**: Role a página até encontrar a seção de Service Key — copie a service role key (não é a password).

### Passo 4: Criar Tabelas no Supabase

No Supabase, vá em **SQL Editor** e execute os scripts acima (conversations, messages, leads, ai_settings, whatsapp_instance).

### Passo 5: Configurar Evolution API

A Evolution API gerencia a instância WhatsApp sem usar Business API (mais simples).

**Opções:**
1. **Servidor próprio**: Deploy Evolution API em seu VPS
   - Documentação: [evolution-api.com](https://evolution-api.com)
   - Custo: manutenção do servidor

2. **Fornecedor terceiro**: Use um provedor que hospeda Evolution API
   - Exemplo: [Z-API](https://z-api.io) ou similar
   - Custo: R$ 50-200/mês dependendo volume

### Passo 6: Conectar WhatsApp

1. Com o backend rodando, acesse seu painel (frontend)
2. Clique **Conectar WhatsApp**
3. Escaneie o QR code com celular
4. Aguarde conexão (leva ~5-10 seg)
5. Número aparecerá como "Conectado"

⚠️ **Importante**: Use um número dedicado para o bot (não use seu pessoal).

### Passo 7: Customizar a Persona

1. Edite `backend/persona.py`
2. Mude `SYSTEM_PROMPT` com:
   - Nome da empresa
   - Descrição do negócio
   - Tom de voz
   - Fluxo de qualificação
3. Rode backend para aplicar

3. Também preencha `ai_settings` no Supabase com:
   - `ai_name`: nome que a IA usa
   - `tone_of_voice`: descrição do tom
   - `custom_instructions`: instruções adicionais
   - `welcome_message`: saudação customizada

### Passo 8: Deploy no Vercel

```bash
# 1. Push para GitHub
git add .
git commit -m "Initial commit"
git push origin main

# 2. No Vercel, clique New Project
# 3. Selecione seu repo do GitHub
# 4. Configure variáveis de ambiente (mesmo do .env)
# 5. Deploy automático!
```

---

## 🔧 Fluxo de Funcionamento (Passo a Passo)

### O que acontece quando um cliente envia mensagem via WhatsApp:

```
1. Cliente envia mensagem pelo WhatsApp
   ↓
2. Evolution API recebe a mensagem
   ↓
3. Evolution API faz POST em BACKEND_URL/webhook/evolution com o evento
   ↓
4. Backend extrai:
   - Número do cliente (phone)
   - Texto da mensagem
   - Se houver imagem, baixa dela
   ↓
5. Backend chama agent.reply():
   a) Busca conversa anterior (se existir) no Supabase
   b) Busca últimas 20 mensagens do histórico
   c) Busca ai_settings (tom, nome, instruções)
   d) Monta system prompt com base em ai_settings
   e) Chama Claude Sonnet 4.6 com mensagens + system prompt
   f) Claude retorna resposta
   g) Salva resposta no Supabase (tabela messages)
   h) Extrai info de lead automaticamente (se encontrar "nome", "tipo evento", etc)
   ↓
6. Backend envia resposta via Evolution API:
   whatsapp.send_text(phone, response_text)
   ↓
7. Cliente recebe resposta no WhatsApp
```

---

## 💻 Código-Chave Explicado

### Agent: `backend/agent.py`

**`reply()` — a função principal**

```python
async def reply(
    phone: str,
    contact_name: str | None,
    user_text: str,
    image_bytes: bytes | None = None,
    image_mime: str = "image/jpeg",
) -> str:
    # 1. Busca conversa anterior ou cria nova
    conv = db.get_or_create_conversation(phone, contact_name)
    
    # 2. Busca histórico de 20 mensagens
    history = db.get_messages(conv["id"], limit=20)
    
    # 3. Se houver imagem, adiciona ela ao conteúdo
    if image_bytes:
        user_content = [
            {"type": "image", "source": {...}},
            {"type": "text", "text": user_text}
        ]
    else:
        user_content = user_text
    
    # 4. Monta system prompt com customizações
    system_prompt = _build_system_prompt()
    
    # 5. Chama Claude
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=messages
    )
    
    # 6. Salva resposta no BD
    db.save_message(conv["id"], "ai", response_text)
    
    # 7. Extrai info de lead silenciosamente
    _extract_lead_info(user_text, phone)
    
    return response_text
```

**`_extract_lead_info()` — extrai dados do cliente**

```python
def _extract_lead_info(text: str, phone: str) -> None:
    fields = {}
    lower = text.lower()
    
    # Busca padrões simples
    if "meu nome é" in lower:
        name = extract_name_logic(lower)
        fields["name"] = name
    
    if "casamento" in lower:
        fields["event_type"] = "casamento"
    elif "corporativo" in lower:
        fields["event_type"] = "corporativo"
    # ... etc
    
    # Salva no BD se encontrou algo
    if fields:
        db.upsert_lead(phone, **fields)
```

### WhatsApp: `backend/whatsapp_manager.py`

**`connect()` — gera QR code**

```python
def connect() -> dict:
    # Garante que a instância existe
    ensure_instance()
    
    # Configura webhook automaticamente
    _configure_webhook()
    
    # Faz request pra Evolution API
    res = client.get(
        f"{BASE_URL}/instance/connect/{INSTANCE}",
        headers=_headers()
    )
    
    qr_base64 = res.json()["base64"]
    return {"qr": qr_base64, "status": "connecting"}
```

**`handle_connection_event()` — callback quando status muda**

```python
def handle_connection_event(data: dict) -> None:
    state = data.get("state", "")
    
    if state == "open":
        # Conectado! Salva telefone no BD
        phone = data.get("wuid", "").split(":")[0]
        db.update_whatsapp_instance(
            status="connected",
            phone=phone
        )
    elif state in ("close", "refused"):
        # Desconectado
        db.update_whatsapp_instance(status="disconnected")
```

### Banco: `backend/supabase_client.py`

**`get_or_create_conversation()` — busca ou cria conversa**

```python
def get_or_create_conversation(phone: str, name: str | None = None) -> dict:
    # Busca conversa existente
    res = db.table("conversations")\
        .select("*")\
        .eq("contact_phone", phone)\
        .maybe_single()\
        .execute()
    
    if res.data:
        return res.data  # já existe
    
    # Cria nova
    row = db.table("conversations").insert({
        "contact_phone": phone,
        "contact_name": name or phone,
        "lead_status": "novo"
    }).execute()
    
    return row.data[0]
```

---

## 📱 Teste Local

### 1. Rodar backend

```bash
cd backend
python main.py
```

Deve mostrar:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 2. Rodar frontend

```bash
npm run dev
```

Deve abrir:
```
http://localhost:5173
```

### 3. Testar fluxo local (sem WhatsApp real)

Edite `backend/main.py` e adicione um endpoint de teste:

```python
@app.post("/api/test-message")
async def test_message(request: Request):
    body = await request.json()
    
    response = await agent.reply(
        phone="5585987654321",
        contact_name="João Teste",
        user_text=body["text"]
    )
    
    return {"response": response}
```

Teste via curl:
```bash
curl -X POST http://localhost:8000/api/test-message \
  -H "Content-Type: application/json" \
  -d '{"text": "Olá! Vocês fazem eventos corporativos?"}'
```

---

## 🎨 Customizações Recomendadas para Novas Empresas

### 1. **Persona**
Edite `persona.py` com:
- Nome e descrição da empresa
- Tom de voz (warm/corporate/playful/etc)
- Serviços específicos
- Fluxo de qualificação customizado

### 2. **Extraction de Leads**
Edite `_extract_lead_info()` em `agent.py` pra extrair dados relevantes:
```python
# Exemplo pra e-commerce:
if "tamanho" in lower:
    fields["preferred_size"] = extract_size(lower)

# Exemplo pra agência:
if "orçamento" in lower or "custa" in lower:
    fields["has_budget_question"] = True
```

### 3. **Fields do Banco**
Adicione colunas na tabela `leads` pra dados específicos:
```sql
ALTER TABLE leads ADD COLUMN client_segment TEXT;
ALTER TABLE leads ADD COLUMN preferred_contact_time TEXT;
```

### 4. **Model do Claude**
No `agent.py`, line 131:
```python
response = get_client().messages.create(
    model="claude-opus-4-7",  # Mais poderoso (custo +)
    # ou
    model="claude-haiku-4-5",  # Mais rápido e barato
    max_tokens=1024,
    system=system_prompt,
    messages=messages,
)
```

---

## 📈 Métricas & Monitoramento

### Supabase Dashboard

Vá em **SQL Editor** pra queries rápidas:

```sql
-- Quantas conversas?
SELECT COUNT(*) FROM conversations;

-- Qual empresa tem mais leads?
SELECT COUNT(*), source FROM leads GROUP BY source;

-- Última atividade?
SELECT contact_name, last_message_at 
FROM conversations 
ORDER BY last_message_at DESC LIMIT 10;

-- Taxa de resposta?
SELECT 
  COUNT(CASE WHEN sender = 'user' THEN 1 END) as client_msgs,
  COUNT(CASE WHEN sender = 'ai' THEN 1 END) as ai_msgs
FROM messages;
```

---

## ⚠️ Troubleshooting

| Problema | Solução |
|----------|---------|
| "Connection refused" ao testar | Backend não está rodando. Rode `python main.py` |
| QR code não aparece | Evolution API URL ou KEY incorretos. Teste com curl |
| Mensagens não salvam | SUPABASE_SERVICE_KEY errada. Verifique em Settings → API |
| Resposta muito lenta | Aumente `max_tokens` ou mude pra Haiku (mais rápido) |
| Claude não responde | ANTHROPIC_API_KEY expirada ou sem créditos. Verifique em console.anthropic.com |
| Evolution API retorna erro | Instância não está conectada. Escaneie QR novamente |

---

## 🚀 Próximos Passos

1. **Adicionar análise de sentimento**: Detectar cliente insatisfeito
2. **Integrar CRM**: Syncar leads com Salesforce/HubSpot
3. **Multi-idioma**: Detectar idioma automaticamente
4. **Agendamento**: Integrar com calendário (Google Calendar, etc)
5. **Conhecimento customizado**: Usar RAG com docs da empresa
6. **Analytics avançado**: Dashboard com métricas de conversão

---

## 📚 Referências

- **Anthropic Claude**: https://docs.anthropic.com/
- **Supabase**: https://supabase.com/docs
- **Evolution API**: https://evolution-api.com/docs
- **FastAPI**: https://fastapi.tiangolo.com
- **Vercel Deploy**: https://vercel.com/docs

---

**Última atualização**: 2026-05-18  
**Versão**: 1.0  
**Status**: Pronto para replicação
