---
title: WhatsApp Cloud API — Migração Meta Concretize
type: handoff-tecnico
project: IA de Atendimento Rodrigo / Concretize
date: '2026-05-19'
status: historica-supersedida-por-handoff-2026-05-22
tags:
  - concretize
  - whatsapp
  - meta
  - cloud-api
  - vercel
  - webhook
  - migração
updated: '2026-05-22'
---
# WhatsApp Cloud API — Migração Meta Concretize

## Resumo executivo
Estamos migrando o WhatsApp da IA da Concretize de uma API não oficial para a WhatsApp Cloud API oficial da Meta.

A IA/agente já está pronta. A regra da migração é não mexer em prompt, memória, regras comerciais, RAG, banco ou fluxo de atendimento. O trabalho feito foi criar o conector oficial Meta/Cloud API preservando a integração antiga como fallback.

Estado real em 2026-05-19: backend, rota, verificação, adapter, assinatura HMAC e envio Cloud API foram implementados e deployados. O webhook de teste da Meta chega na Vercel e aciona a IA. Mensagens reais do WhatsApp ainda não chegaram ao callback; causa mais provável identificada: falta assinar a WABA no App via `/{WABA_ID}/subscribed_apps` usando token permanente válido.

## Identificadores Meta
- App: `IA CONCRETIZE`
- App ID: `1330367675744725`
- WABA ID: `2013351966214745`
- Phone Number ID de teste: `1173823579138528`
- Número de teste Meta: `+1 555 632 3563`
- Número real futuro da Concretize: `+55 34 99718-3001`
- Número pessoal José/desenvolvedor usado em teste: `+55 34 99103-6586`
- `wa_id` observado do José no payload Meta: `553491036586`
- Verify token configurado: `iaconcretize_verify_2026`

## Segurança
- Tokens e App Secret foram colados no chat durante a sessão. Não registrar valores em notas, código ou logs.
- Antes de produção real, rotacionar token e App Secret.
- Solução definitiva exige token de System User, não token temporário da tela “Experimente”.
- Não commitar secrets.
- Não logar `META_WHATSAPP_TOKEN` nem `META_APP_SECRET`.

## Código implementado
Arquivos criados/alterados no backend `C:\Users\ynwwi\Projects\concretize-ia-webhook`:

- `lib/metaWhatsapp.ts`
  - Normaliza payload da Meta Cloud API para o formato interno legado.
  - Extrai `wa_id`, nome, texto, `message_id`, timestamp, `phone_number_id` e tipo da mensagem.
  - Envia texto via `https://graph.facebook.com/v25.0/{META_PHONE_NUMBER_ID}/messages`.
  - Suporta envio de mídia por URL para image/video/document; link vira texto.
  - Valida `X-Hub-Signature-256` com `META_APP_SECRET`.
  - Expõe status sanitizado para painel/admin.

- `api/webhook/meta-whatsapp.ts`
  - `GET /webhook/meta-whatsapp`: verificação da Meta com `hub.mode`, `hub.verify_token`, `hub.challenge`.
  - `POST /webhook/meta-whatsapp`: recebe payload Meta, valida assinatura, normaliza e envia para fluxo legado da IA.

- `api/webhook.ts`
  - Adicionado `WebhookSource = 'megaapi' | 'meta-whatsapp'`.
  - Mensagens Meta passam pelo mesmo `processMessage()` da IA.
  - Respostas de mensagens Meta são enviadas pela Cloud API.
  - Respostas de mensagens MegaAPI continuam pela integração antiga.
  - Presence/digitação foi pulado para Meta, pois não há equivalente direto usado nesse fluxo.

- `api/admin/wa-status.ts`
  - Mantém compatibilidade com campos antigos: `connected`, `phone`, `state`.
  - Adiciona `activeProvider`, `providers.metaWhatsapp`, `providers.megaapi` e `migration`.
  - Centro de comando pode exibir saúde da Meta e fallback antigo.

- `vercel.json`
  - Adicionada função `api/webhook/meta-whatsapp.ts`.
  - Adicionado rewrite `/webhook/meta-whatsapp` para `/api/webhook/meta-whatsapp`.

- `tests/meta-whatsapp.test.js`
  - Testes do parser/normalização/assinatura/envio Meta.

- `tests/webhook-source.test.js`
  - Ajustado para source Meta vs MegaAPI.

## Commits criados
- `0e865d8` — `feat: add Meta WhatsApp Cloud API connector`
- `7be08fd` — `feat: expose Meta WhatsApp status`

