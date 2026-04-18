# Encerramento — 2026-04-18 00h00

## O que foi feito

### Pipeline de catálogo
- `lib/supabase.ts`: novo `getCatalogSnapshot()` que retorna prompt rico (nome, dimensões, aplicações, argumentos de venda, brain_context) agrupado por categoria, com cache de 60s.
- Catálogo agora é injetado em **todo** request de IA via `lib/aiRouter.ts` (antes só tinha "Cobogós" genérico no identity).

### Validador determinístico (novo)
- `lib/responseValidator.ts`: detecta invenção de produto com regex + Levenshtein fuzzy match (tolera transcrição/fonética tipo "Fenestraa").
- `validateResponse()` rodando em `generateWithValidation()` no aiRouter: se IA inventa, refaz 1x com alerta corretivo; loga `double_miss` se falhar de novo.
- `scanHistoryForInvalid()` varre mensagens prévias do assistente e injeta `[AVISO DE CONTEXTO]` se detectar invenção passada — quebra ciclo de auto-reforço.
- `tests/response-validator.test.js`: 8 testes de regressão, todos verdes.

### Regras do brain (v10 publicada no Supabase)
- Removidos literais "Eter do Muno" de `lib/brainConfig.ts` (linhas 1393, 1442).
- `POSTURA PARA PRODUTO FORA DO CATÁLOGO`: rule genérica (qualquer produto ausente vira "esse a gente não trabalha, temos X/Y/Z, quer ver?").
- `REGRA DE FLUIDEZ DA CONVERSA`: segue última mensagem do lead, não insiste em assunto abandonado, volta quando o lead volta, espelha ritmo/tom/formato.
- `handoff` com **LISTA FECHADA**: passa pro Rodrigo só em desconto, fechamento, comprovante/pix/agendamento, orçamento+frete. Resto (dúvida técnica, reclamação, pedido de catálogo/foto, cliente dizendo "quero falar com alguém" genericamente) → IA resolve.

### Robustez do roteador
- `lib/ai.ts`: `isRetryableProviderError()` agora **pula retry em 429/quota** — Gemini exausto cai direto no OpenAI fallback sem desperdiçar tentativa.
- Length cap em `lib/aiRouter.ts`: `resolveMaxLines()` baseado no tamanho do input do lead (≤8 palavras → 2 blocos; ≤20 → 4; else sem cap). Evita textão em resposta a mensagem curta.
- `history` agora é passado pro router e chega no scanner/prompt.

### Patch script
- `scripts/patch-brain-config.mjs`: `LEGACY_PATCH_HEADERS` para stripar conteúdo pré-marker poluído; `HANDOFF_RULES` aplicado tanto em `ai_brain_versions` (main) quanto em `analytics_v2` (fallback).
- Utilitários: `scripts/dump-brain-sections.mjs`, `scripts/dump-identity.mjs`, `scripts/dump-product-schema.mjs`, `scripts/hunt-eter.mjs` (confirmou que "Eter do Muno" não existe em DB — era só hallucination).

### Commit + deploy
- Commit `736613c` em main, push feito, Vercel auto-deploy disparado.

## Decisões tomadas

- **Regra anti-invenção generalizada** — cliente pediu que não fosse só "Éter", qualquer produto fora do catálogo entra no mesmo padrão de resposta.
- **Handoff apertado** — cliente explícito: só desconto/fechamento/pagamento/orçamento+frete passa pro humano, mais nada. Dúvida técnica, reclamação, pedido de catálogo, tudo é IA.
- **Validador + retry único (não loop)** — se dois tries falham, log `double_miss` e deixa a resposta sair; evita travar webhook.
- **429 ≠ retry** — rate limit do Gemini não melhora com backoff curto; fallback imediato pro OpenAI é mais barato em latência.
- **Cache de 60s no catálogo** — balanço entre frescor e carga no Supabase; produtos mudam raramente.

## Estado atual

- **Produção**: commit `736613c` em main, Vercel em deploy.
- **Brain**: v10 no Supabase (org `ccf52483-3e36-4a1d-8e7a-b2d9e107a36d`), `is_current=true`, com marker `__PATCH_V2__` em guardrails, tone_style, sales_rules, handoff.
- **Tests**: 114/114 verdes, typecheck limpo.
- **Modelos**: Gemini 2.5 Flash-Lite principal + OpenAI GPT-4o mini fallback.
- **WhatsApp**: pendente reconectar (item operacional, fora do código).

## Próximos passos

- **Monitorar logs** de `[validator:invalid]` e `[validator:double_miss]` nas primeiras horas pós-deploy — se double_miss for frequente, ajustar prompt do retry.
- **Reconectar WhatsApp** na MegaAPI (item operacional do Rodrigo, não é código).
- **Observar se o 429 do Gemini** ainda aparece em volume — se sim, avaliar subir quota ou inverter ordem (OpenAI principal).
- **Validar em conversas reais** se a regra de fluidez tá funcionando (lead muda assunto → IA acompanha; lead volta → IA volta).
- **Dashboard** de hoje (item antigo pendente) — não foi tocado nesta sessão.
