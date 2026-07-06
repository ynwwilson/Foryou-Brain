# 16 — Setup e Credenciais

> Voltar ao [[AG Estofados — Índice]]
>
> Checklist executável de tudo que precisa ser conectado, criado e configurado pra o projeto rodar. Status vivo em [[17 - Status do Projeto (Live)]].

## ⚠️ Segurança em primeiro lugar

**✅ Resolvido em 2026-05-22:**

- Os 3 arquivos `.txt` com chaves em `C:\Users\ynwwi\Projetos\` foram renomeados pra `.env` real:
  - `foryoucode.env.txt` → `foryoucode.env`
  - `envs2.0.txt` → `envs2.0.env`
  - `env infinitycontent.txt` → `infinitycontent.env`
- `.gitignore` global criado em `C:\Users\ynwwi\.gitignore_global` e registrado via `git config --global core.excludesfile`; `.gitignore` local também criado em `C:\Users\ynwwi\Projetos\`. Os padrões `*.env*` cobrem todos os arquivos de credenciais.

**⚠️ Pendente — ação do Mestre:**

- **Rotacionar as chaves expostas** (GitHub, Vercel, Cloudflare, Anthropic) — trafegaram em conversa. Gerar novas nos dashboards e atualizar os `.env`. Enquanto não rotacionar, considere as chaves antigas comprometidas.

## Tier 0 — Agora (sem isso eu não começo)

| # | Item | Onde pegar | Formato | Custo | Status |
|---|---|---|---|---|---|
| 1 | **Lovable MCP** | Claude Code → Settings → Connectors → URL `https://mcp.lovable.dev` | OAuth | Incluso Pro | ⚠️ Pendente |
| 2 | **GitHub PAT** | https://github.com/settings/tokens (classic, scope `repo, workflow, read:org, write:packages`) | Token `ghp_...` | R$ 0 | ✅ Tem (válido, login `ynwwilson`) |
| 3 | **Vercel Token** | https://vercel.com/account/tokens (Full Account, no expiration) | Token | R$ 0 | ✅ Tem (user `yngomesmarco-hue`) |
| 4 | **Cloudflare API Token** | https://dash.cloudflare.com/profile/api-tokens (escopo Workers + Pages + R2 + Stream + DNS) | Token | R$ 0 | ✅ Tem (account `64f87e0d...`, 10 zones) |
| 5 | **Banco — Neon ou Supabase ou Schema novo** | [[17 - Status do Projeto (Live)#Conflito do banco]] | URL + Key | R$ 0 | ⚠️ Pendente decisão |
| 6 | **Registrar `agestofados.com.br`** | https://registro.br | Login Registro.br | ~R$ 40/ano | ⚠️ Pendente |

## Tier 1 — Essa semana (libera geração cinematográfica)

### A. APIs de geração de mídia

| # | Item | Onde pegar | Pra quê | Custo |
|---|---|---|---|---|
| 7 | **GEMINI_API_KEY** | https://aistudio.google.com/apikey | Veo 3, Imagen 4, Nano Banana via código | Incluso no Gemini Advanced |
| 8 | **OPENAI_API_KEY** | https://platform.openai.com/api-keys | Sora 2, GPT-Image-1, GPT-4o Vision | Pré-pago $20 |
| 9 | **ELEVENLABS_API_KEY** | https://elevenlabs.io (Starter $5/mês) | Voz IA, narração, voz clonada | $5/mês |
| 10 | **REPLICATE_API_TOKEN** (opcional) | https://replicate.com/account/api-tokens | Modelos open: Flux Pro, Stable Video, Real-ESRGAN | Pré-pago $10 |
| 11 | **RESEND_API_KEY** | https://resend.com (free 3k emails/mês) | E-mail transacional do form | R$ 0 |

### B. Skills anti-slop (instalar localmente)

| # | Skill | Comando |
|---|---|---|
| 12 | **Taste** | `git clone https://github.com/leonxlnx/taste-skill ~/.claude/skills/taste` |
| 13 | **UI/UX Pro Max** | Clone do repo + copiar skill interno |
| 14 | **Impeccable** | `npx impeccable install` no projeto |
| 15 | **Huashu-Design** | `npx -y @huashu-design/cli install` |
| 16 | **Playwright skill** | `git clone https://github.com/lackeyjb/playwright-skill ~/.claude/skills/playwright-skill` |

### C. Software local

| # | Item | Onde pegar | Pra quê | Custo |
|---|---|---|---|---|
| 17 | **Polycam** (iPhone) | App Store | Fotogrametria das peças AG + tour 360 da loja | Free ou $8/mês Pro |
| 18 | **Blender** | https://www.blender.org/download/ | Limpar mesh 3D antes do Spline | R$ 0 |
| 19 | **Topaz Photo AI** (opcional) | https://www.topazlabs.com/topaz-photo-ai | Upscale 4K fotos do Insta | License ~$199 ou Magnific via API |
| 20 | **ffmpeg** | https://ffmpeg.org/download.html (Windows binary) | Manipulação de vídeo via terminal | R$ 0 |

### D. Fontes premium

| # | Item | Onde pegar | Custo |
|---|---|---|---|
| 21 | **PP Editorial New** | https://pangrampangram.com/products/editorial-new (trial gratuito uso pequeno) | R$ 0 trial / ~$80 commercial |
| 22 | **Migra** (alternativa) | https://pangrampangram.com/products/migra | Trial R$ 0 |
| 23 | **Inter** | https://fonts.google.com/specimen/Inter ou Fontsource | R$ 0 |
| 24 | **Cormorant Garamond** | https://fonts.google.com/specimen/Cormorant+Garamond | R$ 0 |

Baixar `.woff2` e `.ttf`. Colocar em `fontes/` no projeto.

## Tier 2 — Inputs da AG Estofados (cliente entrega)

| # | Item | Como pedir |
|---|---|---|
| 25 | Número WhatsApp oficial (com DDD) | Mensagem direta |
| 26 | E-mail oficial pra receber leads | Mensagem direta |
| 27 | Lista das 8–15 peças (nome + 1-2 frases) | Reunião curta com dono |
| 28 | 3–5 depoimentos reais (texto + autor + cidade + autorização escrita) | Pedir antes do ensaio |
| 29 | Horário de funcionamento | Mensagem direta |
| 30 | Acesso Google Business Profile (ou autorização pra reivindicar) | Acesso via Gmail |
| 31 | Material visual existente (fotos brutas, logo vetor) | WeTransfer / Drive |
| 32 | Autorização escrita pra usar nome/voz/imagem do dono | Documento simples (template no doc 18 futuro) |
| 33 | Data do ensaio fotográfico | Combinar com fotógrafo |

## Tier 3 — Quando escalar

| Item | Quando ativar |
|---|---|
| **HeyGen / D-ID API** | Avatar falante (Fase 7) |
| **WhatsApp Business Cloud API** | Atendimento IA (Fase 3) |
| **Sentry DSN** | Quando deploy estiver estável |
| **PostHog project key** | Quando começar A/B test |
| **Algolia / Meilisearch** | Após 30+ peças no catálogo |
| **Stripe / Mercado Pago** | Se entrar venda online |

## Como me passar as chaves com segurança

### Forma 1 — OAuth (zero risco)
MCPs (Lovable, Vercel, GitHub via gh CLI) → autoriza no browser, token fica local.

### Forma 2 — `.env` local (recomendado)
Criar `C:\Users\ynwwi\Projetos\ag-estofados\.env`:

```env
# Reaproveita da ForYou
GITHUB_PAT=<reusa>
VERCEL_TOKEN=<reusa>
CLOUDFLARE_API_TOKEN=<reusa>
CLOUDFLARE_ACCOUNT_ID=64f87e0d24c915cc2dbd50376712a030
CLOUDFLARE_ZONE_ID=<preencher após registrar domínio>
ANTHROPIC_API_KEY=<reusa>

# Banco (decidir A/B/C — ver [[17 - Status do Projeto (Live)]])
NEON_DATABASE_URL=<reusa ou nova>
NEON_DATA_API=<reusa ou nova>
# OU
SUPABASE_URL=<criar>
SUPABASE_SERVICE_ROLE_KEY=<criar>

# Mídia (criar hoje)
GEMINI_API_KEY=<trazer>
OPENAI_API_KEY=<trazer>
REPLICATE_API_TOKEN=<opcional>
ELEVENLABS_API_KEY=<opcional>

# E-mail
RESEND_API_KEY=<criar>
```

Leio via `ctx_execute` na hora de usar. Nunca exibo no chat. Nunca commito.

### Forma 3 — Colar no chat só na hora
Funciona, mais trabalho.

## Cronograma sugerido

```
HOJE (~1h do Mestre)
─────
☑ Renomear .env.txt → .env real + gitignore  (feito 2026-05-22)
□ Rotacionar chaves expostas (GitHub, Vercel, Cloudflare, Anthropic)
□ Decidir banco (A: Neon novo / B: schema separado / C: Supabase novo)
□ Registrar agestofados.com.br
□ Conectar Lovable MCP (OAuth)
□ Criar arquivo .env do projeto AG

ESSA SEMANA
───────────
□ Criar GEMINI_API_KEY
□ Criar OPENAI_API_KEY (pré-pago $20)
□ Criar RESEND_API_KEY (free)
□ Criar ELEVENLABS Starter ($5)
□ Criar REPLICATE (opcional)
□ Instalar 5 skills anti-slop
□ Baixar fontes PP Editorial New + Inter + Cormorant
□ Cobrar inputs da AG

INSTALAR LOCAL (uma vez)
────────────────────────
□ Polycam no iPhone
□ Blender no PC
□ ffmpeg
□ Topaz (opcional)
```