## Deploy e validações
Deploy de produção feito na Vercel para:
- `https://concretize-ia.vercel.app`

Validações realizadas:
- `npm run build` passou.
- `npm test` passou com `166/166` testes.
- Atualização Codex em 19/05/2026:
  - commits `0e865d8` e `7be08fd` enviados para `origin/main`;
  - Vercel criou deploy production `READY` para `7be08fd`;
  - `GET /api/status` retornou `status: ok`, readiness de IA verde e catálogo com 30/30 imagens;
  - handshake `GET /webhook/meta-whatsapp` retornou o challenge corretamente;
  - `POST /webhook/meta-whatsapp` sem assinatura retornou `403 invalid_signature`, confirmando HMAC ativo.
- GET de verificação funcionou:
  - URL testada: `https://concretize-ia.vercel.app/webhook/meta-whatsapp?hub.mode=subscribe&hub.verify_token=iaconcretize_verify_2026&hub.challenge=teste123`
  - Resposta esperada/observada: `teste123`
- Acesso direto sem parâmetros retorna `invalid_verify_token`, o que é normal.
- POST sem assinatura Meta retorna `403 invalid_signature`, provando que HMAC está ativo.

## Env vars necessárias na Vercel
Somente nomes, sem valores:

```env
META_WHATSAPP_TOKEN=
META_PHONE_NUMBER_ID=1173823579138528
META_WABA_ID=2013351966214745
META_VERIFY_TOKEN=iaconcretize_verify_2026
META_APP_SECRET=
```

Também continuam necessárias as envs já existentes da IA, Supabase, Redis, OpenAI/Gemini, Chatwoot e MegaAPI.

## Meta: o que já foi feito
- App `IA CONCRETIZE` criado.
- Caso de uso WhatsApp adicionado.
- Webhook configurado com callback:
  - `https://concretize-ia.vercel.app/webhook/meta-whatsapp`
- Verify token configurado:
  - `iaconcretize_verify_2026`
- Campo `messages` assinado.
- Teste do campo `messages` pelo painel Meta retornou sucesso.
- Payload de exemplo da Meta chegou na Vercel e acionou a IA.

## Evidências dos logs
Teste do botão da Meta:
- Vercel recebeu `POST /webhook/meta-whatsapp`.
- Resposta HTTP: `200`.
- IA acionada: log `[processMessage] starting for 16315551181`.
- `ai-route` gerou resposta via OpenAI.
- Erro final: `Meta WhatsApp error 400: (#131030) Recipient phone number not in allowed list`.

Interpretação: esse erro é esperado no teste do botão porque a Meta usa número fictício `16315551181`. Esse teste prova webhook/backend, mas não prova resposta para um WhatsApp real.

Teste real do José:
- Meta mostrou payload real com:
  - nome `José Wilson`
  - `wa_id: 553491036586`
  - texto `Oi teste`
  - `phone_number_id: 1173823579138528`
- Logs Vercel em janelas de 5, 15 e 30 minutos não mostraram novo `POST /webhook/meta-whatsapp` com esse payload.

Interpretação: a mensagem real existe na Meta, mas não foi entregue ao callback de produção. Isso aponta para configuração Meta/WABA, não para bug do adapter.

## Erros encontrados e leitura correta
- `invalid_verify_token` ao abrir `/webhook/meta-whatsapp` sem query é normal.
- `401 Authentication Error` no envio Cloud API ocorreu com token temporário antigo/inválido.
- `#131030 Recipient phone number not in allowed list` ocorreu em testes com destinatário fictício ou número ainda não permitido no ambiente de teste.
- Token da tela “Experimente” some/expira; não serve como solução final.
- Mensagens reais não chegando ao webhook mesmo com teste do botão funcionando indicam provável falta de `subscribed_apps` na WABA.

## Próximo passo definitivo
Criar token permanente de System User no Business Manager:

1. Ir para `business.facebook.com/settings`.
2. Abrir `Usuários > Usuários do sistema`.
3. Criar usuário do sistema Admin, por exemplo `concretize_whatsapp_system_user`.
4. Atribuir ativos com controle total:
   - App `IA CONCRETIZE`
   - WABA `2013351966214745`
5. Gerar novo token para o app `IA CONCRETIZE` com permissões:
   - `whatsapp_business_messaging`
   - `whatsapp_business_management`
6. Escolher expiração “Nunca” ou maior duração disponível.
7. Não colar o token em chat ou notas.

Depois assinar a WABA no app:

