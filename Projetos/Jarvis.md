---
title: "Jarvis"
type: projeto
created: 2026-03-26
tags: [projeto, automacao, ia, sistema-pessoal]
status: ativo
---

# Jarvis

## Objetivo
Sistema pessoal de automacao e memoria de Mestre. Opera via Telegram, Claude Code e VPS. Automacao 24/7.

## Arquitetura
- VPS: 72.60.9.212 — gateway OpenClaw 24/7, recebe Telegram
- PC (Wilson-PC): node pareado ao VPS via SSH tunnel, executa comandos locais
- OpenClaw: gateway de IA com Telegram, workspace /root/stark
- Claude: modelo principal (sonnet-4-5/4-6)

## Capacidades atuais
- Controle remoto do PC (screenshot, click, type, yes_terminal)
- Execucao de comandos via Telegram -> VPS -> PC
- Memoria persistente em 4 camadas (este sistema)
- Skills: computer, obsidian, gog, postgres, cloudflare-dns

## Status checklist
- [x] Gateway VPS rodando
- [x] PC node pareado
- [x] SSH tunnel automatico
- [x] Skill computer funcionando
- [x] Memoria 4 camadas (implementando)
- [ ] VPS configurado com embedding provider

## Relacionado
- [[ForYou Code]]
