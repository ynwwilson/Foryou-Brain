---
title: "Rainha — Super-Análise e Verificação"
type: relatorio
created: 2026-05-27
tags: [rainha, verificacao, auditoria, producao]
status: concluido
---

# Super-Análise & Verificação — Método Rainha da Aprovação
**Data:** 2026-05-27 · **Repo:** `metodorainha-4fadbe36` (branch `main`, HEAD `b7dae71`)
**Produção:** frontend `https://www.metodorainhadaaprovacao.com.br` (Vercel/main) · backend Lovable Cloud (Supabase `tftipqnwprsranaovkci`)
**Método:** 3 camadas — Código (repo) · Deploy (está em produção?) · Runtime (funciona?)

---

## 0. Veredito executivo

A **grande maioria das correções está no código e funcionando** — access gate, gate financeiro, segurança de gabarito, performance e filtros foram confirmados em produção. **Porém há 1 problema CRÍTICO em produção:**

> 🔴 **Só 4 das 30 edge functions foram redeployadas com o CORS novo.** As outras 26 (incluindo `student-progress`) rodam CORS antigo e **NÃO permitem o domínio oficial `www.metodorainhadaaprovacao.com.br`**. Confirmado em runtime: `student-progress` falha com `net::ERR_FAILED` no dashboard do aluno.

**Causa:** a migração de domínio para `.com.br` exige **redeploy de TODAS as edge functions**. A Lovable só redeployou as 4 que foram nomeadas explicitamente no prompt de deploy (`invite-user`, `create-and-invite`, `send-password-reset`, `send-notification-email`). Antes, com o app em `*.vercel.app`, as functions stale funcionavam (sufixo `.vercel.app` é confiável); ao mudar pro `.com.br`, quebraram.

**Ação #1 (crítica):** redeployar **todas** as 30 edge functions via Lovable.

---

## 1. Achado crítico — CORS stale em 26/30 edge functions

Teste: preflight OPTIONS com `Origin: https://www.metodorainhadaaprovacao.com.br`. FRESH = reflete o domínio; STALE = devolve fallback `metodorainhadaaprovacao.vercel.app`.

**✅ FRESH (4):** `invite-user`, `create-and-invite`, `send-password-reset`, `send-notification-email`

**⚠️ STALE (26):** `analyze-weakness`, `backup-question-images`, `batch-delete-questions`, `check-expired-subscriptions`*, `classify-questions`, `delete-student`, `eduzz-webhook`*, `explain-question`, `generate-flashcards`, `health`, `import-cda-students`, `import-portugues`, `import-questions`, `import-students`, `proxy-essay-pdf`, `reclassify-topics`, `search-profiles`, `send-bulk-password-reset`, `send-custom-email`, `serve-essay-pdf`, `set-password`, **`student-progress`**, `sync-study-room-planner`, `test-email`, `update-student-email`, `verify-identity`

(*`eduzz-webhook` e `check-expired-subscriptions` devolvem `*` — server-to-server/cron, CORS não as afeta.)

**Impacto em produção (chamadas do browser no `.com.br`):**
- 🔴 `student-progress` — **confirmado quebrado em runtime** (`net::ERR_FAILED` ×3 no `/student`). Dashboard de progresso do aluno.
- ⚠️ Risco em: `explain-question` (IA), `analyze-weakness`, `generate-flashcards`, `sync-study-room-planner`, `delete-student`, `update-student-email`, `set-password`, `verify-identity`, `search-profiles`, `send-bulk-password-reset`, `send-custom-email` — todas chamadas potencialmente do domínio oficial.

**Atenuante:** o access gate aguenta a falha do `student-progress` sem travar (loading não fica infinito).

---

## 2. Matriz de verificação — 16 áreas × 3 camadas

