---
data: 2026-05-20
hora: 05h57
tipo: sessão de implementação
projeto: ForYou Leads — Fase 5 Multi-vendedor (Adaptive-Ember)
duração: ~6h
---

# 2026-05-20 05h57 — Fase 5 Multi-vendedor: código completo, deployado, users criados

## O que foi feito

Implementação completa da Fase 5 do ForYou Leads — multi-vendedor (Wilson admin + Marco operator + Eduardo operator).

### Código (8 commits em `feat/multi-user`, merged em `main`)

1. **Commit 1 — Migration 019 + types** (`sql/019_multi_user.sql`, `lib/types.ts`)
   - 5 colunas novas em `users`: `telegram_bot_token`, `telegram_bot_username`, `adspower_profile_id`, `test_lead_ig_username`
   - Reusa colunas existentes: `users.telegram_chat_id`, `users.active`, `users.ig_handle`
   - Ownership: `campaigns.assigned_to_user_id`, `send_jobs.created_by`, `videos.owner_user_id`
   - Tudo additive + nullable + IF NOT EXISTS

2. **Commit 2 — Backend helpers + auth/whoami**
   - `lib/users.ts`: `getUserByEmail`, `getUserById`, `getAdminUser`, `getUsersActive`, `getOwnerOrAdmin`
   - `app/api/auth/whoami/route.ts`: modo session (browser) OU worker (bearer + X-Worker-User-Email)
   - `lib/telegram.ts` refator: `sendTelegramToUser(userId, text)` com fallback global. `dispatch()` helper. Todos `notifyXxx` aceitam `userId?` opcional
   - `lib/auth.ts`: `sendLoginCode` aceita `botToken?` opcional. `auth/start` passa `user.telegram_bot_token` (Marco/Eduardo já interagiram com bot próprio, não o global)

3. **Commit 3 — UI admin**
   - `/admin/users` form completo com 4 campos novos + botão "Testar bot" (pinga `getMe` + envia teste)
   - `/admin/campaigns` com select de owner + dono visível em cada card
   - APIs `/api/users` e `/api/campaigns` aceitam novos campos

4. **Aplicar migration + backfill (manualmente)**
   - `npm run migrate` aplicou 019 em prod
   - Backfill: 142 leads + 4 campaigns + 13 send_jobs + 1 video atribuídos a Wilson (`1d19878f-579c-405f-80d0-bb584434ffa0`)
   - Counts pós-backfill: 0 nulls em todos

5. **Commit 4 — Telegram webhook multi-bot + ManyChat per-user**
   - `/api/telegram/webhook?user_email=` salva chat_id em `users.telegram_chat_id` do user certo; usa bot dele pra responder. Sem param: modo legacy (config_kv)
   - `/api/manychat/inbound`: notifica bot do `lead.assigned_to` (não mais o global). Novo lead inbound → atribuído ao admin

6. **Commit 5 — Worker per-user + endpoints filtering**
   - `lib/worker-auth.ts`: `authorizeWorker(req)` — secret + header `X-Worker-User-Email`. Fallback admin se sem header (zero-downtime)
   - `scripts/worker-adspower.mjs`: lê `WORKER_USER_EMAIL`, helper `apiHeaders()` injeta header, startup chama `/api/auth/whoami` pra validar
   - Endpoints filtrados por `created_by = user.id`: `cron/send/{poll,progress,block,cleanup}`, `cron/videos/sync`, `send/start`, `send/test`
   - `lib/send-queue.ts`: `fetchSendQueue(limit, assignedToUserId?)` filtra por dono

7. **Commit 6 — UI privacy**
   - `lib/lead-auth.ts`: `authorizeLeadAccess(leadId)` — 403 se operator não é dono
   - Aplicado em `/api/leads/[id]/{status,notes,tags}`
   - Páginas `/pipeline`, `/hoje`, `/respostas` filtram `assigned_to = me.id` se não-admin
   - `/lead/[id]/page.tsx` mostra 403 amigável se não dono
   - `sidebar.tsx` esconde `/admin/*` pra não-admin + mostra "👑 admin" ou "👤 operator"
   - `/admin/campaigns` ganhou check de admin (não tinha)

