---
projeto: Pipeline de Leads ForYou Code
status: Em produção. Roadmap pós-auditoria (Fases 1-5) 100% entregue + Sistema de Ofertas multi-produto + Gerenciador de Campanhas estilo Ads Manager.
criado: 2026-05-14
atualizado: 2026-05-22
tags: [projeto, forYou-code, automacao, leads, vendas, instagram, manychat, apify, claude-api, nextjs, vercel, neon, adspower, multi-user, telegram, anti-detection, ab-test, sentiment, weekly-digest]
---

# Pipeline de Leads — ForYou Code

> **Sistema automatizado completo de prospecção de profissionais de saúde/estética no Instagram para vender websites premium.** Stack migrada de Google Apps Script para **Next.js 15 + Vercel + Neon Postgres + AdsPower + Playwright**.

---

## 📊 Estado em 22/05/2026

> **Roadmap pós-auditoria 100% entregue. Sistema evoluiu pra multi-produto (Ofertas) + Gerenciador de Campanhas estilo Ads Manager.**

### Sessões marcantes
- 18/05: auditoria completa + roadmap pós-auditoria (5 fases, 55 melhorias mapeadas)
- 19-20/05: maratona — Fases 1-4 deployadas + primeiro envio real. Detalhes em [[2026-05-20 01h00 encerramento]]
- 20/05: Fase 5 Multi-vendedor (Wilson + Marco + Eduardo). Detalhes em [[2026-05-20 05h57 - Fase 5 multi-vendedor — código completo + deploy + users]]
- 22/05 00h37: Sistema de Ofertas (multi-produto) + Gerenciador de Campanhas + corte de redundância. Detalhes em [[2026-05-22 00h37 - ForYou Leads — Ofertas + Gerenciador de Campanhas]]
- 22/05 01h15: **Phase 5 Refactor Frontend** (design system zinc, Vercel/GitHub) — entregue, PR #4. Detalhes em [[2026-05-22 01h15 - ForYou Leads — Phase 5 Frontend Redesign]]
- 29/05: **Envio automático + worker sempre-on (sem terminal)** + Ads Manager + templates por oferta — PR #5. Detalhes em [[2026-05-29 - ForYou Leads — Envio automático + sem terminal]]
- 29/05 (2): **Separar Busca × Envio + Públicos Salvos** (sem busca automática diária; busca conclui na meta; público salvo reutilizável) — PR #6. Detalhes em [[2026-05-29b - ForYou Leads — Busca x Envio + Públicos Salvos]]

### Evoluções pós-roadmap (22/05)
- **Sistema de Ofertas**: o produto vendido virou catálogo configurável (`offers`) — público, preço, case, pitch, CTAs. A IA monta as mensagens a partir da oferta. Tela `/admin/ofertas`. Permite vender IA de Atendimento, App, etc. Migration 021.
- **Gerenciador de Campanhas**: a campanha virou objeto completo (captura + envio + oferta + criativo + ritmo). Estados rascunho→pausada→ativa, lista estilo Ads Manager, painel por campanha com "Enviar agora". `/enviar` absorvido. Migration 022.
- **Corte de redundância**: `/hoje`+`/respostas` → `/atendimento`; `/metricas`+ROI Nichos em abas. Menu 12 → 9 itens.

### Phase 5 — Refactor Frontend ✅ ENTREGUE (22/05)
- **Design system zinc/minimalista** (Vercel/GitHub) substituiu o glassmorphism em **todo** o app.
- `components/ui/` novo (button, input, card, badge, select, table, status-badge, stat-card, form-field, etc.), fonte Geist, tokens zinc no tailwind/globals.
- Todas as ~17 telas migradas; zero glassmorphism/rgba/slate sobrando (grep limpo). Build + typecheck limpos.
- **PR #4 mergeado em `main` (29/05) → em produção.** Branch `feat/frontend-redesign` (8 commits).
- Detalhes: [[2026-05-22 01h15 - ForYou Leads — Phase 5 Frontend Redesign]]

