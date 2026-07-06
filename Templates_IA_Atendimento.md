# 📄 Templates & Exemplos de Código

**Pronto para copiar/colar em sua IA de atendimento**

---

## 1️⃣ `requirements.txt` (Backend Python)

Crie arquivo `backend/requirements.txt`:

```
fastapi==0.100.0
uvicorn==0.23.0
python-dotenv==1.0.0
anthropic==0.15.0
supabase==2.0.0
httpx==0.24.0
```

**Instalação:**
```bash
pip install -r requirements.txt
```

---

## 2️⃣ `.env` Template

Crie `backend/.env`:

```env
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ANTHROPIC API (Claude)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANTHROPIC_API_KEY=sk-ant-v0-XXXXXXXXXXXX

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SUPABASE (PostgreSQL Database)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUPABASE_URL=https://abc123.supabase.co
SUPABASE_SERVICE_KEY=eyJ0eXAiOiJKV1QiLCJhbGc...

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EVOLUTION API (WhatsApp)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVOLUTION_API_URL=http://seu-servidor-evolution:8080
EVOLUTION_API_KEY=sua-chave-evolution
EVOLUTION_INSTANCE=nomeda-empresa

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BACKEND URL (para webhooks)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BACKEND_URL=https://seu-projeto.vercel.app

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DEVELOPMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PORT=8000
```

---

## 3️⃣ Personas de Exemplo

### A. Agência de Cenografia (Totus AI original)

```python
# backend/persona_cenografia.py

SYSTEM_PROMPT = """Você é a assistente virtual da Totus Cenografia, chamada TOTUS AI.

## Sobre a Totus Cenografia
A Totus Cenografia é especializada em cenografia, decoração e montagem de eventos corporativos e sociais.
Criamos ambientes únicos e memoráveis para feiras, lançamentos, casamentos, formaturas e eventos em geral.

## Sua personalidade
- Tom: caloroso, profissional e criativo
- Você representa uma empresa premium — transmita confiança e qualidade
- Seja consultiva: entenda a necessidade antes de oferecer solução
- Fale sobre design, estética e experiência

## Suas responsabilidades
1. **Atendimento**: recepcionar o cliente com entusiasmo
2. **Qualificação**: descobrir tipo de evento, data, local, orçamento
3. **Portfolio**: descrever trabalhos anteriores
4. **Contato comercial**: encaminhar para equipe de vendas

## Fluxo de conversa
- Nome do cliente
- Tipo de evento (corporativo / social / casamento / formatura / feira / lançamento)
- Data prevista
- Local/cidade
- Número de pessoas
- Estilo desejado ou referências
- Orçamento (opcional)

## Encerramento
Quando tiver as informações: "Perfeito! Vou passar seus dados para nossa equipe. Eles entrarão em contato em breve com uma proposta personalizada! 🎯"
"""
```

### B. E-commerce de Moda

```python
# backend/persona_moda.py

SYSTEM_PROMPT = """Você é a assistente virtual da [NOME LOJA], chamada [AI_NAME].

## Sobre [NOME LOJA]
Somos uma loja online de moda premium com foco em tendências e qualidade.
Oferecemos roupas, acessórios e calçados para todos os estilos.

## Sua personalidade
- Tom: descontraído, amigável, atualizado com tendências
- Você é uma fashion buddy — ajude o cliente a encontrar o look perfeito
- Use emojis com moderação mas com personalidade

## Suas responsabilidades
1. **Boas-vindas**: receba com energia e ofereça ajuda
2. **Busca de produtos**: entenda o estilo, ocasião, tamanho
3. **Recomendações**: sugira combinações e looks
4. **Dúvidas**: responda sobre envios, trocas, materiais
5. **Carrinho**: ajude a finalizar compra se necessário

## Fluxo de conversa
- O que está procurando? (tipo, cor, estilo)
- Ocasião? (casual, festivo, trabalho, etc)
- Tamanho usual?
- Faixa de preço?

## Encerramento
"Adorei ajudar! Se quiser adicionar ao carrinho, é só dizer. Aproveite sua compra! 💋"
"""
```

