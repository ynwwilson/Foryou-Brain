---
tipo: plano-execucao
tags: [foryoucode, conteudo, infinity-content, painel, execucao, autonomo]
atualizado: 2026-06-10
status: ✅ EXECUTADO 2026-06-10 — painel no ar em https://infinity-painel.vercel.app
---

# ✅ ATUALIZAÇÃO 2026-06-11 — painel maduro

- **Página de insights por vídeo** `/videos/[id]` — clicável de Dashboard/Métricas/Conteúdo. KPIs reais vs média dos últimos 10, radar comparativo, funil do vídeo, **retenção REAL** (duração extraída do MP4 via parse `mvhd` + watch time → % média; curva segundo-a-segundo a Meta NÃO expõe), comentários reais + sentimento por IA, diagnóstico acionável, variações que geram roteiro no Telegram, timeline.
- **Análise IA automática**: sync a cada 15min enfileira `{kind:'analise'}` pra reels novos; página gera sozinha ao abrir se faltar. Zero clique.
- **Sync IG a cada 15min** (era 2×/dia) — corrige defasagem. Métricas estendidas (total_watch_s). Catálogo até 100 mídias.
- **Demografia real** por país via `follower_demographics`. Dashboard com período global (Hoje/7/14/30/90/Máx/custom), largura total, funil SVG suave, mapa pontilhado, globo 3D R3F.
- **Zero dado fictício** — tudo real ou marcado "sem fonte".
- Tabelas novas: `reel_analises`. Colunas: `reels.duration_s`, `metricas_reel.total_watch_s/profile_visits`.
- **Limitações honestas:** curva de retenção 2-a-2 (só TRIBE v2 resolveria); profile_visits/follows por reel a API recusa; receita sem fonte; 1 vídeo antigo saiu da listagem da Meta.

# ✅ RESULTADO DA EXECUÇÃO (2026-06-10)

- **Painel:** https://infinity-painel.vercel.app (Vercel, projeto `infinity-painel` em yngomesmarco-hues-projects). Login = senha definida pelo Mestre (`PANEL_PASSWORD`).
- **App Meta:** "Infinity Content Painel" id 1400970145249923, business ForYouCode (verificado). Permissões FB-login: basic/insights/publish/pages/business. Token long-lived 60d + IG_USER_ID (17841438240208105, @ynwwilson) como secrets do Worker. **Renovar token a cada ~60d** (aviso automático no TG <10d).
- **Métricas reais fluindo:** 1989 seguidores, 24 Reels com snapshots diários (cron 12h UTC + `/ig-sync` manual).
- **API REST:** ~25 rotas `/api/*` no Worker (auth PANEL_KEY). Endpoints debug: /ig-sync, /notify.
- **Validações E2E:** login, dashboard com dados reais (funil 1537→454→133→28→3→1), 5 páginas, POST via proxy, screenshots desktop+mobile OK.
- **Fase 4 embutida na v1:** multi-formato, dials, linter, hook arena, ângulos, agendamento (lembrete 15min), balanceador (radar), runway, busca, smart filters.
- **Fora (precisa App Review da Meta):** DM automática, inbox de comentários. **Reddit** segue 403 (OAuth pendente).
- **Gotcha env Vercel:** `echo | vercel env add` injeta \r\n — usar arquivo sem newline via `cmd /c "... < file"` (mesmo gotcha do wrangler secret).
- **Token IG quase-gotcha:** OAuth "Adicionar conta" (Instagram-login) trava sem papel de Instagram Tester; caminho que funcionou = permissões FB-login no caso de uso + Graph Explorer + OAuth direto na aba.

# Infinity Content — SUPER PLANO: Painel completo (execução autônoma)

> Plano pra MIM (Claude) executar do início ao fim SEM o Mestre, após confirmação única.
> A confirmação do Mestre a este plano AUTORIZA todas as ações externas descritas
> (criar app Meta, projeto Vercel, secrets, deploys, posts de teste no canal Telegram).
> EXCEÇÃO: 2FA da Meta — se pedir, alerto no Telegram e AGUARDO o Mestre confirmar.

