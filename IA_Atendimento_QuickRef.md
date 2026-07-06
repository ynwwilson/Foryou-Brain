# ⚡ Quick Reference - IA de Atendimento

**Uma página com tudo que você precisa saber**

---

## 🏗️ Arquitetura em 1 Minuto

```
CLIENTE
  │ WhatsApp
  ▼
EVOLUTION API
  │ Webhook (POST)
  ▼
BACKEND (FastAPI)
  ├─ Recebe evento
  ├─ Extrai texto + imagem
  ├─ Busca histórico (Supabase)
  ├─ Chama Claude API
  ├─ Salva resposta (Supabase)
  ├─ Extrai lead (automático)
  └─ Envia via Evolution
  ▲ ▼
SUPABASE (PostgreSQL)
  ├─ conversations (histórico)
  ├─ messages (chat)
  ├─ leads (qualificados)
  ├─ ai_settings (config)
  └─ whatsapp_instance (status)
  
FRONTEND (React Lovable)
  └─ Painel para gerenciar + conectar WhatsApp
```

---

## 🔌 Conexões Entre Serviços

| De | Para | O Quê | Frequência |
|---|---|---|---|
| Cliente | Evolution API | Mensagens WhatsApp | Sempre |
| Evolution API | Backend | Webhooks (events) | Sempre |
| Backend | Claude API | Processamento IA | Por mensagem |
| Backend | Supabase | Histórico + config | Por mensagem |
| Backend | Evolution API | Respostas | Por mensagem |
| Frontend | Backend | API calls | On demand |
| Frontend | Supabase | Ler config | On load |

---

## 📦 Stack por Componente

| Componente | Stack | Deploy | Custo |
|---|---|---|---|
| **Backend** | Python 3.10+ FastAPI | Vercel Serverless | ~$5-20/mês |
| **Frontend** | React TypeScript Lovable | Vercel Static | ~$5-20/mês |
| **Database** | Supabase (PostgreSQL) | Cloud | ~$0-50/mês |
| **IA** | Claude Sonnet 4.6 | Anthropic API | Pay-as-you-go |
| **WhatsApp** | Evolution API | Self-hosted ou provider | ~$50-200/mês |

---

## 🎯 Fluxo de Implementação (4 Horas)

```
0h    │ Setup credenciais (API keys)
      │ └─ Anthropic, Supabase, Evolution
      ▼
1h    │ Banco de dados (criar tabelas)
      │ └─ Supabase SQL
      ▼
2h    │ Backend + Frontend local
      │ └─ Testar fluxo completo
      ▼
3h    │ Customizar persona
      │ └─ Editar system prompt
      ▼
4h    │ Deploy (Vercel)
      │ └─ Go live!
```

---

## 🚀 Comandos Essenciais

