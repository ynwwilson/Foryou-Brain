# ✅ Checklist de Implantação - IA de Atendimento

**Tempo estimado**: 3-4 horas (primeira vez)

---

## 🔐 Setup de Credenciais (30 min)

- [ ] **Anthropic API**
  - [ ] Criar conta em https://console.anthropic.com
  - [ ] Settings → API Keys → Create Key
  - [ ] Copiar `ANTHROPIC_API_KEY=sk-ant-...`
  - [ ] ✅ Guardar em `.env`

- [ ] **Supabase**
  - [ ] Criar projeto em https://supabase.com
  - [ ] Escolher região (São Paulo recomendado)
  - [ ] Copiar `SUPABASE_URL=https://xxxx.supabase.co`
  - [ ] Settings → API → Copiar Service Role Key
  - [ ] ✅ Guardar ambos em `.env`

- [ ] **Evolution API**
  - [ ] Decidir: servidor próprio ou fornecedor?
  - [ ] Obter `EVOLUTION_API_URL`
  - [ ] Obter `EVOLUTION_API_KEY`
  - [ ] Definir `EVOLUTION_INSTANCE=nome-empresa`
  - [ ] ✅ Guardar em `.env`

- [ ] **Backend URL**
  - [ ] Será: `https://seu-projeto.vercel.app` (depois do deploy)
  - [ ] Por enquanto, usar localhost: `http://localhost:8000`
  - [ ] ✅ Guardar em `.env` como `BACKEND_URL=`

---

## 🗄️ Banco de Dados (30 min)

- [ ] **Supabase SQL Editor**
  - [ ] Acessar SQL Editor
  - [ ] Executar script de criação de `conversations` table
  - [ ] Executar script de criação de `messages` table
  - [ ] Executar script de criação de `leads` table
  - [ ] Executar script de criação de `ai_settings` table
  - [ ] Executar script de criação de `whatsapp_instance` table
  - [ ] Verificar que todas as tabelas foram criadas

- [ ] **Índices e Constraints**
  - [ ] Criar índice em `messages.conversation_id`
  - [ ] Criar índice em `conversations.contact_phone`
  - [ ] Verificar que as constraints de foreign key existem

---

## 💻 Backend Setup (45 min)

- [ ] **Projeto local**
  - [ ] Clonar ou criar novo repositório
  - [ ] Navegar para pasta `backend/`
  - [ ] Criar `venv`: `python -m venv venv`
  - [ ] Ativar: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
  - [ ] Instalar deps: `pip install -r requirements.txt`
    - [ ] Se `requirements.txt` não existir, criar com:
      ```
      fastapi==0.100.0
      uvicorn==0.23.0
      python-dotenv==1.0.0
      anthropic==0.15.0
      supabase==2.0.0
      httpx==0.24.0
      ```

- [ ] **Configurar `.env`**
  - [ ] Copiar `.env.example` para `.env`
  - [ ] Preencher todos os valores (do passo anterior)
  - [ ] ✅ Salvar

- [ ] **Testar backend local**
  - [ ] Rodar: `python main.py`
  - [ ] Verificar: "Uvicorn running on http://0.0.0.0:8000"
  - [ ] Testar: `curl http://localhost:8000/health`
  - [ ] Esperar resposta: `{"status":"ok"}`

---

## 🧠 Customizar Persona (30 min)

- [ ] **Editar `backend/persona.py`**
  - [ ] Mudar nome da empresa no SYSTEM_PROMPT
  - [ ] Atualizar descrição do negócio
  - [ ] Customizar tom de voz (caloroso, profissional, criativo, etc)
  - [ ] Atualizar fluxo de qualificação com dados específicos
  - [ ] Salvar

- [ ] **Popular `ai_settings` no Supabase**
  - [ ] Ir em Supabase → Table Editor
  - [ ] Selecionar tabela `ai_settings`
  - [ ] Clicar Insert
  - [ ] Preencher:
    - `ai_name`: Nome que a IA usa
    - `tone_of_voice`: Descrição do tom
    - `custom_instructions`: Instruções extras
    - `welcome_message`: Saudação primeira mensagem
    - `business_description`: Sobre a empresa
  - [ ] ✅ Salvar

---

## 📱 Configurar WhatsApp (45 min)

- [ ] **Evolution API Setup**
  - [ ] Garantir que servidor Evolution API está rodando
  - [ ] Testar acesso: `curl http://seu-evolution-api:8080/instance/fetchInstances`
  - [ ] Verificar que EVOLUTION_API_KEY está funcionando