## Recursos disponíveis
- **Dev Browser no Opera** (aberto, logado: Meta developers, Vercel, Cloudflare) — livre acesso pra ESTE projeto.
- **Senha de re-auth** (Meta etc): fornecida pelo Mestre no chat (não replicada aqui).
- **Senha do painel**: fornecida (vai virar secret `PANEL_PASSWORD`, nunca em código).
- **wrangler CLI** autenticado (Worker + D1 + secrets). **Vercel CLI** logado.
- **Vercel workspace:** `yngomesmarco-hue` — projeto NOVO lá (domínio *.vercel.app).
- **IG @ynwwilson:** JÁ profissional + Página vinculada (confirmado pelo Mestre).
- **LLM:** Anthropic only (fallback OpenAI segue 401 — risco aceito pelo Mestre).

## Guard-rails (invioláveis)
1. **NÃO tocar em NADA de outros projetos** — em Vercel/Cloudflare/Meta/GitHub, só criar recursos novos deste projeto ou editar `infinitycontent`. Nenhum projeto existente alheio é aberto/alterado.
2. **Telegram não pode quebrar** — toda mudança no Worker preserva os fluxos atuais; deploy só após `tsc` + teste dos endpoints existentes (`/health`, backlog-first).
3. Segredos só via `wrangler secret put` / Vercel env vars — nunca em código ou docs.
4. 2FA Meta → alerta no Telegram (`notifyOps`) + pausa SÓ a fase Meta; resto continua.
5. Cada fase termina com validação ao vivo + commit + aviso de progresso no canal Telegram.
6. Browser: agir só nas abas/sites do projeto (developers.facebook.com, vercel.com, dash.cloudflare.com, business.facebook.com). Não abrir e-mail/outras contas.

## Arquitetura final
```
[Painel Next.js no Vercel (yngomesmarco-hue) — *.vercel.app]
   │  login por senha (PANEL_PASSWORD) → cookie httpOnly
   │  rotas server-side proxy → nunca expõe keys no client
   ▼
[Worker infinitycontent (API REST nova /api/*, auth PANEL_KEY + CORS)]
   │            │
   ▼            ▼
[D1 (cérebro)] [Meta Graph API (insights + publish, app novo, token longo)]
   ▲
[Telegram bot — INTOCADO, mesmos fluxos; painel e bot compartilham o mesmo D1]
```

---

## FASE 0 — Pre-flight (15 min)
1. Dev Browser: abrir, confirmar Opera respondendo; checar sessões (vercel.com, developers.facebook.com, dash.cloudflare.com) sem agir.
2. `vercel whoami` + listar workspaces → confirmar acesso a `yngomesmarco-hue`.
3. `rtk git status` no infinitycontent (limpo); branch main.
4. Validar Worker vivo (`/health`) e D1 respondendo.
5. Avisar no canal Telegram: "🚧 começando a construção do painel — te aviso a cada fase".
**Falha aqui = paro e reporto.**

## FASE 1 — API REST no Worker (3-4h)
Tudo que o painel precisa, sem quebrar nada existente.

### 1.1 Auth + CORS
- Novo secret `PANEL_KEY` (gero forte). Middleware: rotas `/api/*` exigem `Authorization: Bearer PANEL_KEY`.
- CORS: origin do painel (defino após criar o projeto Vercel; começa com `*.vercel.app` do projeto).

