---
title: Concretize IA Meta produção frete imagens
date: '2026-05-22'
project: Concretize
type: session-handoff
tags:
  - codex
  - concretize
  - handoff
  - meta-cloud-api
  - frete
---
# Sessão — Concretize IA Meta produção, frete e imagens

## Resultado da sessão
A IA da Concretize está em produção com WhatsApp Cloud API oficial da Meta.

Status validado:
- Backend: `https://concretize-ia.vercel.app`
- Painel: `https://concretize-insight-hub.vercel.app`
- Provider ativo: `meta-whatsapp`
- Número: `+55 34 9718-3001`
- `officialCloudApiReady: true`
- Catálogo: 30 produtos, 30 com imagem
- Deploy final: `dpl_Hr1EKVaMmN54i7uZci4hzdPKYMin`
- Alias: `https://concretize-ia.vercel.app`

## Nota completa
Handoff completo salvo em: [[IA Concretize — Handoff Produção Meta e Entrega 2026-05-22]]

Índice atualizado: [[Concretize — Índice do Projeto]]

Nota histórica atualizada/supersedida: [[WhatsApp Cloud API — Migração Meta 2026-05-19]]

## O que foi corrigido
- Meta Cloud API oficial conectada ao número real.
- Imagens WebP do Supabase não chegavam no WhatsApp porque a Meta recusava `image/webp`; agora URLs são normalizadas para render JPEG compatível.
- Respostas duplicadas foram mitigadas com batching e supressão de resposta recente igual.
- Linguagem de entrega para hoje foi protegida para não prometer disponibilidade sem confirmação.
- Regras de frete/entrega adicionadas:
  - blocos/canaletas: R$ 70 dentro da cidade;
  - bloquetes/pavers: R$ 700 até 50m² dentro da cidade; grátis a partir de 100m²;
  - cobogós: R$ 70 até 15 unidades; grátis acima de 15;
  - pisos de passeio: R$ 70 até 30m²; grátis acima disso.
- Follow-up de entrega agora usa histórico recente; se o cliente já falou rua/endereço, a IA não deve perguntar cidade de novo.
- `4 pontas` agora pode ser ligado ao produto `Cobogó 4 Pontas` pelo catálogo.

## Caso crítico testável
Frase do cliente:
```text
Quanto fica aqui na artur magalhaes 1350 20 unidades do 4 pontas
E quanto é a entrega?
```

Resposta esperada:
```text
20 unidades do Cobogó 4 Pontas ficam R$ 860,00.
Para essa quantidade, a entrega dentro da cidade fica grátis.
```

Não deve perguntar cidade, porque `aqui na artur magalhaes 1350` já é contexto local/endereço.

## Validações executadas
- `rtk npm test -- tests/reply-rules.test.js` passou.
- `rtk npm test -- tests/webhook-source.test.js` passou.
- `rtk npm run build` passou.
- Deploy Vercel produção passou.
- `rtk curl.exe -sS https://concretize-ia.vercel.app/api/status` confirmou Meta conectada.

## Segurança
Tokens técnicos foram usados durante a sessão, mas não foram salvos nas notas. Wilson deve revogar/rotacionar token Vercel e tokens Meta temporários usados no chat.

## Próximo passo
Testar no WhatsApp real:
1. imagem de produto;
2. `20 unidades do 4 pontas` com rua/local;
3. follow-up `quanto é a entrega?`;
4. casos das quatro regras de frete.

Se falhar, pegar horário exato e logs Vercel, depois verificar `lib/replyRules.ts`, `lib/aiRouter.ts`, batching em `api/webhook.ts`/`lib/redis.ts`.
