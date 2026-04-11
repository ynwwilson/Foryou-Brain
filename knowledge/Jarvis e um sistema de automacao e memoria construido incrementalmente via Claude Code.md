---
tipo: knowledge
tags: [jarvis, sistema, arquitetura]
atualizado: 2026-03-25
---

## Objetivo
Operar 24/7 como sistema pessoal de Mestre.

## Stack prevista
- Claude Code v2.1.81: cerebro principal
- OpenClaw: daemon 24/7 conectado ao Telegram
- Python bridge: conecta Claude Code a outros servicos
- AdsPower perfil 14: automacao de browser
- VPS Hetzner ou Oracle Cloud: infraestrutura 24/7

## Arquitetura de memoria (3 camadas)
Camada 1 (CONCLUIDA): CLAUDE.md + autoMemory + arquivos em ~/.claude/memory
Camada 2 (CONCLUIDA): Vault Stark em Projects/jarvis/stark, MCPs a instalar
Camada 3 (PENDENTE): brain-ingest para processar video/audio

## Filosofia de automacao
Codigo direto (Python/Node.js) + frontend em Lovable.
Nenhuma automacao fica so como script no terminal.

## Localizacao do projeto
C:\Users\ynwwi\Projects\jarvis

## Links relacionados
- [[atlas/Arquitetura do Jarvis|Canvas — Arquitetura do Jarvis]]
- [[atlas/vault-information-arch|Arquitetura do vault Stark]]