### O que está rodando em produção
- ✅ **Fase 1 — Sobrevivência IG:** variação de CTA (8 variantes), rotação de vídeo, detecção bloqueio IG (24h pause), warm-up de conta (3-5min antes do 1º DM), janela horária (só domingo bloqueado), HMAC ManyChat (soft mode), backup Neon → Vercel Blob (domingo 4h BR)
- ✅ **Fase 2 — Reliability:** audit log de status changes, rate limit via Neon (sem Upstash), idempotency webhook ManyChat, migrations versionadas (`npm run migrate`), IG account health check via Apify (diário 8h BR), CRON_SECRET por scope (5 secrets), setup automatizado (`npm run setup:fase2`). Sentry deferred. Test send pulado (sem conta secundária)
- ✅ **Fase 3 — UX:** histórico unificado de conversa (worker registra outbound), search global na sidebar (atalho `/`), filtros persistentes na URL, date range em /metricas, Quick Replies via Claude (3 sugestões contextuais), view dedicada de respostas pendentes (badge dinâmico), export CSV, drag-and-drop no pipeline (@dnd-kit)
- ✅ **Fase 4 — Inteligência:** revenue tracking + ROI por hashtag, A/B test por CTA index (8 variantes mensuradas), sentimento via Claude (😊/😐/😣 em respostas), score insights via Telegram (sexta 17h), Weekly Digest no Telegram (sexta 18h)
- 🔮 **Próxima:** **Multi-vendedor** (Wilson + Marco no Mac M4 + Eduardo no Windows). Plano completo em `C:\Users\ynwwi\.claude\plans\vamos-para-a-fase-adaptive-ember.md` (20 seções, ~1000 linhas)

### Crons agendados no Vercel
- Apify daily 9h30 BR
- Morning brief 10h BR
- Followup 11h BR
- Cleanup 8h BR seg
- Backup Neon 4h BR dom
- Account health 8h BR diário
- Score insights 17h BR sex
- Weekly Digest 18h BR sex

### Validações reais
- 1º DM real entregue pra `@jessica.montelari` (texto + vídeo Dr Eder 19mn)
- Backup Neon validado (14 tabelas, 173 rows, 339 KB)
- IG account snapshot inicial: 1744 followers @ynwwilson
- Weekly Digest testado via Telegram

### Pendências de implementação (Fase Multi-vendedor)
Plano de 8 commits aguardando GO do Wilson. Decisões já tomadas:
- Distribuição: cada campanha pertence a 1 user (flexibilidade semanal)
- UI privacy: "Meus" default, admin vê toggle "Todos"
- Repo privado + GitHub collaborators
- OTP login via bot do user (precisa `/start` antes)
- Apify cron: 5 hashtags × N campanhas
- Cada user com bot Telegram próprio + AdsPower próprio + IG dedicado

### Bugs corrigidos durante a maratona (lembrar)
- `vercel env pull` precisa `--environment=production`
- Vercel marca envs como "Sensitive Encrypted" — não revelam via UI
- Scripts Node não leem `.env.local` automaticamente (worker precisa `loadEnvLocal()`)
- `@vercel/blob` v2: `access:"private"` + `allowOverwrite:true`
- `clickMessageButton` no IG: precisa verificação pós-click + Vision fallback
- Vídeo confirmation: timeout 8s → 20s + benefício da dúvida
- Migration script: pular statements só se TODAS as linhas forem comentários
- PowerShell quebra comandos longos — usar Git Bash no Windows

---

---

## 🎯 Objetivo

**Vender sites profissionais (R$1.500 a R$2.000) pra profissionais individuais de saúde/estética** via prospecção automatizada no Instagram.

- **ICP**: profissionais individuais (não empresas/clínicas institucionais) — dermato, nutri, harmoniza, biomédica estética, médico estético
- **Mercado**: Brasil (foco MG primeiro, expandindo)
- **Followers**: 1.000 a 60.000 (filtro triplo no cron, garante pessoa solo com público real)
- **Canal**: DM no Instagram com mensagem personalizada + vídeo do site referência (Dr. Eder Paula, drederdepaula.com.br)
- **Volume atual**: 15 DMs/dia (potencial até 30 com warm-up)
- **App**: foryou-leads.vercel.app