- [ ] **Conectar WhatsApp**
  - [ ] (Depois do frontend estar rodando)
  - [ ] Acessar painel em http://localhost:5173
  - [ ] Clicar em "Conectar WhatsApp"
  - [ ] Escaneie o QR code com celular
  - [ ] Aguarde conexão (~5-10 segundos)
  - [ ] Verifique que aparece "Conectado" + número do telefone
  - [ ] ✅ Teste enviando mensagem pro número

---

## 🎨 Frontend Setup (30 min)

- [ ] **Instalar dependências**
  - [ ] Navegar para raiz do projeto
  - [ ] Rodar: `npm install`
  - [ ] Aguarde conclusão

- [ ] **Rodar frontend local**
  - [ ] `npm run dev`
  - [ ] Acessar: http://localhost:5173
  - [ ] Verificar que carrega sem erros

- [ ] **Testar fluxo completo**
  - [ ] Conecte WhatsApp via painel
  - [ ] Envie mensagem de um celular pro número conectado
  - [ ] Verifique que recebe resposta em ~2-5 segundos
  - [ ] Verifique que apareça histórico no painel

---

## 🚀 Deploy no Vercel (1 hora)

- [ ] **Preparar repositório**
  - [ ] Adicionar `.env.example` (sem valores sensíveis)
  - [ ] Colocar `requirements.txt` na raiz de `backend/`
  - [ ] Git push para GitHub

- [ ] **Vercel Frontend**
  - [ ] Entrar em https://vercel.com
  - [ ] New Project → Selecionar repo
  - [ ] Build: Next.js / Vite (detecta automático)
  - [ ] Deploy automático!
  - [ ] Copiar URL: `https://seu-projeto.vercel.app`

- [ ] **Vercel Backend (Serverless)**
  - [ ] Mesmo projeto Vercel
  - [ ] Add custom env vars do `.env`
  - [ ] Atualizar `BACKEND_URL=https://seu-projeto.vercel.app`
  - [ ] Deploy!

- [ ] **Teste após deploy**
  - [ ] Acessar: `https://seu-projeto.vercel.app/health`
  - [ ] Verificar: `{"status":"ok"}`
  - [ ] Reconectar WhatsApp (update webhook URL)
  - [ ] Enviar mensagem de teste

---

## 🔄 Pós-Deploy (Monitoramento)

- [ ] **Verificar logs Vercel**
  - [ ] Vercel Dashboard → Logs
  - [ ] Procure por erros ao receber mensagens

- [ ] **Monitorar Supabase**
  - [ ] Dashboard → Tables → `messages` deve crescer
  - [ ] Table → `conversations` deve listar chats

- [ ] **Testar evolução**
  - [ ] Envie várias mensagens
  - [ ] Verifique se histórico mantém contexto
  - [ ] Teste upload de imagem
  - [ ] Verifique que leads estão sendo extraídos

---

## 🎯 Customizações Recomendadas (Futura)

**Após ter tudo funcionando:**

- [ ] Adicionar análise de sentimento
- [ ] Customizar extraction de leads (padrões específicos da empresa)
- [ ] Adicionar suporte a novos tipos de evento
- [ ] Integrar com CRM da empresa
- [ ] Adicionar FAQ customizado
- [ ] Treinar equipe no uso do painel
- [ ] Definir SLAs de resposta
- [ ] Setup de escalação automática

---

## 🆘 Se algo der errado...

### Backend não inicia
```bash
# Verifique variáveis de ambiente
echo $ANTHROPIC_API_KEY

# Instale deps faltando
pip install -r requirements.txt

# Rode com logs detalhados
PYTHONUNBUFFERED=1 python main.py
```

### WhatsApp não conecta
```bash
# Verifique Evolution API
curl -H "apikey: YOUR_KEY" http://evolution-api:8080/instance/fetchInstances

# Verifique que BACKEND_URL está correto
echo $BACKEND_URL
```

### Supabase não responde
```bash
# Verifique credenciais
curl -H "Authorization: Bearer YOUR_SERVICE_KEY" https://your-project.supabase.co/rest/v1/conversations

# Verifique que tabelas existem
SELECT * FROM information_schema.tables WHERE table_schema='public';
```

---

## 📞 Suporte

- Documentação completa: Ver `Manual_IA_Atendimento_Totus.md`
- Issues: Abrir no repositório do projeto
- Docs oficiais:
  - Claude API: https://docs.anthropic.com
  - Supabase: https://supabase.com/docs
  - Evolution API: https://evolution-api.com/docs

---

**Boa sorte! 🚀**

Checklist criado em: 2026-05-18
Próxima revisão: quando tiver novo feature request