8. **Commit 7 — Apify per-campaign + crons per-user**
   - `cron/apify`: loopa **todas** campanhas ativas (não LIMIT 1). 5 hashtags por campanha (era 10). Insere lead com `assigned_to = campaign.assigned_to_user_id`. Notifica dono no bot pessoal por campanha
   - `cron/weekly-digest`: loop por user ativo, payload filtrado por `assigned_to`, manda no bot pessoal. Pula operator sem atividade na semana
   - `cron/morning-brief`: idem (per-user)
   - `cron/followup`: agrupa por owner, manda contagem no bot do dono
   - `cron/account-health`: loop por users com `ig_handle`. 1 snapshot por user. Alerta no bot pessoal se queda > 5%. Fallback legacy se nenhum user
   - `cron/score-insights`: mantém global (agregação). Manda só pro admin

9. **Commit 8 — Setup script + 5 docs**
   - `scripts/setup-worker.mjs` (`npm run setup:worker`): interativo, valida whoami + AdsPower, salva `.env.local`
   - Docs em `brain/`: multi-user-architecture, admin-criar-user, onboarding-marco-mac, onboarding-eduardo-windows, bot-telegram-setup

### Deploy + dados

- Branch `feat/multi-user` push + PR #1 (`https://github.com/ynwwilson/foryou-leads/pull/1`)
- Merged em `main` com `--no-ff`. Vercel auto-deployou + `vercel --prod` confirmou.
- Deploy `dpl_ACQmwf6D49KNYWU2Dd2dTeZZrvh5` → `foryou-leads.vercel.app`
- `whoami` validado em prod (200, retorna Wilson admin)
- INSERT users via SQL direto:
  - Marco: id `7ecf8de3-3a2f-4605-8928-ae28a7de6537`, operator, bot `@gomesmarcoleads_bot`, chat_id `8654690285`, profile `k1cnbr5n`, IG `gomesmarco._`
  - Eduardo: id `0d849094-077e-43f5-baab-c3e26271683e`, operator, bot `@PaiDoJose_bot`, chat_id `8596813900`, profile `k1cnbrrg`, IG `eduaardoqz._`
- Webhooks Telegram configurados nos 2 bots com `?user_email=` correto
- 1 campanha inicial inativa pra cada operator (Wilson ativa quando worker rodar)
- Wilson DB atualizado: `ig_handle=ynwwilson`, `adspower_profile_id=k1cn2qmx`
- Wilson `.env.local` local atualizado: `WORKER_USER_EMAIL=wilsonads.ia@gmail.com`, `ADSPOWER_PROFILE_ID=k1cn2qmx`

## Decisões tomadas

| # | Decisão | Escolha |
|---|---|---|
| 1 | Migration 019 timing | Aplicar entre Commit 3 e Commit 4 (depois UI admin, antes worker per-user) |
| 2 | OTP via bot global | Refinada na implementação: usa **bot do user se tem token**, senão fallback global. Marco/Eduardo recebem OTP no bot pessoal (chat_id veio dessa interação) |
| 3 | Apify hashtags | 5 por campanha × N campanhas (era 10×1). `maxDuration: 300` mantido |
| 4 | Docs formato | Markdown puro com comandos copiáveis |
| 5 | Branch | `feat/multi-user` + PR #1 antes de merge |
| 6 | Deploy | `vercel --prod` autorizado e executado |
| 7 | Backfill | Wilson como dono de todos os 142 leads existentes |
| 8 | Worker auth backward compat | Header ausente → fallback admin (zero downtime no deploy) |

## Estado atual

**Infraestrutura prod:**
- App `foryou-leads.vercel.app` rodando código novo
- DB Neon com migration 019 aplicada + backfill
- 3 users ativos: Wilson admin, Marco operator, Eduardo operator
- 2 webhooks Telegram per-bot configurados
- Bot global continua funcionando pra OTP de users sem bot próprio

**Wilson:**
- `.env.local` local atualizado com WORKER_USER_EMAIL
- Worker antigo precisa restart pra carregar nova env (ou continua com fallback admin sem header — funciona mas perdeu o "✓ Logado como Wilson")

**Marco/Eduardo:**
- Logam no app, veem 0 leads (correto, campanhas inativas)
- Workers ainda NÃO rodam no PC deles — falta o passo TeamViewer

## Próximos passos

### Wilson — restart worker local (1 min)

No PC do Wilson:
1. Ctrl+C no terminal onde worker está rodando
2. `cd C:\Users\ynwwi\Projects\foryou-leads`
3. `rtk git pull origin main` (puxa código novo)
4. `node scripts/worker-adspower.mjs`
5. Log esperado: `✓ Logado como Wilson (admin) — profile k1cn2qmx`

