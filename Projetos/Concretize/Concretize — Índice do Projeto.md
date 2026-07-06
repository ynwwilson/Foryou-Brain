---
title: Concretize — Índice do Projeto
type: project-index
project: Concretize
updated: '2026-05-27'
status: prod2-midia-estruturada-painel-validado
tags:
  - concretize
  - indice
  - projeto
  - ia-atendimento
  - midia
  - prod2
---
# Concretize — Índice do Projeto

## Notas principais
- [[IA Concretize - Status Atual 2026-05-27]] — nota canônica atual: PROD2, midia estruturada, painel, deploys, validações e limites.
- [[IA Concretize - Pendencias e Proximos Passos 2026-05-27]] — checklist ativa do que ainda depende de teste real/dados reais.
- [[2026-05-27 23h46 - Concretize IA memoria completa midia painel e pendencias]] — sessão Codex completa com passo a passo da rodada de mídia/painel.
- [[IA de Atendimento Rodrigo]] — nota histórica e status geral acumulado do projeto.
- [[WhatsApp Cloud API — Migração Meta 2026-05-19]] — histórico da migração oficial Meta WhatsApp Cloud API.
- [[IA Concretize — Handoff Produção Meta e Entrega 2026-05-22]] — handoff anterior da virada Meta/produção e regras de entrega.

## Estado atual curto
A IA da Concretize está em produção no PROD2 com WhatsApp Cloud API oficial da Meta, backend `https://concretize-ia-prod2.vercel.app` e painel `https://concretize-insight-hub-prod2.vercel.app`.

A rodada mais recente fechou a camada de mídia: renderização no painel, transcrição de áudio moderna, PDF texto/escaneado, DOCX, vídeo, contrato estruturado `status/confidence/action`, proteção contra loops de instabilidade/reenvio e faixa operacional no Inbox indicando se a mídia foi entendida ou precisa revisão humana.

## Regra operacional atual
O próximo passo não é mais patch cego: é teste real no WhatsApp com imagem, áudio, PDF, DOCX, vídeo e arquivo ruim. Cada falha deve virar caso de eval/teste antes de novo ajuste de prompt ou pipeline.

## Segurança
Não armazenar tokens, App Secret, senhas ou chaves em notas. Se algum segredo foi exposto em sessões antigas, tratar como candidato a rotação. As notas novas registram apenas URLs, IDs de deploy, commits e comportamento técnico sem credenciais.
