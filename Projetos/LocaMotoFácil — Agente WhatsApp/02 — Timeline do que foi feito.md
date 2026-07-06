---
projeto: LocaMotoFácil — Agente WhatsApp
nota: Timeline do que foi feito
---

# Timeline do que foi feito

## Fase A — Fundação (sessões anteriores)
Construído o esqueleto: core (toolkit), gateway (Worker+DO), panel (Next), migration 0001. Stack decidida com o dono. Typecheck + ~38 testes verdes. Ainda não deployado.

## Fase B — Construir o código (12 "waves", branch `build-b`)
Commits `da075c2` (baseline) → `62ea568` (verificação). Cada wave = build + commit atômico.
1. **Confiabilidade** — idempotência (índice único wa_message_id), ordem, DO exactly-once
2. **Cérebro** — system prompt LocaMotoFácil + anti-injection
3. **Entrada** — áudio/imagem/doc/vídeo/comprovante + failover Groq
4. **Voz** — áudio pré-gravado como nota de voz PTT (sem selo encaminhado)
5. **Memória** — recente + resumo rolante + pgvector + fila de re-embed
6. **Segurança** — RLS por `panel_users`, brain secret constant-time
7. **Observabilidade** — error_log, painel /health, kill-switch de custo
8. **Perfil + style-filter** — profileUpdate estruturado, filtro de clichê
9. **Robustez** — NaN-guards, router hooks fora do try, zod nas actions
10. **Proativo + LGPD** — templates, cron, opt_in, apagar contato
11. **Polish** — cache signed URL, ticks de entrega, timezone
12. **Verificação** — 15 requisitos mapeados, relatório `FASE-B-VERIFY.md`
Resultado: typecheck (3 workspaces) + 99 testes + next build verdes.

## Fase C — Deploy + E2E (2026-06-07)
Tudo feito **pelo navegador (dev-browser no Opera logado)** + CLIs:
- Migrations 0002–0006 rodadas no Supabase (renumerei proactive 0005→0006, colidia). **Fix de segurança:** `panel_users` tinha hole de escalonamento (sem RLS + grants amplos) → enable RLS + policy SELECT-only.
- **Painel → Vercel** (`waa-panel`, scope `yngomesmarco-hues-projects`, Root Directory=apps/panel, 29 env vars, cron /15)
- **Gateway → Cloudflare** (`waa-gateway`, DO, 4 secrets)
- **Webhook Meta** configurado via Graph API (POST /{app}/subscriptions + /{waba}/subscribed_apps). Fields: messages + message_template_status_update.
- Número de teste **registrado** (POST /{PNID}/register, pin). Celular do dono cadastrado+verificado como destinatário.
- **E2E:** "quanto custa" → IA respondeu "R$427..." status delivered. Pipeline inteiro verde.

### Bloqueio resolvido na Fase C
As 2 chaves LLM estavam **sem crédito** (OpenAI 429 insufficient_quota; Anthropic 400 low balance). Dono pôs crédito na OpenAI → funcionou. Anthropic ainda sem crédito.

### Quirk do "9" brasileiro
Meta normaliza o celular `5534991036586` → wa_id `553491036586` (sem o 9 extra). Tive que cadastrar **as duas formas** na lista de permissão do número de teste, senão envio dá `(#131030) not in allowed list`. Em número real não existe lista, não acontece.

## Testes de mídia (2026-06-07) — todos passaram, com 4 fixes
- **Áudio** ✅ transcreve+responde. **Documento PDF** ✅ extrai o corpo (unpdf funciona no serverless Vercel).
- **Comprovante** ✅ com 4 correções: (1) data-âncora no prompt (classificava "agendado" pagamento de hoje), (2) extrai `recipient` + compara valor/empresa → avisa Pix errado (migration 0007), (3) retry 1x + anti-recusa na visão (gpt-4o recusava ~50%), (4) persiste texto do doc.

## Redesign do painel (2026-06-08) — Revolut Dark laranja
Spec em `docs/superpowers/specs/2026-06-07-panel-redesign-design.md`. Mockup aprovado pelo dono. Commits `ecd7848`→`dd9188a`.
- Design system (tokens + primitivas Card/StatCard/Ring/Tag/Pill/Panel/Avatar/Sparkline + Icon SVG)
- Shell responsivo (sidebar desktop + bottom-nav mobile + drawer "Mais" só com não-principais)
- Telas novas: Visão Geral (dashboard) + Pagamentos (agrupado por lead)
- Chat reescrito (desktop 2-col, mobile bottom-sheet de contexto)
- Todas as outras telas reskinadas. Mobile 100% (vários fixes de overlap/tamanho).
- **Pix destino errado ≠ efetuado** → status "destino errado", não conta como efetuado.

## Regras de negócio travadas (2026-06-08/09)
- **Pagamento só na retirada, presencial, nada adiantado** (anti-golpe). IA nunca pede Pix. Commits `38ca2b6`, `b4e9a66`.
- **CNPJ 00.971.610/0001-32** na base + FAQ (prova de legitimidade).

## SGRLock — consulta de risco (2026-06-09)
Integração completa construída (commit `3687d9f`). Ver [[07 — SGRLock (consulta de risco)]]. Falta só credencial da Odeen.
