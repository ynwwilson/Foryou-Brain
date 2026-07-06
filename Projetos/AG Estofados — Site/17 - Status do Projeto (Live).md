# 17 — Status do Projeto (Live)

> Voltar ao [[AG Estofados — Índice]]
>
> 🔴 **Documento vivo.** Atualizado a cada sessão. Snapshot do estado real do projeto.

**Última atualização:** 2026-05-22 (sessão Claude Code — correção de stack e segurança)

---

## Resumo executivo

- **Fase atual:** Pré-produção encerrada. Pronto pra disparar projeto Lovable.
- **Bloqueio principal:** 4 chaves API a criar + decisão de banco + conectar Lovable MCP.
- **Próxima ação:** Mestre cria GEMINI + OPENAI + RESEND keys, decide banco (A/B/C), conecta Lovable MCP.

---

## Decisões batidas (com data)

| Decisão | Data | Onde está |
|---|---|---|
| Conversão por WhatsApp + form, sem checkout | 2026-05-21 | [[01 - Briefing]] |
| Visual preto + dourado | 2026-05-21 | [[03 - Identidade Visual e Tom de Voz]] |
| Páginas de produto individuais, catálogo 8-15 peças | 2026-05-21 | [[02 - Arquitetura e Catálogo]] |
| Stack: **Lovable em TanStack Start** (não Astro, não Next puro) | 2026-05-21 | [[10 - Toolchain Premium e Workflow MCP#1]] |
| Banco: **Neon (não Supabase)** — mas decidir A/B/C abaixo | 2026-05-21 | Mestre confirmou |
| **D1 — Banco: Supabase ou Neon** — a stack suporta os dois (Postgres nos dois; ver [[10 - Toolchain Premium e Workflow MCP#6. Banco como CMS leve — Supabase ou Neon]]). Preferência atual: projeto **Neon** novo `ag-estofados`, isolado do ForYou Leads (Opção A) | 2026-05-21 | Mestre confirmou |
| Fontes: **PP Editorial New + Inter + Cormorant italic** | 2026-05-21 | [[09 - Design System — Fontes e Tokens]] |
| Tom: **afiado, manifesto, ofício** | 2026-05-21 | [[10 - Toolchain Premium e Workflow MCP#4.2]] |
| Animação: **GSAP 3.13 + Lenis + Spline + Framer Motion + Lottie** | 2026-05-21 | [[10 - Toolchain Premium e Workflow MCP#3]] |
| Vídeo: **B-roll gerado IA (Veo 3) no lançamento + filmagem real depois** | 2026-05-21 | Mestre confirmou |
| Copy afiado adaptado pro ofício | 2026-05-21 | [[06 - Conteúdo e Copy]] |
| Storytelling em 4 atos | 2026-05-21 | [[11 - Storytelling em 4 Atos]] |
| Pipelines P0 (#1-5) aprovados pro lançamento | 2026-05-21 | [[13 - Pipelines Generativos]] |
| 5 skills anti-slop entram no workflow | 2026-05-21 | [[15 - Skills Anti-Slop]] |
| Lovable Pro ativo (Mestre confirma) | 2026-05-21 | — |
| **Sem Telegram** pra notificação do AG | 2026-05-21 | Mestre confirmou |
| Domínio sugerido: `agestofados.com.br` | 2026-05-21 | Confirmar Registro.br |

## Decisões pendentes

| # | Decisão | Opções | Recomendação |
|---|---|---|---|
| D2 | **Repo GitHub: onde criar** | a) usuário `ynwwilson` · b) Org ForYou (verificar se existe) | Conferir org |
| D3 | **Visibilidade do repo** | Privado / Público | Privado até lançar |
| D4 | **Tier 2 Pipelines (#6-8 showroom virtual)** | Lançamento ou Fase 2 | Fase 2 |
| D5 | **Voz narrativa (#17 immersive)** | Lançamento ou Fase 2 | Fase 2 + autorização AG |

---

## Status dos tokens (testados em 2026-05-21)

| Token | Status | Detalhes |
|---|---|---|
| **GITHUB_PAT** | ✅ Funcional | Login `ynwwilson` |
| **VERCEL_TOKEN** | ✅ Funcional | User `yngomesmarco-hue`, email `yngomesmarco@gmail.com` |
| **CLOUDFLARE_API_TOKEN** | ✅ Funcional* | Account `64f87e0d24c915cc2dbd50376712a030`. 10 zones ativas. Endpoint `/user/tokens/verify` retorna 401 (escopo `User: Memberships, Read` falta) mas isso **não afeta** uso prático (DNS, Workers, R2, Stream funcionam) |
| **ANTHROPIC_API_KEY** | ✅ Funcional | 9 modelos disponíveis (Opus 4.7, Sonnet 4.6, Opus 4.6) |
| **NEON DATABASE_URL** | ✅ Conecta | `neondb` Postgres 17.10, 20 tabelas (ForYou Leads — ver conflito abaixo) |
| **NEON_DATA_API** | ⚠️ Auth | 400 missing credentials — precisa Bearer JWT (Neon Auth) ou token específico |
| **TELEGRAM_BOT_TOKEN** | ✅ Funcional (não usaremos no AG) | bot `foryouleadsbot` |
| **MANYCHAT_API** | ✅ Funcional (não usaremos no MVP) | — |

## Tokens a criar (Mestre)

| Token | Pra que | Status |
|---|---|---|
| **GEMINI_API_KEY** | Veo 3, Imagen, Nano Banana via código | ⚠️ Falta |
| **OPENAI_API_KEY** | Sora 2, GPT-Image-1, GPT-4o Vision | ⚠️ Falta |
| **RESEND_API_KEY** | E-mail do form | ⚠️ Falta |
| **ELEVENLABS_API_KEY** | Voz IA (Fase 2) | ⚠️ Opcional agora |
| **REPLICATE_API_TOKEN** | Modelos open | ⚠️ Opcional agora |

## MCPs a conectar (Mestre)

| MCP | Status |
|---|---|
| **Lovable** (`mcp.lovable.dev`) | ⚠️ Falta conectar (OAuth) |
| **Supabase** ou **Neon Tools** | Depende decisão D1 |
| **Vercel** (`mcp.vercel.com`) | ⚠️ Falta (claude.ai pode ter equivalente) |
| **Cloudflare** (oficial) | ⚠️ Falta (existe oficial) |
| **GitHub** (oficial) | Verificar se Composio cobre |
| **Sentry** | Quando ativar |
| **PostHog** | Quando ativar |
| **Playwright skill** | Quando instalar (Tier 1 setup) |

---

## ⚠️ Conflito do banco Neon

O `neondb` JÁ TEM 20 tabelas — todas do **ForYou Leads**:

```
_migrations, ab_test_state, audio_library, auth_codes, campaigns,
config_kv, ig_account_snapshots, lead_messages, lead_status_changes,
leads, metrics_daily, offers, rate_limit_events, score_predictions,
send_jobs, sessions, users, videos, webhook_dedup, worker_state
```

**Conflito**: a tabela `leads` já existe (ForYou Leads). Pra AG eu também precisaria criar `leads`.

**Opções (D1):**
- **A.** Criar **projeto Neon novo** `ag-estofados`. Free tier permite. Recomendado.
- **B.** Criar **schema separado** `ag` no `neondb` atual. Tabelas viram `ag.products`, `ag.leads`, `ag.testimonials`. Aceita pra MVP.
- **C.** Voltar pra Supabase. Mestre já disse Neon, então A/B.

**Recomendação: A.** Mestre cria em https://console.neon.tech → New Project → me passa nova DATABASE_URL.

---

## Tasks em aberto (criadas na sessão)

| ID | Subject | Status | Owner |
|---|---|---|---|
| 1 | Conectar Lovable MCP no Claude Code | pending | Mestre |
| 2 | Trazer GEMINI_API_KEY (Google AI Studio) | pending | Mestre |
| 3 | Trazer OPENAI_API_KEY (platform.openai.com) | pending | Mestre |
| 4 | Trazer RESEND_API_KEY (resend.com free) | pending | Mestre |
| 5 | Registrar agestofados.com.br no Registro.br | pending | Mestre |
| 6 | Criar tabelas no Neon (products, leads, testimonials) | pending | Claude (depende D1) |
| 7 | Criar repo GitHub ag-estofados | pending | Claude (depende D2) |
| 8 | Disparar projeto Lovable | pending | Claude (depende #1) |

---

## Backlog (Fase 2+)

- Tier 2 pipelines (showroom virtual #6-8)
- Tier 3 immersive interactions (#11 AR, #15 WebGL transitions, #17 voz, #18 modo bastidor)
- Pipelines P2 (#9 site auto-Insta, #10 blog SEO, #11 avatar IA, #12 memória visitante)
- Sentry + PostHog setup
- Migração pra Next.js (se necessária)

---

## Riscos ativos

| Risco | Mitigação |
|---|---|
| Lovable trava em animação complexa | Tudo de animação via Claude Code MCP, não no Lovable |
| Ensaio fotográfico atrasar | Plano B com fotos do Instagram upscaled |
| Cliente AG demorar inputs | Mestre cobra Fase 1 em paralelo ao setup técnico |
| Custo de geração explode (Veo, Sora, Magnific) | Budget de R$ 200 inicial pra P0; cap mensal pós |
| Lovable regenera arquivo e quebra animação | Convenção `// LOCKED — edit via Claude Code` |
| Conflito Neon ForYou Leads × AG | Decisão D1 acima |

---

## Próximas 5 ações concretas (em ordem)

1. **Mestre:** cria projeto Neon novo `ag-estofados` em https://console.neon.tech → me passa nova DATABASE_URL
2. **Mestre:** cria GEMINI + OPENAI + RESEND keys → coloca em `.env`
3. **Mestre:** conecta Lovable MCP
4. **Claude:** cria repo GitHub `ag-estofados` + roda schema no Neon novo
5. **Claude:** dispara projeto Lovable com prompt-sistema completo (todos os docs 01-16)

---

## Histórico de sessões

| Data | Sessão | Resultado |
|---|---|---|
| 2026-05-21 (13h52, Claude Nova) | Briefing inicial + análise Instagram AG + referência COCO HOME | Docs 01-04 criados |
| 2026-05-21 (sessão atual, Claude Code) | Fechamento de planejamento + toolchain + skills + pipelines + storytelling + setup | Docs 05-17 criados/atualizados, tokens testados |
| 2026-05-22 (Claude Code) | Correção de inconsistências: stack (Astro/Antigravity → Lovable/TanStack/Vercel), banco flexível Supabase **ou** Neon, segurança (`.env` renomeados + gitignore global/local) | Docs 04, 05, 10, 14, 16, 17, Índice atualizados |
