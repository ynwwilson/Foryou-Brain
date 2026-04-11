---
tags: [tipo/guia, projeto/foryoucode, chatbot, infra]
data: 2026-04-04
---

# Manual de Clonagem White-Label — IA ForYou Code (v3.1)

Este guia é a sua "receita de bolo" definitiva para replicar todo o ecossistema (IA + Painel + Banco) para um novo cliente em aproximadamente **20 a 30 minutos**.

## Estrutura Multi-modal v3.1 (O que foi entregue hoje)
- **Visão:** Suporte a análise de imagens (Anthropic Vision).
- **Voz:** Transcrição automática (OpenAI Whisper).
- **Catálogo Visual:** Envio de fotos/vídeos nativos via WhatsApp.
- **Humanização:** Mirroring, fatiamento em balões e banimento de emojis.

## O que muda por cliente (White-Label Checklist)

| Item | Onde mudar |
|---|---|
| **Painel Lovable** | "Copy Project" no Lovable → Trocar logo e cores. |
| **Repo Vercel** | Git clone do template → Novo repositório GitHub. |
| **Instância MegaAPI** | Criar nova instância → Escanear QR Code do Cliente. |
| **Banco Supabase** | Criar novo projeto → Rodar SQL Schema v3.1. |
| **Identity (AI Config)** | Tabela `ai_config` → Nome da IA, Horários e Prompt. |
| **Produtos (Catalog)** | Tabela `products` → Importar nomes, preços e URLs de fotos. |
| **Redis Upstash** | Criar novo db para isolar o agrupamento de mensagens. |

---

## Passo a Passo

### 1. Clonar Repositório
```bash
cp -r concretize-ia-webhook novo-cliente-ia
cd novo-cliente-ia
git init && git add . && git commit -m "init"
# Push para novo repositório GitHub
```

### 2. Editar Contexto do Negócio
Abra `lib/context.ts` e substitua a constante de contexto (ex: `CONCRETIZE_CONTEXT`) pelas regras do novo cliente:
- Nome da empresa e do atendente.
- Produtos/serviços e preços.
- Regiões atendidas e prazos.
- Regra de transferência (ex: "se pedir orçamento, transfire").

### 3. Setup de Serviços

- **MegaAPI:** Criar instância → Conectar WhatsApp QR Code → Pegar credenciais.
- **Upstash:** Criar Redis Database → Pegar credenciais (REST).
- **Supabase:** Criar projeto → Rodar SQL (ver schema abaixo).
- **Chatwoot:** Settings → Inboxes → Add Inbox (API) → Nota: Pegar Token no perfil do usuário.

#### Schema SQL Mínimo (Supabase)
```sql
create table conversations (
  id uuid primary key default gen_random_uuid(),
  contact_phone text not null,
  contact_name text,
  status text default 'open',
  is_ai_handled boolean default true,
  last_message text,
  last_message_at timestamptz,
  created_at timestamptz default now()
);

create table messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid references conversations(id),
  role text not null, -- 'user', 'ai', 'agent'
  content text not null,
  created_at timestamptz default now()
);

create table leads (
  id uuid primary key default gen_random_uuid(),
  phone text unique not null,
  name text,
  status text default 'warm',
  source text default 'whatsapp',
  created_at timestamptz default now()
);

create table ai_config (
  id int primary key generated always as identity,
  prompt text not null,
  is_active boolean default true,
  created_at timestamptz default now()
);
```

### 4. Deploy Vercel
Configure as Env Vars (atenção: não deixe espaços em branco ao colar):
- `ANTHROPIC_API_KEY` (Para Visão)
- `OPENAI_API_KEY` (Para Transcrição de Áudio)
- `MEGAAPI_HOST`, `MEGAAPI_INSTANCE_KEY`, `MEGAAPI_TOKEN`
- `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
- `UPSTASH_REDIS_REST_URL`, `UPSTASH_REDIS_REST_TOKEN`
- `CHATWOOT_URL`, `CHATWOOT_TOKEN`, `CHATWOOT_ACCOUNT_ID`, `CHATWOOT_INBOX_ID`

## 💎 Toque de Mestre: Ativando a IA
Não basta clonar, é preciso dar vida ao assistente:
1.  **AI Config:** Vá ao banco e insira o nome do atendente (Ex: "Felipe") e o tom de voz.
2.  **Catalog URLs:** No painel, cole os links das fotos reais dos produtos nas colunas `image_url`. Isso ativa o "Vendedor Visual".
3.  **Webhook:** Lembrar de registrar a nova URL da Vercel no MegaAPI.

---

## Lições Aprendidas (Importante)
- **Whitespace:** Vercel preserva espaços. Sempre dê `trim()` nos tokens ao colar.
- **Remote JID:** Use sempre `key.remoteJid` para identificar o destinatário, nunca o ID da instância.
- **Sincronia:** O batching de 3s no Redis é essencial para agrupar mensagens e evitar respostas duplicadas.
