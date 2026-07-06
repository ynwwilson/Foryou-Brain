---
title: Status Atual — 2026-05-23 Migração Vercel
type: status
project: Concretize IA
client: Rodrigo / Concretize Pré Moldados
created: '2026-05-23'
updated: '2026-05-23'
tags:
  - concretize
  - ia-atendimento
  - meta-cloud-api
  - vercel
  - status
  - producao
status: backend-prod2-pronto-aguardando-troca-webhook-meta
---
# Status Atual — 2026-05-23 Migração Vercel

## Resumo executivo
A Concretize foi restaurada em cópia paralela no workspace Vercel ativo `yngomesmarco-hue's projects`, sem apagar os projetos antigos e sem trocar ainda o webhook da Meta. O backend novo está online, público, conectado à Meta Cloud API oficial, com IA apta a responder. O painel novo também está online.

A produção antiga continua bloqueada por billing no workspace `ynwwilson-9617's projects`, retornando `402 Payment Required / DEPLOYMENT_DISABLED`.

## Workspace antigo bloqueado
- Team: `ynwwilson-9617's projects`
- Team ID: `team_9Ppcz2paqfrLcUMhkMHgSgEx`
- Estado: `Overdue`
- Backend antigo: `concretize-ia`
- Painel antigo: `concretize-insight-hub`
- URLs antigas:
  - `https://concretize-ia.vercel.app`
  - `https://concretize-insight-hub.vercel.app`
- Estado das URLs antigas: `402 Payment Required / DEPLOYMENT_DISABLED`

## Workspace ativo usado
- Team: `yngomesmarco-hue's projects`
- Team ID: `team_uZU2DYDtmcTe4QYFnquE3EqJ`
- Estado visual: Pro ativo

## Backend novo
- Projeto: `concretize-ia-prod2`
- Project ID: `prj_LKh0oH60D7dbbUrciD4MqybXVFmb`
- URL pública temporária: `https://concretize-ia-prod2-yngomesmarco-hues-projects.vercel.app`
- Último deployment validado: `dpl_F7Hc1mu1DeYEp7GZjcuiNYfKQm8q`
- Status Vercel: `READY`
- Vercel Authentication: desativado no projeto temporário, necessário para webhook Meta público.

### Status `/api/status` após última validação
- HTTP: `200 OK`
- `whatsapp.status`: `connected`
- `whatsapp.phone`: `+55 34 9718-3001`
- `activeProvider`: `meta-whatsapp`
- `officialCloudApiReady`: `true`
- `webhookCanProcess`: `true`
- `primaryAiReady`: `false`
- `fallbackAiReady`: `true`
- `aiCanProcessReplies`: `true`

Interpretação: Meta oficial pronta e IA apta a responder usando OpenAI disponível. Gemini não está configurado, por isso `primaryAiReady` fica `false` no status atual.

## Painel novo
- Projeto: `concretize-insight-hub-prod2`
- Project ID: `prj_yK4qQh5zhYz35B7VMp4j0CoXKgZL`
- URL pública temporária: `https://concretize-insight-hub-prod2-yngomesmarco-hues-projects.vercel.app`
- Deployment validado: `dpl_5NdYLogGBuDtK9zEbMavkQaSaCKK`
- Status Vercel: `READY`
- Vercel Authentication: desativado no projeto temporário.
- Validação: HTTP `200 OK`, build Vite concluído.

## Meta WhatsApp Cloud API
- WABA da Concretize: `1555241252688170`
- Phone Number ID: `1159981177197401`
- Número real conectado: `+55 34 9718-3001`
- Conta WhatsApp: `Concretize Pré Moldados`
- System User: `concretize_admin`, ID `61589978737217`
- App: `IA CONCRETIZE`
- Token Meta foi cadastrado no backend novo e validado pelo `/api/status`.

## O que foi feito
1. Criada pasta local de dossiê: `C:\Users\ynwwi\Concretize IA`.
2. Exportadas env vars dos projetos antigos quando possível.
3. Criados projetos paralelos no workspace ativo:
   - `concretize-ia-prod2`
   - `concretize-insight-hub-prod2`
4. Importadas env vars recuperáveis.
5. Removidas variáveis indevidas de sistema (`VERCEL_*`, `TURBO_*`, `NX_DAEMON`) dos projetos novos.
6. Inseridos manualmente os dados Meta que a Vercel não devolveu:
   - `META_PHONE_NUMBER_ID`
   - `META_WABA_ID`
   - `META_WHATSAPP_TOKEN`
7. Inseridas chaves de IA encontradas em `APIS.txt`:
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`
8. Redeployado backend novo.
9. Validado backend novo com `/api/status`.
10. Validado painel novo com HTTP 200.

## O que NÃO foi feito
- Não foi trocado o webhook da Meta ainda.
- Não foram apagados projetos antigos.
- Não foram transferidos domínios antigos.
- Não foi mexido no billing antigo.
- Não foi feita alteração de código para Anthropic fallback.

## Próximo passo obrigatório
Trocar no painel Meta o callback do webhook para:

```text
https://concretize-ia-prod2-yngomesmarco-hues-projects.vercel.app/webhook/meta-whatsapp
```

Manter o mesmo verify token já configurado.

Depois testar:
1. Mensagem simples no WhatsApp real.
2. Resposta da IA.
3. Conversa aparecendo no painel novo.
4. Pedido com produto, frete e imagem.

## Atenção sobre Anthropic
A chave `ANTHROPIC_API_KEY` foi cadastrada no projeto novo porque o usuário pediu Anthropic como fallback. Porém o código atual da Concretize não usa Anthropic no runtime principal; há teste indicando que o runtime atual centraliza Gemini/OpenAI e não depende de Anthropic. Para usar Anthropic de fato como fallback, precisa alteração de código e testes.