### C. Consultório Odontológico

```python
# backend/persona_dentista.py

SYSTEM_PROMPT = """Você é a assistente virtual do [NOME CONSULTÓRIO], chamada [AI_NAME].

## Sobre [NOME CONSULTÓRIO]
Somos um consultório odontológico moderno oferecendo limpeza, estética, implantes e tratamentos gerais.
Funcionamos de segunda a sexta, 8h-18h.

## Sua personalidade
- Tom: profissional, acolhedor e tranquilizador
- Transmita confiança e expertise
- Seja empático com ansiedades de pacientes

## Suas responsabilidades
1. **Recepção**: cumprimente e qualifique a necessidade
2. **Agendamento**: agende consultas em horários disponíveis
3. **Informações**: explique tratamentos e duração
4. **Tranquilização**: responda sobre dor, anestesia, pós-operatório
5. **Encaminhamento**: passe pro atendente human se precisar

## Fluxo de conversa
- Nome e telefone
- Qual é a principal dúvida/problema? (dor, estética, limpeza, etc)
- Primeira vez aqui ou paciente retorno?
- Quando gostaria de vir?

## Encerramento
"Perfeito! Vou agendar sua consulta. A equipe confirmará por SMS. Qualquer dúvida, é só chamar! 😊"
"""
```

### D. Agência de Viagens

```python
# backend/persona_viagens.py

SYSTEM_PROMPT = """Você é a assistente virtual da [NOME AGÊNCIA], chamada [AI_NAME].

## Sobre [NOME AGÊNCIA]
Somos uma agência de viagens especializadas em pacotes nacionais e internacionais.
Oferecemos customização total para roteiros perfeitos.

## Sua personalidade
- Tom: inspirador, entusiasmado, aventureiro
- Você é um travel buddy — inspire sonhos
- Seja consultivo mas entusiasmado

## Suas responsabilidades
1. **Inspiração**: entenda o tipo de viagem desejado
2. **Qualificação**: saiba orçamento, datas, grupo
3. **Recomendações**: sugira destinos e pacotes
4. **Detalhes**: documentos, vistos, dicas práticas
5. **Fechamento**: encaminhe para agente de vendas

## Fluxo de conversa
- Tipo de viagem? (praia, montanha, cidade, aventura, cultural)
- Quando gostaria de viajar?
- Quantas pessoas?
- Duração prevista?
- Orçamento aproximado?

## Encerramento
"Que viagem incrível te espera! Vou passar pro nosso especialista que fará a proposta perfeita. 🌍✈️"
"""
```

---

## 4️⃣ SQL Scripts Prontos

### Script 1: Criar todas as tabelas

```sql
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- CONVERSATIONS (Histórico de chats)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREATE TABLE conversations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  contact_phone TEXT UNIQUE NOT NULL,
  contact_name TEXT,
  lead_status TEXT DEFAULT 'novo',
  last_message_at TIMESTAMP DEFAULT now(),
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_conversations_phone ON conversations(contact_phone);
CREATE INDEX idx_conversations_last_message ON conversations(last_message_at DESC);

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- MESSAGES (Cada mensagem)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREATE TABLE messages (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE NOT NULL,
  sender TEXT NOT NULL,
  content TEXT NOT NULL,
  media_url TEXT,
  created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_messages_conversation ON messages(conversation_id);
CREATE INDEX idx_messages_created ON messages(created_at DESC);

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- LEADS (Leads qualificados)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREATE TABLE leads (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  phone TEXT UNIQUE NOT NULL,
  name TEXT,
  email TEXT,
  event_type TEXT,
  event_date TEXT,
  location TEXT,
  estimated_guests INTEGER,
  budget DECIMAL(10,2),
  reference_style TEXT,
  source TEXT DEFAULT 'whatsapp',
  status TEXT DEFAULT 'novo',
  notes TEXT,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_leads_phone ON leads(phone);
CREATE INDEX idx_leads_status ON leads(status);

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- AI_SETTINGS (Configurações da IA)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREATE TABLE ai_settings (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  ai_name TEXT,
  tone_of_voice TEXT,
  custom_instructions TEXT,
  welcome_message TEXT,
  business_description TEXT,
  business_hours TEXT,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- WHATSAPP_INSTANCE (Status WhatsApp)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREATE TABLE whatsapp_instance (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  instance_name TEXT UNIQUE NOT NULL,
  status TEXT DEFAULT 'disconnected',
  phone TEXT,
  profile_name TEXT,
  qr_code TEXT,
  last_check TIMESTAMP DEFAULT now(),
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- ANALYTICS (Opcional: Métricas)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREATE TABLE analytics (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
  sentiment TEXT,  -- positive, neutral, negative
  response_time_ms INTEGER,
  model_used TEXT,
  tokens_used INTEGER,
  created_at TIMESTAMP DEFAULT now()
);
```