### Wilson — TeamViewer no Mac do Marco

Abre TeamViewer no Mac do Marco, cola no Terminal:

```bash
mkdir -p ~/Projects && cd ~/Projects && \
  (git clone https://github.com/ynwwilson/foryou-leads.git || (cd foryou-leads && git pull)) && \
  cd foryou-leads && npm install && npx playwright install chromium && \
  cat > .env.local <<'EOF'
API_BASE=https://foryou-leads.vercel.app
CRON_WORKER_SECRET=ab3bc2d004c5ce8aabd06417a7c25d70ec4ef9cb82f82fbe4b6b139162f6ae6f
WORKER_USER_EMAIL=ygomesmarco@gmail.com
ADSPOWER_PROFILE_ID=k1cnbr5n
EOF
  echo "" && echo "✅ Setup OK. Pra rodar worker:" && echo "  node scripts/worker-adspower.mjs"
```

Depois confirma que AdsPower está aberto + roda `node scripts/worker-adspower.mjs`.

### Wilson — TeamViewer no Windows do Eduardo

No Git Bash (não PowerShell):

```bash
mkdir -p ~/Projects && cd ~/Projects && \
  (git clone https://github.com/ynwwilson/foryou-leads.git || (cd foryou-leads && git pull)) && \
  cd foryou-leads && npm install && npx playwright install chromium && \
  cat > .env.local <<'EOF'
API_BASE=https://foryou-leads.vercel.app
CRON_WORKER_SECRET=ab3bc2d004c5ce8aabd06417a7c25d70ec4ef9cb82f82fbe4b6b139162f6ae6f
WORKER_USER_EMAIL=romarionazario36@gmail.com
ADSPOWER_PROFILE_ID=k1cnbrrg
EOF
  echo "" && echo "✅ Setup OK. Pra rodar worker:" && echo "  node scripts/worker-adspower.mjs"
```

### Validação final (Gate 2 do plano)

1. Cada operator loga em `foryou-leads.vercel.app` (OTP no bot pessoal dele)
2. Wilson ativa campanha do Marco em `/admin/campaigns`
3. Próximo cron Apify (ou disparo manual via `curl ".../api/cron/apify?key=$CRON_SECRET"`) atribui leads novos ao Marco
4. Marco em `/pipeline` agora vê os leads dele
5. Marco em `/enviar` → 3 DMs teste → DM real sai pelo IG dedicado dele
6. Lead responde → notificação chega em `@gomesmarcoleads_bot` (não no bot do Wilson)
7. Repete pra Eduardo

## Riscos residuais

- **Worker antigo do Wilson:** se ele não restartar, continua funcionando via fallback admin (sem `X-Worker-User-Email` header). Esperado vai dar warning na log do `whoami` no startup mas worker segue.
- **Marco/Eduardo precisam aquecer conta IG:** se IG dedicada de algum deles não foi aquecida mínimo 1 semana com posting/follows manuais, bloqueio em horas.
- **Campanha do Marco/Eduardo está com hashtags genéricas** (`empreendedorismo`, `marketingdigital`, `agenciademarketing`). Wilson refina antes de ativar.

## Artefatos

- PR: https://github.com/ynwwilson/foryou-leads/pull/1
- Plano executado: `C:\Users\ynwwi\.claude\plans\sim-bright-codd.md`
- Plano-mãe (770 linhas): `C:\Users\ynwwi\.claude\plans\vamos-para-a-fase-adaptive-ember.md`
- Docs novos: `brain/multi-user-architecture.md`, `brain/admin-criar-user.md`, `brain/onboarding-marco-mac.md`, `brain/onboarding-eduardo-windows.md`, `brain/bot-telegram-setup.md`
- Migration: `sql/019_multi_user.sql`
- Roadmap atualizado: [[ForYou Leads — Roadmap Pós-Auditoria]]

## Métricas

- 8 commits (+1 chore gitignore)
- ~2300 linhas adicionadas, ~700 removidas
- 1 migration (additive)
- 12 arquivos novos
- ~30 arquivos modificados
- 0 dependências novas
- Typecheck zero erros em cada commit
- Tempo dev real: ~6h (estimado original: 3-4h — extra tempo gasto refinando filtros per-user + cron loops)

Relacionado: [[ForYou Leads — Roadmap Pós-Auditoria]], [[Pipeline de Leads ForYou]]