---

## 🏗 Arquitetura atual (em produção)

3 camadas que conversam entre si:

```
┌──────────────────────────────────────────┐
│  CLOUD (Vercel + Neon + Vercel Blob)    │
│  - Site/Dashboard (Next.js 15)          │
│  - Postgres serverless (Neon)            │
│  - Crons automáticos 24/7                │
│  - Integrações (Apify, Claude, ManyChat) │
└──────────────┬───────────────────────────┘
               │ API REST
┌──────────────▼───────────────────────────┐
│  MÁQUINA DO WILSON (Windows)             │
│  - AdsPower (browser anti-detect)        │
│  - Worker Node.js (envio Playwright)     │
│  - Pasta scripts/videos/ (locais)         │
└──────────────┬───────────────────────────┘
               │ controla browser
┌──────────────▼───────────────────────────┐
│  INSTAGRAM (via AdsPower profile)        │
│  - Captura via Apify (scraping)          │
│  - Envio via worker (DMs)                │
│  - Respostas via webhook ManyChat        │
└──────────────────────────────────────────┘
```

---

## 🔑 Credenciais e Recursos

### Vercel + Neon
- **App**: foryou-leads.vercel.app
- **Banco**: Neon Postgres serverless (free tier, GRU1)
- **Storage**: Vercel Blob (planos pagos por uso — usado pra futuros backups)

### Apify
- **Tasks**: Hashtag Scraper + Profile Scraper (2-stage)
- **Custo**: ~$50-100/mês

### Claude
- **Modelo**: `claude-sonnet-4-6` (alta qualidade) + prompt caching (70% economia)
- **Função**: análise de perfil + geração de msg_unified + Vision fallback no worker
- **Custo**: ~$50-150/mês (depende do volume)

### AdsPower
- **Versão**: V2 (7.12.29)
- **Profile principal**: `k1cn2qmx` (conta @ynwwilson)
- **API local**: `http://127.0.0.1:50325`
- **Verificação de API**: OFF (sem key required pra localhost)

### ManyChat
- **Plano**: Pro (~R$60/mês)
- **Função**: webhook quando lead responde → atualiza status no nosso banco

### Telegram
- **Bot custom** pra notificações
- **Função**: morning brief, alertas de quente, follow-up done, etc.

### Custos totais
| Item | R$/mês |
|------|--------|
| Vercel (free tier) | 0 |
| Neon (free tier) | 0 |
| Claude API | 50-150 |
| Apify | 50-100 |
| ManyChat | 60 |
| AdsPower | 25 |
| **Total** | **~200-350** |

Pra pagar com 1 cliente fechado de R$1.500 = sobra MUITA grana.

---

## 🤖 O que roda automaticamente (24/7)

| Horário | Cron | O que faz |
|---------|------|-----------|
| 09:30 | `/api/cron/apify` | Captura novos leads (hashtags → Apify → Claude → DB) |
| 10:00 | `/api/cron/morning-brief` | Telegram com resumo: quentes, respondidos, agendados, novos, follow-up pendente |
| 11:00 | `/api/cron/followup` | Gera msg_followup pra leads `enviado` 72h+ sem resposta. Volta status pra `novo`. |
| Segunda 08:00 | `/api/cron/cleanup` | Descarta leads em `enviado` há 30+ dias com 2+ follow-ups |
| Real-time | `/api/manychat/inbound` | Webhook quando lead responde. Detecta hot keywords (preço, agendar, fechar, etc.) → muda status pra `quente` |

---

## 💻 O que tem no dashboard (foryou-leads.vercel.app)