### Script 2: Inserir dados de exemplo

```sql
-- Insert ai_settings example
INSERT INTO ai_settings (
  ai_name,
  tone_of_voice,
  custom_instructions,
  welcome_message,
  business_description,
  business_hours
) VALUES (
  'Luna',
  'amigável, descontraído, atualizado',
  'Sempre ofereça atendimento excepcional',
  'Oi! 👋 Bem-vindo! Como posso ajudar?',
  'Somos a melhor loja de X do país',
  'Seg-Sex: 9h-18h | Sáb: 10h-14h'
);

-- Insert whatsapp instance
INSERT INTO whatsapp_instance (
  instance_name,
  status
) VALUES (
  'minha-empresa',
  'disconnected'
);
```

### Script 3: Queries úteis de análise

```sql
-- Quantas conversas?
SELECT COUNT(*) as total_conversas FROM conversations;

-- Conversas por status
SELECT lead_status, COUNT(*) FROM conversations GROUP BY lead_status;

-- Últimas conversas
SELECT contact_name, last_message_at 
FROM conversations 
ORDER BY last_message_at DESC 
LIMIT 10;

-- Taxa de mensagens por conversa
SELECT 
  c.id,
  c.contact_name,
  COUNT(m.id) as total_mensagens
FROM conversations c
LEFT JOIN messages m ON c.id = m.conversation_id
GROUP BY c.id
ORDER BY total_mensagens DESC;

-- Leads por tipo de evento
SELECT event_type, COUNT(*) 
FROM leads 
WHERE event_type IS NOT NULL
GROUP BY event_type;

-- Leads com maior orçamento
SELECT name, event_type, budget 
FROM leads 
WHERE budget IS NOT NULL
ORDER BY budget DESC 
LIMIT 10;
```

---

## 5️⃣ Customizações de `agent.py`

### Extraction de Lead Customizada (E-commerce)

```python
def _extract_lead_info(text: str, phone: str) -> None:
    """Extrai informações específicas pra e-commerce."""
    fields = {}
    lower = text.lower()
    
    # Nome do cliente
    if "meu nome é" in lower or "me chamo" in lower:
        parts = lower.split("meu nome é") if "meu nome é" in lower else lower.split("me chamo")
        if len(parts) > 1:
            name = parts[1].strip().split()[0].capitalize()
            fields["name"] = name
    
    # Tipo de produto
    tipos = ["calça", "blusa", "vestido", "sapato", "jaqueta", "bolsa", "acessório"]
    for tipo in tipos:
        if tipo in lower:
            fields["product_interest"] = tipo
            break
    
    # Tamanho
    tamanhos = ["pp", "p", "m", "g", "gg", "xg", "34", "36", "38", "40", "42"]
    for tam in tamanhos:
        if f"tamanho {tam}" in lower or f"numero {tam}" in lower or f"size {tam}" in lower:
            fields["preferred_size"] = tam
            break
    
    # Cor
    cores = ["preto", "branco", "vermelho", "azul", "rosa", "verde", "cinza", "bege"]
    for cor in cores:
        if cor in lower:
            fields["color_preference"] = cor
            break
    
    if fields:
        db.upsert_lead(phone, **fields)
```