### 1.2 Endpoints (REST JSON)
| Rota | O quê |
|---|---|
| GET /api/overview | KPIs: backlog, semana (saíram/gravados/taxa), custo estimado, content runway (dias de conteúdo pronto), saúde (últ. refill, fontes ok/fail, alertas recentes) |
| GET /api/items?status=&tag=&categoria=&fonte=&q=&page= | backlog/temas com filtros + busca |
| GET /api/items/:id | detalhe (raw_content, hook, histórico) |
| POST /api/items/:id/dossie | enfileira dossiê (mesma fila do TG) |
| POST /api/items/:id/feedback {signal, reason?} | gravei/pulei + motivo |
| POST /api/items/:id/descartar · /restaurar | soft-delete (lixeira) |
| GET /api/dossies?gravado=&page= | roteiros gerados (subabas Gravados/Não gravados/Postados) |
| GET /api/dossies/:id | conteúdo completo (roteiro/legenda/hashtags/capa) |
| POST /api/acoes/temas · /buscar {termo} · /roteiro {texto,url} · /refill | paridade Telegram |
| GET/POST/DELETE /api/exemplos | CRUD padrões (Feature D) |
| GET /api/aprendizado | afinidade por categoria/fonte/tópico + motivos de pulei agregados |
| GET /api/fontes | 12 fontes, status, itens/fonte (7d), última coleta |
| GET /api/funil | coleta→aprovado→carded→dossiê→gravado→postado (taxas) |
| GET /api/metricas/ig/conta · /reels | snapshots IG (Fase 3) |
| POST /api/reels/match {dossie_id, ig_media_id} | linkar Reel↔dossiê |
| GET /api/multiformato/:dossieId?formato=carrossel|thread|stories|outline | Estúdio multi-formato (LLM, na fila) |
| POST /api/dossies/:id/dial {eixo} | dials de tom (+lofi, +curto, +cybersec, +polêmico) — nova versão |
| GET /api/dossies/:id/versoes | versionamento de roteiro |

### 1.3 Schema novo (schema.sql + migrations.sql + aplicar em prod)
- `reels` (id, dossie_id?, ig_media_id, caption, posted_at, permalink)
- `metricas_reel` (reel_id, snapshot_date, views, likes, comments, shares, saves, reach, avg_watch_time, follows)
- `metricas_conta` (snapshot_date, followers, reach, impressions, profile_views, engaged)
- `dossie_versoes` (id, dossie_id, content, origem[dial/regen/manual], created_at)
- `items.pilar` TEXT (os 7 pilares — classificador passa a preencher)
- `items.deleted_at` TEXT (lixeira/soft-delete)
- `angulos_descartados` (id, item_id, angulo, pilar, created_at) — banco de ângulos
- FTS5: tabela virtual `busca_fts` (título+hook+dossiê) + triggers

### 1.4 Features de backend embutidas
- **Balanceador 7 pilares:** classificador ganha campo `pilar`; `/api/overview` devolve mix dos últimos 14d + flag de desvio.
- **Banco de ângulos:** dossiê passa a salvar os ângulos cortados pela regra de ouro.
- **Linter lofi:** POST /api/linter {texto} → clichês de IA/lacração/jargão marcados + score (lista de proibidas das ROTEIRO_RULES).
- **Content runway:** cálculo no overview.
**Validação F1:** `tsc` limpo; deploy; smoke de CADA endpoint via curl; fluxos TG intactos (gerar temas dry + dossiê de teste). Commit + aviso TG.

## FASE 2 — Meta App via Dev Browser no Opera (1-2h + possível espera 2FA)
1. developers.facebook.com → My Apps → **Create App** → tipo Business → nome "Infinity Content Painel".
2. Add products: **Instagram Graph API** + **Facebook Login for Business**.
3. Copiar App ID/Secret → `wrangler secret put META_APP_ID / META_APP_SECRET`.
4. Graph API Explorer (ou flow OAuth): token de usuário com `instagram_basic, instagram_manage_insights, pages_show_list, pages_read_engagement, business_management, instagram_content_publish` → trocar por **long-lived (60d)** → `wrangler secret put META_ACCESS_TOKEN`. Descobrir `IG_USER_ID` do @ynwwilson via `GET /me/accounts` → page → `instagram_business_account`.
5. Teste real: `GET /{ig-user-id}/media?fields=...` e insights de 1 Reel.
6. **Se pedir senha:** uso a fornecida. **Se pedir 2FA:** alerta no Telegram "preciso de você: 2FA da Meta" + pauso fase (sigo Fase 4 em paralelo) até confirmar.
7. Worker: módulo `src/instagram.ts` (insights conta + por mídia), cron diário (12h UTC junto do refill) puxa → `metricas_reel`/`metricas_conta`. Auto-match Reel↔dossiê por proximidade caption/horário; fallback match manual no painel.
8. Renovação de token: cron checa validade (<10d → alerta no TG pra renovar; refresh automático de long-lived quando possível).
**Validação F2:** snapshot real no D1 com métricas do @ynwwilson. Commit + aviso TG.
**Limite honesto:** DM automática/inbox precisa de App Review da Meta → FORA desta execução (estrutura fica pronta; submissão fica pra depois com o Mestre).

