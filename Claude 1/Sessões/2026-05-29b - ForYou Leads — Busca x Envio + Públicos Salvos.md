---
data: 2026-05-29
tipo: implementação
projeto: ForYou Leads — Separar Busca × Envio + Públicos Salvos
status: ENTREGUE — PR #6 mergeado, em produção
---

# 2026-05-29 (2) — ForYou Leads: busca × envio separados + públicos salvos

> Quebra a campanha mono em **dois tipos** e mata a busca automática diária. 6 commits na branch `feat/scrape-send-split` → **PR #6**. Build + typecheck limpos, migration 024 aplicada.

## Dor / pedido
Busca de leads rodava automática todo dia. Wilson quis: tornar a busca **manual + auto por toggle** (campanha própria que conclui ao bater a meta), e separar de envio. Públicos salvos reutilizáveis. Ao clicar "Criar campanha", escolher entre **Buscar** e **Enviar**.

## Decisões
- **2 tipos**: 📡 busca (scrape) × 🚀 envio (send).
- **Busca**: ativa pelo toggle → busca até `scrape_goal` → status **concluída**. Botão "Buscar agora". Vira público salvo (nome = nome da campanha).
- **Envio**: público **salvo** (trava + cancelar) OU **manual** (nicho/cidade/faixa filtra leads existentes). Impossível publicar sem público.
- **Oferta + templates moram na BUSCA** (mensagens são geradas na captura). Envio herda.
- **Exclusão da busca**: apaga leads + público, **pausa** os envios que usavam.
- Sem busca automática diária pras campanhas de envio.

## Backend
- Migration 024: `campaigns.type`, `scrape_goal`, `audience_campaign_id`, status `concluida`. Backfill: existentes → send + audiência = self.
- `lib/scrape-pipeline.ts` (extraído de apify route, que não pode exportar helper). `/api/campaigns/[id]/scrape`, `/api/audiences`.
- `fetchSendQueue` por audiência/filtro manual; `dispatch` só `type=send`, teto via `send_jobs`; cron Apify só `type=scrape ativa`, conclui na meta.
- stats por tipo (join na audiência via `COALESCE(audience_campaign_id, id)`).

## UI
- Seletor de tipo ao criar. ScrapeBuilder + SendBuilder. Lista com chip 📡/🚀 e capturados/meta. Painel da campanha em 2 modos (busca: progresso + Buscar agora; envio: como antes + qual público).

## Estado
- **PR #6**: github.com/ynwwilson/foryou-leads/pull/6 — aguardando merge → deploy.

## Pendências / atenção
- Mensagens são geradas na captura com a oferta da busca → mudar de oferta exige nova busca (geração on-the-fly por oferta no envio ficou fora de escopo).
- Worker sempre-on (`npm run worker:install`) continua valendo da entrega anterior.

Relacionado: [[Pipeline de Leads ForYou]], [[2026-05-29 - ForYou Leads — Envio automático + sem terminal]]