### 1. Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Editar .env com suas credenciais
python main.py
```

### 2. Setup Frontend
```bash
cd ..
npm install
npm run dev
# Abrir http://localhost:5173
```

### 3. Testar API
```bash
curl http://localhost:8000/health
# Esperado: {"status":"ok"}
```

### 4. Deploy
```bash
git push origin main
# Vercel detecta e faz deploy automático
```

---

## 🔑 Credenciais Necessárias

| Serviço | Obter em | O Que Copiar |
|---|---|---|
| **Anthropic** | console.anthropic.com/api/keys | `sk-ant-...` |
| **Supabase** | project.supabase.co/settings/api | URL + Service Role Key |
| **Evolution** | seu-servidor-evolution:8080 | URL + API Key |

**Tempo para obter:** ~15 minutos total

---

## 📊 Tabelas do Banco (5 no Total)

```sql
conversations    -- Chats com clientes
messages         -- Histórico de mensagens
leads            -- Leads qualificados
ai_settings      -- Config da IA (tone, nome, etc)
whatsapp_instance-- Status WhatsApp (conectado/desconectado)
```

**Schema mínimo:** ~500 linhas SQL (incluído em Templates)

---

## 🎭 Personas de Exemplo

| Negócio | Tom | Fluxo Principal |
|---|---|---|
| **Cenografia** | Profissional + criativo | Tipo evento → Data → Local → Orçamento |
| **E-commerce** | Descontraído + amigável | Tipo → Tamanho → Cor → Checkout |
| **Consultório** | Empático + tranquilizador | Problema → Agende → Tranquilize |
| **Agência viagens** | Inspirador + aventureiro | Destino → Datas → Orçamento → Proposta |

---

## 💰 Preço Estimado (1º mês)

| Serviço | Custo | Notas |
|---|---|---|
| Anthropic API | $5-50 | Pay-as-you-go (~$0.003/1k tokens entrada) |
| Supabase | $25 | Starter plan incluso |
| Vercel | $0-20 | Incluso no free tier |
| Evolution API | $50-200 | Depende do provider |
| **Total** | **$80-270** | Escalável com volume |

---

## 📱 WhatsApp: O Que Você Precisa

- ✅ **Número dedicado** (não use pessoal)
- ✅ **Evolution API** acesso (próprio servidor ou provider)
- ✅ **Backend URL** pública (pra webhook)
- ❌ NÃO precisa de Business API da Meta (mais caro)

---

## ⚡ Performance Esperada

| Métrica | Valor | Notas |
|---|---|---|
| Tempo resposta | 2-5 segundos | Depende da Evolution API |
| Custo/mensagem | $0.005-0.02 | Variável por tamanho |
| Uptime | 99%+ | Vercel + Supabase |
| Histórico | Indefinido | Escalável até TB |

---

## 🔒 Segurança

- ✅ HTTPS por padrão (Vercel)
- ✅ Env vars sensíveis em Vercel (não em .env)
- ✅ Service role key no backend apenas
- ✅ Webhook signature opcional (WEBHOOK_SECRET)
- ✅ Rate limiting em Evolution API

**Setup:** ~5 minutos

---

## 🆘 Top 3 Problemas & Soluções

| Problema | Causa | Solução |
|---|---|---|
| "401 Unauthorized" | API key inválida | Gerar nova em console.anthropic.com |
| QR code não aparece | Evolution URL errada | Verificar EVOLUTION_API_URL no .env |
| Mensagens não salvam | Service key incorreta | Copiar de Supabase → Settings → API |

---

## 🎓 Customização: Níveis de Esforço

| Level | O Que Muda | Tempo |
|---|---|---|
| **Nível 1** | Persona (nome, tom) | 15 min |
| **Nível 2** | Extraction (dados a coletar) | 30 min |
| **Nível 3** | Fluxo (perguntas, respostas) | 1 hora |
| **Nível 4** | Integração com CRM/Tools | 4+ horas |

---

## 📚 Arquivos Principais

```
meu-projeto/
├── backend/
│   ├── main.py              ← FastAPI app
│   ├── agent.py             ← Lógica Claude
│   ├── persona.py           ← System prompt
│   ├── whatsapp.py          ← Evolution client
│   ├── whatsapp_manager.py  ← Gerenciar instância
│   ├── supabase_client.py   ← DB queries
│   ├── .env                 ← Variáveis
│   └── requirements.txt      ← Deps Python
├── src/
│   ├── pages/               ← React pages
│   ├── components/          ← UI components
│   └── integrations/        ← Supabase client
├── package.json             ← Deps Node
└── vite.config.ts           ← Build config
```

---

## 🎯 Próximos Passos Depois de Live

1. **Treinar equipe** no uso do painel
2. **Monitorar logs** e ajustar prompts
3. **Coletar feedback** de clientes
4. **Análise de sentimento** (opcional)
5. **Integração com CRM** (Salesforce/HubSpot)
6. **Multi-idioma** (detectar automático)

---

## 📞 Suporte Rápido

- **Docs Anthropic**: https://docs.anthropic.com
- **Supabase Docs**: https://supabase.com/docs
- **Evolution API**: https://evolution-api.com/docs
- **FastAPI**: https://fastapi.tiangolo.com
- **Vercel**: https://vercel.com/docs

---

## ✅ Checklist Básico

- [ ] Credenciais obtidas (Anthropic, Supabase, Evolution)
- [ ] Banco criado (5 tabelas)
- [ ] Backend rodando local
- [ ] Frontend rodando local
- [ ] WhatsApp conectado e testado
- [ ] Persona customizada
- [ ] Deploy em produção
- [ ] Equipe treinada

**Tempo total: 4 horas (primeira vez)**

---

**Pronto? Comece pelo Manual Completo → Checklist → Templates!**

*Última atualização: 2026-05-18*
