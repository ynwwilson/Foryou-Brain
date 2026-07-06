---
title: IA Concretize - Arquivado 2026-05-28
type: status-operacional
project: Concretize / IA de Atendimento Rodrigo
date: '2026-05-28'
updated: '2026-05-28 11:45'
status: arquivado-sem-ia
tags:
  - concretize
  - ia-atendimento
  - whatsapp
  - meta-cloud-api
  - vercel
  - arquivado
  - sem-ia
---
# IA Concretize - Arquivado 2026-05-28

## Decisao
Wilson decidiu que Rodrigo volta para o WhatsApp Business padrao, sem agente de IA e com atendimento manual.

## Estado aplicado
- Backend PROD2 preservado em `https://concretize-ia-prod2.vercel.app`.
- Codigo, historico, banco, catalogo e painel nao foram apagados.
- Runtime entrou em modo arquivado por env `ARCHIVE_MODE=1`.
- Nome publico/status: `Rodrigo - arquivado`.
- Telefone exibido no status: `+1 555 0100`.
- Provider exibido: `archived`.
- Instancia exibida: `meta-test-number`.
- `/api/status?debug=1` confirmou `status=archived`, `webhookCanProcess=false`, `aiCanProcessReplies=false` e sem `recentFailures`.
- `POST /api/webhook/meta-whatsapp` confirmou `ignored=archived`.

## Commits e deploy
- `5d79139 feat: add archived mode for Rodrigo shutdown`
- `7ccda3f fix: hide debug failures in archived mode`
- Deploy final Vercel PROD2: `dpl_9nbghkWrESgpuntjgSvjAc7Nb82J`, alias `https://concretize-ia-prod2.vercel.app`.

## O que foi bloqueado
- Webhook legado e webhook Meta nao processam mensagens quando `ARCHIVE_MODE=1`.
- Envio manual por `/api/send` retorna `whatsapp_archived`.
- Envio de midia por `/api/send-media` retorna `whatsapp_archived`.
- Follow-up automatico retorna `archived`.
- Aprovacao de follow-up nao dispara envio quando arquivado.
- Status administrativo de WhatsApp retorna provider `archived`.

## O que nao foi feito
- Nenhum dado foi apagado.
- Nenhuma conversa, lead, memoria, catalogo ou produto foi deletado.
- Nenhum segredo foi impresso em nota.
- As variaveis antigas da Meta/MegaAPI continuam no Vercel, mas ficam neutralizadas pelo modo arquivado.

## Se precisar reativar
1. Remover ou desligar `ARCHIVE_MODE` no projeto Vercel `concretize-ia-prod2`.
2. Redeployar producao.
3. Validar `/api/status?debug=1`.
4. Conferir Meta WhatsApp, Chatwoot, painel e um teste real antes de permitir atendimento automatico.