### Páginas (atualizado 22/05):
- `/admin/campaigns` — Gerenciador de Campanhas: lista estilo Ads Manager + builder em seções
- `/admin/campaigns/[id]` — painel da campanha: captura + envio + "Enviar agora" + feed do job ao vivo (absorveu o antigo `/enviar`)
- `/atendimento` — fila de ação humana (leads respondeu/quente/agendou) — fusão do antigo `/hoje` + `/respostas`
- `/pipeline` — kanban por status (Novo → Enviado → Respondeu → Quente → Agendou → Cliente → Descartado)
- `/metricas` — métricas em abas (Geral + ROI por nicho), inclui breakdown por oferta
- `/videos` — biblioteca de vídeos locais (sync via worker)
- `/audios` — biblioteca de URLs de áudios padrão pra resposta manual
- `/lead/[id]` — detalhe individual (mensagens, histórico, dados)
- `/admin/ofertas` — catálogo de Ofertas (produtos vendáveis configuráveis)
- `/admin/users` — CRUD usuários · `/admin/apify-usage` — custo Apify

Rotas antigas (`/enviar`, `/hoje`, `/respostas`, `/metricas/nichos`) redirecionam pras novas.

### Lead card features
- Foto de perfil + nome + @ + cidade + score colorido
- Pain point destacado
- Tags editáveis + notas auto-save (debounce 700ms)
- Mensagens V1/V2/V3 + msg_unified + msg_followup expansíveis
- Botão "Abrir IG + Copiar" (envio manual rápido)
- Snooze 3/7/30/90 dias
- Bulk actions (status, snooze, tags)

### Auth
- Login via código Telegram OTP (sem senha)
- Cookie `foryou_session` (Middleware protege)

---

## 🚀 Worker AdsPower (executor de DMs)

`scripts/worker-adspower.mjs` — roda na máquina do Wilson, hidden via VBS na pasta Startup do Windows.

**Fluxo**:
1. Polls API a cada 5s pra ver se tem job
2. Quando tem: chama AdsPower API → abre profile `k1cn2qmx`
3. Pra cada lead na fila:
   - Navega pro perfil
   - Clica em "Enviar mensagem" → expande mini chat pra full DM
   - Digita mensagem letra-por-letra (45-140ms/char, pausas após pontuação)
   - Aperta Enter
   - Espera 5s
   - Anexa vídeo local (`scripts/videos/`)
   - Aguarda processamento + clica Enviar
   - Verifica que `<video>` apareceu na conversa (detecção de envio real)
   - Espera 3-8 min aleatórios
4. Snooze 3 dias automático
5. Reporta progresso em tempo real pro dashboard via heartbeats

**Features de robustez (já implementadas)**:
- `typeHumanInPage` via JS injetado (bypass de race conditions)
- `findInput` com scoring inteligente (prefere composer, penaliza Notes/Status)
- `expandMiniChat` com 3 estratégias cascata (DOM → header link → Vision)
- `clickSendButton` estrito (aria-label exato) com Vision fallback
- `ensureInThread` (volta pra conversa se sair)
- CSP bypass + file picker intercept via CDP
- Servidor HTTP local pra vídeos > 50MB (bypassa limite do CDP)
- Auto-cleanup de jobs travados (no startup + heartbeat 30s timeout)
- SIGINT handler marca job atual como failed

---

## ✅ O que JÁ funciona hoje

- Captação automática diária
- Análise por Claude com score 0-100
- Geração de msg_unified personalizada (CTA hardcoded — variar isso é Fase 1 do roadmap)
- Pipeline / Hoje / Pipeline UI
- Métricas
- Worker AdsPower com envio real (texto + vídeo)
- Recovery automático se sai da conversa
- Detecção de envio real (poll DOM)
- Webhook inbound do ManyChat
- Crons (apify, morning brief, follow-up, cleanup)
- Telegram notificações
- Biblioteca de vídeos local

---

## 🚨 Riscos conhecidos hoje (vide roadmap)

1. **CTA do vídeo é hardcoded** — todos DMs usam frase idêntica → padrão fácil pro IG detectar
2. **Webhook ManyChat sem HMAC** — qualquer um pode hitar e poluir DB
3. **Sem detecção de "Action Blocked"** — worker continua mandando mesmo após IG sinalizar
4. **Sem audit log** de status changes — drop de conversion = mistério
5. **Sem backup do Neon** — banco vai pro chão = perde tudo
6. **CRON_SECRET único** — vazou, perdeu tudo
7. **Sem rate limit em endpoints** — `/api/auth/start` é spammável
8. **Sem rotação de vídeo** — mesmo MP4 sempre = fingerprint detectável
9. **Sem warm-up de conta** — DMs disparados sem "atividade humana" prévia