```http
POST https://graph.facebook.com/v25.0/2013351966214745/subscribed_apps
Authorization: Bearer NOVO_TOKEN
```

Resposta esperada:

```json
{ "success": true }
```

Confirmar:

```http
GET https://graph.facebook.com/v25.0/2013351966214745/subscribed_apps
Authorization: Bearer NOVO_TOKEN
```

Precisa aparecer o App ID `1330367675744725`.

Depois atualizar na Vercel:

```env
META_WHATSAPP_TOKEN=NOVO_TOKEN
```

Redeploy de produção após atualizar env.

## Teste final esperado
Depois do token permanente, `subscribed_apps` e redeploy:

1. José envia pelo WhatsApp pessoal para `+1 555 632 3563`.
2. Mensagem única sugerida: `teste jose depois subscribed apps`.
3. Logs esperados na Vercel:

```text
POST /webhook/meta-whatsapp 200
[processMessage] starting for 553491036586
[ai-route] ...
```

4. José deve receber resposta da IA no WhatsApp.

## Diagnóstico se ainda falhar
- Não aparece `POST /webhook/meta-whatsapp`: WABA ainda não está inscrita no app certo ou mensagem foi enviada para número errado.
- Aparece `401`: token inválido, expirado ou não atualizado na Vercel/redeploy ausente.
- Aparece `#131030`: destinatário não permitido no ambiente de teste.
- Aparece `200` sem erro de Meta: integração oficial funcionando.

## Centro de comando
Backend já expõe status Meta pelo endpoint admin `api/admin/wa-status.ts`.

O painel/centro de comando deve exibir, idealmente:
- Provider ativo: `meta-whatsapp` ou `megaapi`.
- Meta Cloud API configurada: token presente, phone number ID presente, WABA ID presente, verify token presente, app secret presente.
- Webhook verificado: GET challenge ok.
- Último webhook recebido.
- Último erro Meta Cloud API.
- Fallback MegaAPI disponível.
- Aviso quando token for temporário/401.
- Aviso quando WABA não tiver `subscribed_apps` confirmado.

Observação: a leitura de `subscribed_apps` exige token válido e chamada Graph API; pode ser implementada depois no status admin se quisermos que o painel detecte isso automaticamente.

## Integração antiga
A integração antiga MegaAPI não foi removida.

Estado esperado:
- Mensagens vindas de MegaAPI continuam usando envio MegaAPI.
- Mensagens vindas de Meta Cloud API usam envio Meta.
- A migração é incremental e reversível.

## Pendências reais
- Criar token permanente de System User.
- Executar `POST /2013351966214745/subscribed_apps`.
- Confirmar via `GET /2013351966214745/subscribed_apps` que o app está inscrito.
- Atualizar `META_WHATSAPP_TOKEN` na Vercel.
- Redeploy.
- Testar mensagem real do José para o número de teste Meta.
- Só depois planejar migração/adicionar o número real `+55 34 99718-3001` para produção.
- Rotacionar secrets expostos antes de produção real.

## Não fazer agora
- Não migrar o número real da Concretize pelo código antes do teste completo com número de teste.
- Não remover MegaAPI ainda.
- Não refazer prompt, memória, RAG ou lógica comercial.
- Não usar token temporário como solução definitiva.


---

## Atualização 2026-05-22 — Migração concluída em produção
Esta nota ficou histórica. O estado atual não é mais “pendente WABA/subscribed apps”.

Em 2026-05-22 a produção passou a operar com Meta WhatsApp Cloud API oficial:
- `https://concretize-ia.vercel.app` confirmou `whatsapp.status: connected`.
- Provider ativo: `meta-whatsapp`.
- Número conectado: `+55 34 9718-3001`.
- `officialCloudApiReady: true`.
- Mensagens reais aparecem no painel `https://concretize-insight-hub.vercel.app`.

Correções adicionais publicadas no mesmo ciclo:
- Imagem WebP do Supabase convertida para formato aceito pela Meta antes de enviar.
- Regras de entrega/frete local adicionadas.
- Follow-up de entrega usa histórico recente para não pedir cidade quando já recebeu rua/endereço.
- Respostas duplicadas reduzidas via batching e supressão de resposta recente igual.
- Linguagem de entrega para hoje foi protegida para não prometer disponibilidade sem confirmação.

Handoff atual completo: [[IA Concretize — Handoff Produção Meta e Entrega 2026-05-22]].

Segurança: tokens usados/colados durante a sessão devem ser revogados ou rotacionados. Valores de token não foram registrados nesta nota.