### Extraction de Lead Customizada (Agência de Viagens)

```python
def _extract_lead_info(text: str, phone: str) -> None:
    """Extrai informações de viagem."""
    fields = {}
    lower = text.lower()
    
    # Nome
    if "meu nome é" in lower or "me chamo" in lower:
        parts = lower.split("meu nome é") if "meu nome é" in lower else lower.split("me chamo")
        if len(parts) > 1:
            name = parts[1].strip().split()[0].capitalize()
            fields["name"] = name
    
    # Tipo de viagem
    destinos = {
        "caribe": "praia",
        "maldivas": "praia",
        "paris": "cidade",
        "nova york": "cidade",
        "machu picchu": "aventura",
        "safári": "aventura"
    }
    for dest, tipo in destinos.items():
        if dest in lower:
            fields["trip_type"] = tipo
            fields["destination"] = dest
            break
    
    # Orçamento
    import re
    match = re.search(r'(\d+)\s*(?:mil|k)', lower)
    if match:
        fields["budget"] = int(match.group(1)) * 1000
    
    if fields:
        db.upsert_lead(phone, **fields)
```

---

## 6️⃣ Variáveis Customizáveis por Empresa

Crie arquivo `backend/config.py`:

```python
# config.py
import os

class Config:
    # Empresa
    COMPANY_NAME = os.getenv("COMPANY_NAME", "Minha Empresa")
    COMPANY_CITY = os.getenv("COMPANY_CITY", "São Paulo")
    
    # Claude
    CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")
    CLAUDE_MAX_TOKENS = int(os.getenv("CLAUDE_MAX_TOKENS", "1024"))
    
    # WhatsApp
    EVOLUTION_TIMEOUT = 30
    
    # Supabase
    DB_QUERY_LIMIT = 50
    
    # Extraction
    EXTRACT_KEYWORDS = {
        "nome": ["meu nome é", "me chamo", "sou", "chamam-me"],
        "email": ["email", "mail", "@"],
        "telefone": ["tel", "celular", "whatsapp", "ligue"],
    }

config = Config()
```

---

## 7️⃣ Exemplo de Teste Local

Arquivo `test_agent_local.py`:

```python
import asyncio
from backend.agent import reply

async def test():
    # Teste 1: Mensagem simples
    response = await reply(
        phone="5585987654321",
        contact_name="João",
        user_text="Olá! Vocês fazem eventos?"
    )
    print(f"Resposta: {response}")
    
    # Teste 2: Segunda mensagem (histórico)
    response = await reply(
        phone="5585987654321",
        contact_name="João",
        user_text="Qual é o preço?"
    )
    print(f"Resposta 2: {response}")

if __name__ == "__main__":
    asyncio.run(test())
```

**Rodar:**
```bash
python test_agent_local.py
```

---

## 8️⃣ GitHub Actions CI/CD (Opcional)

Arquivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Vercel

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Vercel
        uses: vercel/action@master
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

---

## 9️⃣ Logs e Debug

Editar `backend/main.py` para mais logs:

```python
import logging

# Setup detalhado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

log = logging.getLogger(__name__)

# Adicionar em cada função importante:
log.info(f"Recebida mensagem de {phone}: {user_text[:50]}...")
log.debug(f"History length: {len(history)}")
log.error(f"Erro ao processar: {e}", exc_info=True)
```

---

## 🔟 Segurança: Variáveis Sensíveis

**Nunca commite .env!**

`.gitignore`:
```
.env
.env.local
__pycache__
venv/
node_modules/
.DS_Store
```

**Em Vercel:**
- Settings → Environment Variables
- Adicionar cada var manualmente (não fazer paste do .env!)

---

**Próxima etapa?** Escolha uma persona de exemplo, adapte pro seu negócio e comece o checklist!
