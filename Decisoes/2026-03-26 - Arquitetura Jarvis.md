---
title: "2026-03-26 - Arquitetura Jarvis"
type: decisao
created: 2026-03-26
tags: [decisao, jarvis, arquitetura, vps]
---

# Decisao: Arquitetura VPS + PC Node

## Contexto
Necessidade de controle remoto do PC via Telegram mesmo fora de casa.

## Decisao tomada
- VPS (72.60.9.212): gateway OpenClaw 24/7, unico receptor Telegram
- PC: node silencioso conectado via SSH tunnel (porta 18790 -> 18789 VPS)
- Telegram no PC desativado — so VPS recebe mensagens
- Node exec-approvals: security=full, ask=off

## Regra
Nunca ativar Telegram no PC gateway. So o VPS e o receptor oficial.

## Relacionado
- [[Jarvis]]
