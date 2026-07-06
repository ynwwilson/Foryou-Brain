---
data: 2026-05-22
hora: 00h37
tipo: sessão de implementação
projeto: ForYou Leads — Sistema de Ofertas + Gerenciador de Campanhas
duração: ~longa (multi-feature)
---

# 2026-05-22 00h37 — ForYou Leads: Ofertas multi-produto + Gerenciador de Campanhas

Sessão longa, três entregas grandes no [[Pipeline de Leads ForYou]], todas deployadas em produção.

## O que foi feito

### 1. Sistema de Ofertas (multi-produto) — PR #2

Antes: o sistema vendia **um produto só** ("site profissional saúde/estética R$1.500-2.000"), hardcoded em 5 lugares dentro de `lib/claude.ts`. Não dava pra oferecer outra coisa sem mexer no código.

Agora: catálogo de **Ofertas** configurável pela UI.

- **Migration 021** (`sql/021_offers.sql`): tabela `offers` + `offer_id` em `campaigns`/`leads`/`videos`. Seed da oferta padrão "Site Profissional" reproduzindo o produto atual, backfill de tudo (5 campanhas, 320 leads, 0 nulls), + rascunhos inativos "IA de Atendimento" e "Aplicativo".
- **`lib/claude.ts`**: os 5 prompts hardcoded viraram funções `buildAnalyzePrompt(offer)`, `buildVendedoraPrompt(offer)`, `buildQuickRepliesPrompt(offer)`. A IA de captação e a IA Vendedora montam as mensagens a partir da oferta da campanha. CTA index respeita `offer.cta_variants.length`.
- **`lib/offers.ts`**: helpers CRUD + `getOfferOrDefault` (fallback pra oferta padrão → zero quebra em leads/campanhas legados).
- **Tela `/admin/ofertas`** (`offers-client.tsx`): criar/editar/duplicar/ativar/excluir ofertas. Cada oferta tem público-alvo, preço, descrição, pitch, case, orientação da DM, orientação da IA Vendedora e lista editável de CTAs.
- **`OfferCombobox`**: balãozinho filtra-enquanto-digita no formulário de campanha (mesma UX do nicho).
- **Métricas**: nova tabela "🎁 Por oferta" em `/metricas`.

### 2. Fix do login + acessos

Bug: login não enviava código no Telegram. **Causa raiz**: a conta do Wilson estava `active = false` → o `/api/auth/start` filtra `WHERE active = true`, não achava o user, caía no anti-enumeration e respondia "código enviado" sem enviar nada.

- Reativada a conta do Wilson/José.
- **Marco, Eduardo e Wilson/José** agora todos `role = admin` (acesso total — decisão do Wilson).
- **`sendLoginCode` endurecido**: agora checa a resposta do Telegram (`data.ok`). Antes, qualquer falha (token errado, chat bloqueado) passava como sucesso silencioso.

### 3. Gerenciador de Campanhas (estilo Ads Manager) — PR #3

Antes: Campanha (captura) e Envio (`/enviar`) eram dois objetos desconectados. O `/enviar` era um "manda uns leads" genérico com filtro de campanha pendurado.

Agora: a **campanha é a unidade de trabalho completa** — captura + envio + oferta + criativo + ritmo.

- **Migration 022** (`sql/022_campaign_full.sql`): `status` (rascunho|pausada|ativa, substitui o booleano `active`) + config de envio na campanha (`video_id`, `use_video_pool`, `dms_per_day`, `send_hour_start/end`, `send_days`, `dm_interval_min/max_sec`). `send_jobs` ganha o intervalo entre DMs.
- **Lista estilo Ads Manager** (`campaigns-client.tsx`): tabela com status + métricas ao vivo (capturados, fila, enviados hoje, respostas, quentes, clientes, R$).
- **Builder em seções**: Público → Oferta → Criativo → Ritmo → Nome/Dono. Salva como rascunho ou publica.
- **Painel da campanha** (`/admin/campaigns/[id]` + `campaign-panel.tsx`): captura + envio + botão "Enviar agora" + feed do job ao vivo. Substitui o `/enviar`.
- **`/api/campaigns/[id]/send`**: monta o lote a partir da config da campanha (teto `dms_per_day`, janela de horário/dias, vídeo, intervalo).
- **Worker** (`worker-adspower.mjs`): respeita o intervalo entre DMs configurado por campanha (antes era fixo 3-8min no código).

### 4. Corte de redundância

- `/enviar` removido → virou o painel da campanha (`SendController` deletado).
- `/hoje` + `/respostas` fundidos em **`/atendimento`** (fila única de ação humana: leads que responderam/quentes/agendaram).
- `/metricas` + ROI Nichos fundidos em **abas** dentro de `/metricas`.
- Menu lateral: de 12 → 9 itens, Campanhas em destaque no topo.
- Rotas antigas (`/enviar`, `/hoje`, `/respostas`, `/metricas/nichos`) redirecionam — nenhum link quebra.

## Decisões tomadas

- **Ofertas editáveis na UI** (banco de dados), não catálogo fixo no código.
- **Template = guia que a IA personaliza** (não texto fixo) — mantém variação anti-bloqueio.
- **Envio manual por lote** — ativar a campanha não dispara envio automático; o operador clica "Enviar agora" no painel. Toda config já vem da campanha.
- **Ritmo controle total** — campanha define janela, DMs/dia e intervalo entre DMs.
- **Marco/Eduardo/Wilson todos admin** — sem distinção de operador.

## Estado atual

- 3 PRs mergeados em `main` (#1 Fase 5 anterior, #2 Ofertas, #3 Campanhas). Migrations 021 + 022 aplicadas em produção.
- Typecheck + `next build` limpos. Vercel deployando.
- 5 campanhas migradas pra `status` (3 pausadas, 2 ativas) — vieram **sem vídeo** definido na config nova.
- 3 ofertas no catálogo: Site Profissional (ativa/padrão, 8 CTAs), IA de Atendimento e Aplicativo (rascunhos inativos).

## Próximos passos / pendências

- **Wilson edita** cada campanha (seção Criativo) pra escolher o vídeo ou pool — as 5 antigas vieram sem vídeo.
- Preencher e ativar a oferta "IA de Atendimento" quando for vender esse produto.
- Worker dos operadores precisa estar rodando pra "Enviar agora" funcionar.
- Migration `019` e `021` acusam checksum mismatch no migrate runner (conversão CRLF do git pós-aplicação) — inofensivo, mas pode ser limpo depois.
- Deferido (follow-up): override de oferta por lead na tela de detalhe; seleção de vídeo de demo por oferta amarrada ao `videos.offer_id`.
- Fase 5 da repaginada minimalista do front (component library) — não iniciada.

## Artefatos

- Plano: `C:\Users\ynwwi\.claude-nova\plans\estou-sentindo-muita-fizzy-tide.md`
- PRs: github.com/ynwwilson/foryou-leads/pull/2 e /pull/3
- Migrations novas: `sql/021_offers.sql`, `sql/022_campaign_full.sql`

Relacionado: [[Pipeline de Leads ForYou]], [[ForYou Leads — Roadmap Pós-Auditoria]]