→ **Roadmap completo de mitigações: [[ForYou Leads — Roadmap Pós-Auditoria]]**

---

## 📊 Estrutura do banco (Neon Postgres)

### Tabelas principais:
- `leads` — perfis capturados, com status, score, mensagens, tags
- `lead_messages` — histórico inbound (manychat) + outbound (a implementar)
- `lead_status_changes` — (a criar) audit log
- `campaigns` — hashtags + filtros + ativa/pausada
- `send_jobs` — jobs de envio (pending/running/done/cancelled/failed)
- `videos` — biblioteca de vídeos locais (sync via worker)
- `users` — equipe
- `sessions` + `auth_codes` — auth Telegram
- `ab_test_state` — A/B test V1/V2/V3
- `metrics_daily` — contadores diários

### Migrations rodadas:
- 001 init
- 002 features
- 003 tier2 (tags, notes, snooze, followup)
- 004 tier3 (auth telegram, ab test, whatsapp)
- 005 profile_pic_url
- 006 send_jobs
- 007 videos + msg_unified
- 008 local_videos

### Migrations no roadmap:
- 009 multi_default_videos
- 010 worker_state
- 011 audit_log
- 012 webhook_dedup
- 013 account_health
- 014 reply_templates
- 015 lead_revenue
- 016 copy_ab
- 017 message_sentiment
- 018 client_lifecycle

---

## 🛣 Histórico de mudanças significativas (2026-05)

### 14 mai — Stack original
Apps Script + Google Sheets + Apify + Claude API + ManyChat manual.

### 15-17 mai — Migração pra Next.js
- Reescrita completa pra Next.js 15 + Vercel + Neon
- Dashboard moderno (dark, glassmorphism)
- Auth Telegram OTP
- Crons no Vercel
- Webhook ManyChat
- Pipeline visual (Hoje / Pipeline / Lead detail)
- Métricas
- Bulk actions, filtros, tags, notas

### 17-18 mai — Sistema de envio automatizado
- Tabela `send_jobs`
- Página `/enviar` com preview + Iniciar
- Tentativas várias: Chrome extension (CORS issue) → Vercel Blob upload (4.5MB limit) → workers locais
- Worker AdsPower escolhido como caminho final
- Múltiplas iterações pra detecção de bloqueio, digitação humana, anexo de vídeo
- Claude Vision como fallback inteligente quando DOM não acha elementos
- Migração de vídeo cloud (Vercel Blob com CORS) pra local file path (worker scaneia pasta)

### 18 mai — Auditoria + roadmap
- Identificadas 55 melhorias (5 fases)
- Variação de mensagem virou prioridade absoluta
- Plano detalhado em [[ForYou Leads — Roadmap Pós-Auditoria]]

### 19-20 mai — Roadmap Fases 1-5
- Fases 1-4 (sobrevivência IG, reliability, UX, inteligência) deployadas
- Fase 5 Multi-vendedor: Wilson admin + Marco + Eduardo operators

### 22 mai — Multi-produto + Gerenciador de Campanhas
- **Sistema de Ofertas**: produto vendido virou catálogo `offers` configurável; IA parametrizada por oferta (migration 021)
- **Gerenciador de Campanhas**: campanha como objeto completo, estilo Ads Manager; `/enviar` absorvido pelo painel da campanha (migration 022)
- **Corte de redundância**: `/hoje`+`/respostas`→`/atendimento`; métricas em abas
- Fix: login do Wilson (conta estava inativa); Marco/Eduardo/Wilson todos admin

---

## 🧠 Aprendizados-chave (dor → solução)