## FASE 3 — Painel Next.js no Vercel (5-7h)
### 3.1 Setup
- `npx create-next-app` (App Router, TS, Tailwind) em `C:\Users\ynwwi\Projetos\infinity-painel`.
- Deploy inicial via `vercel --scope yngomesmarco-hue` → projeto `infinity-painel` → domínio `infinity-painel.vercel.app` (ou similar livre).
- Env vars no Vercel: `PANEL_PASSWORD`, `WORKER_URL`, `PANEL_KEY` (server-side only).
- Auth: página de login (senha) → cookie httpOnly assinado; middleware protege tudo.
- **Proxy server-side:** rotas `/app/api/*` do Next chamam o Worker com `PANEL_KEY` — key nunca vai ao client.

### 3.2 Design system (glassmorphism LIGHT — syncpay/abacatepay vibe)
- Pesquisar referências reais (syncpay.com, abacatepay.com, dribbble "light glassmorphism dashboard") antes de codar; extrair paleta/espaçamento.
- Direção: fundo claro com gradient suave (off-white→lilás/azul claríssimo), cards `bg-white/60 backdrop-blur-xl border-white/40 shadow-sm rounded-2xl`, acento vibrante único (violeta/índigo), tipografia Inter/Geist, números grandes, MUITO espaço em branco, zero poluição.
- Skill `frontend-design` na construção. Charts: Recharts (linhas/áreas suaves, sem 3D).
- **Responsivo de verdade:** desktop (sidebar fixa) + mobile (bottom nav + cards empilhados). Testar nos dois viewports via browser antes de dar pronto. Nada sobreposto/atravessando tela.

### 3.3 Páginas
| Página | Conteúdo |
|---|---|
| /login | senha, glass card central |
| / (Dashboard) | KPIs (seguidores, views 7d, backlog, taxa aproveitamento, runway, custo) + gráfico seguidores/views + radar 7 pilares + alertas + "melhor Reel da semana" |
| /conteudo | tabs: Temas (cards c/ gancho, filtros, smart views salvas, ações) · Roteiros · Gravados · Não-gravados (c/ motivo) · Postados (c/ métricas) · Lixeira |
| /conteudo/[id] | dossiê completo: roteiro/legenda/hashtags/capa, copiar 1-clique, dials de tom, versões (diff), linter lofi inline, multi-formato (gerar carrossel/thread/stories/outline), marcar gravei/pulei, linkar Reel |
| /metricas | tabs: Instagram (conta: seguidores curva, alcance, engajamento · por Reel: tabela sortável views/likes/saves/retenção + detalhe) · Conteúdo (funil produção, cohort fonte→performance, heatmap firehose) · Aprendizado (afinidade, motivos pulei, hook stats) |
| /acoes | gerar temas · buscar termo · colar link→roteiro · upload print→roteiro (vision) · refill · botões grandes estilo command center |
| /fontes | 12 fontes: status, itens/7d, última coleta ok/fail |
| /config | exemplos/padrões (CRUD), pilares alvo do mix, crons (status), custo API, saúde (alertas recentes), runway alvo |