| # | Área | Código | Deploy | Runtime | Veredito |
|---|------|:---:|:---:|:---:|---|
| 1 | Domínio/SSL/redirect/allowlist | ✅ | ✅ | ✅ | OK — `.com.br` via Vercel, root→www 307 |
| 2 | Gate de acesso (loading infinito) | ✅ | ✅ | ✅ | OK — máquina de estados pura, timeout 9s; não trava mesmo com student-progress falhando |
| 3 | Gate financeiro (subscription) | ✅ | ✅ | ⚠️ | Código prova: `hasActiveSubscription` única chave, contrato não libera. Paywall não testado em runtime (pulado) |
| 4 | Segurança de gabarito | ✅ | ✅ | ✅ | OK — `STUDENT_SAFE_QUESTION_SELECT` sem correct_option; RPC pós-submit; 8 SECURITY DEFINER; payload runtime sem gabarito |
| 5 | Simulados | ✅ | ? | ⚠️ | Código + RPC seguro presentes; save/persist não testado em runtime |
| 6 | Caderno de erros | ✅ | ? | ⚠️ | Migration pending→resolved→pending presente; fluxo não testado em runtime |
| 7 | Performance inicial | ✅ | ✅ | ✅ | OK — 1ª página/total separados; 1ª questão em ~1.1s (era 15-20s) |
| 8 | PWA sem reload forçado | ✅ | ✅ | ⚠️ | `registerType:prompt`, `skipWaiting:false`, sem `reload()`; não observado em runtime |
| 9 | Filtros dinâmicos | ✅ | ✅ | ✅ | 3 RPCs, anos≥2010; runtime sem erro de opções, anos presentes |
| 10 | **CORS edge functions** | ✅ | 🔴 | 🔴 | **CÓDIGO certo, mas só 4/30 deployadas — ver seção 1** |
| 11 | Prefetch filtros background | ⚠️ | — | ⚠️ | Não evidenciado por nome no código; inconclusivo |
| 12 | Segurança mantida (sem leak) | ✅ | ✅ | ✅ | Confirmado: sem correct_option no payload de aluno |
| 13 | Testes (build/unit) | ✅ | — | — | 185/185 local (tsc + vitest) |
| 14 | Realtime não reacende loading | ✅ | — | ⚠️ | Código (gate desacopla); não estressado em runtime |
| 15 | public.topics removido (filtro) | ⚠️ | — | — | Filtro usa RPC topic_tree ✅; mas `SubjectsPage`/`SubjectDetailPage` ainda usam `.from('topics')` (feature de navegação ≠ filtro) |
| 16 | Índices SQL de performance | ✅ | ? | ✅ (indireto) | 28 migrations com CREATE INDEX; latência baixa (~1.1s) sugere índices ativos |

---

## 3. Notas e gaps menores

- **#11 Prefetch:** não há `prefetchQuery` explícito; o carregamento rápido pode vir de React Query padrão. Baixa prioridade.
- **#15 public.topics:** resíduo em `SubjectsPage.tsx:83` e `SubjectDetailPage.tsx:41` — é navegação de matérias, não o filtro de questões (esse usa RPC). Avaliar se a tabela `topics` ainda deve existir.
- **FocusStudyMode (falso alarme):** lê `correct_option` mas só pós-resposta, do RPC; fetch usa select seguro. Não é leak.

## 4. Não verificado (precisa de runtime adicional / acesso)

- Paywall (conta sem assinatura) — pulado a pedido.
- Caderno de erros fluxo completo (errar→acertar→corrigidas) em runtime.
- Simulado: salvamento/persistência/retomada em runtime.
- PWA: ausência de reload automático observada ao vivo.
- DB direto (RLS/índices aplicados no banco vivo) — sem acesso ao Supabase do Lovable Cloud; verificado só indiretamente.

## 5. Ações recomendadas (prioridade)

1. 🔴 **Redeployar TODAS as 30 edge functions** via Lovable (não só as 4). Especialmente `student-progress`, `explain-question`, `analyze-weakness`, `generate-flashcards`, `sync-study-room-planner`, e as de admin (`delete-student`, `update-student-email`, `set-password`, `verify-identity`, `search-profiles`). **Sem isso, features quebram no domínio oficial.**
2. Corrigir `docs/AMBIENTES_DEPLOY_DOMINIOS.md` (deploy é via Lovable, não CLI — o token não alcança o projeto).
3. Validar runtime restante: paywall, caderno de erros, simulado, PWA.
4. Decidir sobre `public.topics` (resíduo em SubjectsPage).
5. Apagar aluno de teste `ZZ TESTE QA DEPLOY` (ID `dde11ab1-d0fa-4c90-989e-5be712fec5c1`).
6. Rotacionar os 5 tokens que estavam em texto plano.

---

Relacionado: [[Rainha da Aprovacao]] · [[2026-04-18 Rainha Diagnostico Definitivo v2]]