1. **Vercel é serverless** — não pode controlar AdsPower remotamente. Worker tem que rodar local com IP residencial do Wilson.
2. **Instagram detecta IPs de datacenter** — qualquer DM partindo de Vercel/AWS = ban em horas.
3. **Mini chat do IG só aceita imagens** — pra mandar vídeo precisa expandir pra `/direct/t/THREAD_ID` (DM completo).
4. **Playwright via CDP tem limite de 50MB** pra `setInputFiles` — vídeos maiores precisam de HTTP server local + DataTransfer.
5. **CSP do Instagram bloqueia fetch de localhost** — precisa `Page.setBypassCSP` via CDP.
6. **AdsPower API V2 não exige API key se "Verificação de API" estiver OFF** — boa pra simplificar setup.
7. **`setInputFiles` com botão "Adicionar foto" clicado abre o Explorer do Windows** — solução: não clica no botão, atribui o input direto via marca em DOM.
8. **Heartbeat refresh no poll era bug crítico** — fazia jobs órfãos aparecerem vivos pra sempre, bloqueando novos.
9. **`:has-text()` é fuzzy** — pega substring. Pra "Mensagem" exato, usar `:text-is()`.
10. **`document.execCommand("insertText")` é deprecated mas é o único jeito de inserir em editor Lexical do Instagram** disparando os eventos React certos.
11. **Vercel function tem limite de 4.5MB** no body — uploads grandes precisam ser direto do browser pro destino (não passar pelo Next.js).
12. **Vercel Blob v2.x tem CORS issue com subdomínios `.vercel.app`** — voltamos pra v0.27 OU abandonamos cloud upload de vídeo.
13. **PostgreSQL não consegue inferir tipo de parâmetro `$x` quando aparece 2x na mesma SQL com NULL** — solução: branchear o SQL pra incluir/excluir a coluna conforme se foi passada.

---

## 🔗 Links rápidos

- App: https://foryou-leads.vercel.app
- Repo: ~/Projects/foryou-leads (local)
- Vercel: https://vercel.com/dashboard
- Neon: https://console.neon.tech
- Apify: https://console.apify.com
- ManyChat: https://app.manychat.com
- Roadmap completo: [[ForYou Leads — Roadmap Pós-Auditoria]]

---

## 📋 Status atual + próximos passos

**Status agora**: sistema em produção, mandando DMs reais. Testes confirmaram texto + vídeo enviados pra leads reais.

**Próximo passo**: começar Fase 1 do [[ForYou Leads — Roadmap Pós-Auditoria]], priorizando:
1. Variação de mensagem (1.1)
2. Detecção de bloqueio do IG (1.3)
3. HMAC no webhook ManyChat (1.6)

Resto da Fase 1 (rotação de vídeos, warm-up, janela horária, backup) em sequência.

---

## 📂 Caminhos de arquivos relevantes

| Caminho | Conteúdo |
|---------|----------|
| `~/Projects/foryou-leads/app/` | Next.js routes + páginas |
| `~/Projects/foryou-leads/lib/claude.ts` | Prompts Claude (analyze, vendedora, findElementInImage) |
| `~/Projects/foryou-leads/lib/send-queue.ts` | Pick logic da fila de envio |
| `~/Projects/foryou-leads/scripts/worker-adspower.mjs` | Worker principal |
| `~/Projects/foryou-leads/scripts/videos/` | Vídeos locais |
| `~/Projects/foryou-leads/sql/` | Migrations SQL |
| `~/Projects/foryou-leads/middleware.ts` | Auth middleware |
| `~/Projects/foryou-leads/vercel.json` | Cron schedule |

---

## 🎯 Métricas de sucesso (atualizar conforme operar)

### Cenário base (meta)
- 15-30 DMs/dia
- 15% taxa de resposta → 2-4 respostas/dia
- 40% interesse → 1-2 interessados/dia
- 30% fechamento → ~5-10 clientes/mês

### Custo unitário (estimativa)
- ~$1-2 por lead captado e processado
- ~$15-30 CAC (custo por cliente)

---

> Sessão de auditoria completa em 18-05-2026. Sistema operacional, roadmap claro pra evolução. Variação de mensagem é a urgência número 1.
