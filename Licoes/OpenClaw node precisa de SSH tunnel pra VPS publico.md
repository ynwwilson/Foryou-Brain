---
title: "OpenClaw node precisa de SSH tunnel pra VPS publico"
type: licao
created: 2026-03-26
tags: [licao, openclaw, vps, infraestrutura]
---

# OpenClaw node precisa de SSH tunnel pra VPS publico

## O que aconteceu
Tentativa de conectar node ao VPS via ws:// falhou com erro de seguranca. A env var OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 so funciona para IPs privados.

## O que aprendi
Para IP publico, obrigatorio usar SSH tunnel ou TLS. Solucao implementada: tunnel SSH na porta 18790 local -> 18789 VPS.

## Como aplicar
- Node conecta em 127.0.0.1:18790
- SSH tunnel: ssh -N -L 18790:127.0.0.1:18789 root@72.60.9.212
- Token no node.cmd: OPENCLAW_GATEWAY_TOKEN=...

## Relacionado
- [[Jarvis]]
- [[2026-03-26 - Arquitetura Jarvis]]
