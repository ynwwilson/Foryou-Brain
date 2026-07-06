---
projeto: LocaMotoFácil — Agente WhatsApp
nota: Deploy, Acessos e Segredos
aviso: NÃO contém valores de chaves/tokens. Só onde eles vivem.
---

# Deploy, Acessos e Segredos

## Código / backup
- Local: `C:\Users\ynwwi\Projects\whatsapp-ai-agent` (branch `build-b`)
- **GitHub privado:** https://github.com/ynwwilson/whatsapp-ai-agent (remote `origin`, conta `ynwwilson`, gh autenticado por PAT no keyring). `.env` **não** sobe (gitignored). Push: `git push origin build-b`.

## URLs em produção
| O quê | URL |
|------|-----|
| Painel | https://waa-panel.vercel.app |
| Login painel | https://waa-panel.vercel.app/login |
| Gateway (webhook) | https://waa-gateway.ynwwilson.workers.dev/webhook |
| Brain (interno) | https://waa-panel.vercel.app/api/brain/process |

## Login do painel
- Email: `ynwwilson@gmail.com` **ou** `guilhermepcamargo@gmail.com`
- Senha: `99511638Ab` (mesma pros dois; signup desligado, só esses 2 entram)

## Vercel (painel + brain)
- Projeto: `waa-panel` · scope/team: `yngomesmarco-hues-projects` (Pro)
- Conta CLI logada: `ynwwilson-9617`
- **Root Directory = apps/panel** (config no dashboard — monorepo instala na raiz)
- Cron `/api/cron/proactive` a cada 15min (vercel.json em apps/panel)
- **29 env vars** em Production (chaves, modelos, supabase, whatsapp, BRAIN_SHARED_SECRET, CRON_SECRET, etc)
- Deploy: `vercel deploy --prod --yes --scope yngomesmarco-hues-projects` (da RAIZ do repo)

## Cloudflare (gateway)
- Worker: `waa-gateway` · conta `ynwwilson@gmail.com` (id `64f87e0d24c915cc2dbd50376712a030`)
- Durable Object: `ConversationDO`
- 4 secrets: WHATSAPP_VERIFY_TOKEN, WHATSAPP_APP_SECRET, BRAIN_URL, BRAIN_SHARED_SECRET
- Deploy: `cd apps/gateway && npx wrangler deploy` (wrangler já autenticado por OAuth)

## Supabase
- Projeto: "Agent Locamoto" · ref `mubvbtouuimqypwlyjqe` · org ForyouCode Pro
- Dashboard SQL: https://supabase.com/dashboard/project/mubvbtouuimqypwlyjqe/sql/new
- Migrations 0001–0008 **rodadas**. RLS single-owner via `panel_users` (2 donos seedados).
- Editor Monaco aceita injeção via dev-browser: `window.monaco.editor.getModels()[0].setValue(sql)` + Ctrl+Enter; confirmar modal "destructive" com "Run query".

## Meta (WhatsApp)
- App: "ai agent locamoto" · app id `1485290780011719` · business id `1590796992102932`
- Número de TESTE: **+1 555 636 0545** · phone_number_id `1053813234491361` · WABA id `26899764646359452`
- Webhook ativo (fields messages + message_template_status_update)
- Dono logado no Opera (developers.facebook.com / business.facebook.com)

## Onde vivem os SEGREDOS (valores NÃO ficam aqui)
- **`.env` do repo:** `C:\Users\ynwwi\Projects\whatsapp-ai-agent\.env` — TODAS as chaves reais (OpenAI, Anthropic, Groq, Meta x8, Supabase, BRAIN_SHARED_SECRET, CRON_SECRET, ALERT_THRESHOLD_USD, OWNER_EMAIL). **Gitignored** (não vai pro git).
- **Vercel env (Production):** mesma coisa, setado via `vercel env add`.
- **Cloudflare secrets:** os 4 acima.
- **Arquivos .txt de credenciais do dono:** `C:\Users\ynwwi\Projetos\IAs API.txt`, `locamoto supabasse.txt`, `meta-ai-agent-locamoto-credentials.txt`.
- **SGRLock:** `SGRLOCK_USER` / `SGRLOCK_PASSWORD` — AINDA NÃO existem (esperando Odeen). Base URL já no código.

## Segurança / pendências
- Os 5 arquivos .env/.txt originais tinham segredos vivos duplicados em texto puro (OpenAI, GitHub, Vercel, Cloudflare, Supabase, Neon, Telegram, ManyChat) → **mandei rotacionar**. Verificar se foi feito.
- Chaves dedicadas novas (OpenAI/Anthropic/Groq) criadas pelo dono pra este projeto.