### 3.4 Paridade Telegram (sync natural)
Painel e bot usam o MESMO D1 via mesma fila/funções → ação de um aparece no outro. Nada a sincronizar além disso (uma fonte de verdade).
**Validação F3:** build limpo, deploy prod, login ok, TODAS as páginas com dados reais do D1, teste mobile (375px) e desktop (1440px) via browser, zero overflow. Commit + aviso TG.

## FASE 4 — Features avançadas (3-4h)
1. **Estúdio multi-formato** (killer #1): prompts por formato (carrossel JSON slides, thread X, stories seq, outline longo) no tom lofi; UI no /conteudo/[id]; roda na fila.
2. **Dials de tom** (quick win): 4 eixos, gera `dossie_versoes`, UI com diff e "usar esta".
3. **Linter lofi** UI inline (sublinha + sugestão + score).
4. **Smart views**: filtros salvos (localStorage + D1 `state`), chips no /conteudo.
5. **Balanceador 7 pilares**: radar no dashboard + alerta de desvio (também via TG semanal).
6. **Banco de ângulos descartados**: aba em /conteudo (Temas → "Ângulos"), promover ângulo→card.
7. **Hook tracking** (estrutura do Hook Arena): marcar qual hook gravou no /conteudo/[id]; quando métricas IG acumularem, /metricas/Aprendizado mostra win-rate por alavanca.
8. **Agendamento leve**: marcar dossiê "agendado p/ data/hora" → lembrete no TG na hora (auto-post via API content_publish: TENTAR em dev mode na própria conta; se specs de vídeo bloquearem, fica lembrete + 1 clique).
**Validação F4:** cada feature testada ao vivo no painel. Commit + aviso TG.

## FASE 5 — Hardening + E2E + entrega (2h)
1. E2E completo: login → dashboard → gerar tema → dossiê → dial → multi-formato → gravei → linkar reel → métricas → busca → fontes → config. Desktop + mobile.
2. Performance: lazy charts, paginação, cache leve (SWR).
3. Blindagem painel: erros de API → toast claro; Worker fora → página de status; notifyOps em falhas novas.
4. Review adversarial (Workflow multi-agente) no diff total — corrigir achados reais.
5. Atualizar vault: PRD → "construído", pendências, arquitetura técnica.
6. **Entrega no Telegram:** URL do painel, o que tem em cada aba, o que ficou pendente (DM/App Review), senha NÃO repetida (a que você definiu).

## Ordem & paralelismo
F0 → F1 → F2 (se 2FA travar: pulo pra F3/F4 e volto) → F3 → F4 → F5.
Estimativa total: ~14-19h de execução autônoma.

## Riscos & contingências
| Risco | Plano |
|---|---|
| 2FA Meta | alerta TG + pausa só a fase Meta; resto segue |
| App Review necessário p/ algo essencial | escopo já evita; publish testado em dev mode na própria conta; se falhar → agendar vira lembrete |
| Anthropic sem crédito no meio | blindagem alerta no TG; features LLM pausam, painel/API seguem |
| Nome de projeto/domínio Vercel ocupado | variação `infinity-content-painel` etc |
| Limite CPU Worker nos insights | batch por mídia + cron, nunca request única gigante |
| Quebrar Telegram | guard-rail 2: teste dos fluxos TG após cada deploy do Worker |

## Critério de PRONTO (o que o Mestre encontra ao voltar)
- Painel no ar em domínio *.vercel.app, login com a senha definida.
- Dashboard com dados REAIS (conteúdo + Instagram @ynwwilson).
- Toda ação do Telegram disponível no painel (e TG funcionando igual).
- Subabas Gravados/Não gravados/Postados operantes.
- Métricas IG por conta e por Reel + cortes; funil; aprendizado.
- Multi-formato, dials, linter, smart views, balanceador, ângulos, runway funcionando.
- Design light glass, limpo, responsivo desktop+mobile, nada sobreposto.
- Tudo commitado, vault atualizado, relatório final no Telegram.
