---
tipo: knowledge
tags: [jarvis, antigravity, arquitetura, automacao, computer-use]
atualizado: 2026-03-28
---

# 🏗️ Arquitetura Integrada: Antigravity + Jarvis Computer Use

Este documento cristaliza as decisões arquiteturais e a infraestrutura implementada para o ecossistema Jarvis e Antigravity operando localmente e via VPS.

## 1. Jarvis com Visão e Computer Use

O bot Jarvis (interface via Telegram) recebeu um salto evolutivo para controle físico da máquina Windows:
- **Camada Física (computer_use.py)**: Construída nativamente usando PyAutoGUI para controle de mouse e teclado, em conjunto com a lib mss para capturas de tela ultrarrápidas, entregues ao modelo como Base64.
- **Cognição Multimodal (main_new.py)**: O loop do agente foi elevado para até 15 iterações. A IA interage chamando computer_action ou 
un_shell_command, "vendo" a tela a cada passo e tomando a próxima decisão.
- **Segurança Reforçada**: Módulo travado a um chat_id master, protegendo a máquina de execuções não autorizadas. 

## 2. Servidores Model Context Protocol (MCP)

No plano de comunicação universal com IAs, o arquivo mcp_config.json padronizou fontes de dados vitais:
- **GitHub MCP**: Integração total com CI/CD e versionamento.
- **Obsidian MCP**: Acesso em tempo real em loopback (localhost:27124) ao vault de cérebros.
- **Postgres MCP**: Infraestrutura preparada via Supabase, apenas aguardando a string de conexão na arquitetura.

## 3. Playbooks e Workflows do Antigravity

Foram configuradas quatro diretrizes essenciais no sandbox .agent/workflows/ para acelerar orquestrações:
1. **/activate-skills**: Injeta as rulesets e knowledge do skill_manager.py no contexto.
2. **/deploy-totus**: Blueprint de deploy automatizado focado em Continuous Delivery (lint -> build -> Vercel) para o Totus AI Concierge.
3. **/manage-skills**: Controle fino de contexto, permitindo debloat do prompt a qualquer instante (purge/clear/status).
4. **/new-project**: Automação formadora de base tech-stack. Criação unificada usando Next.js 14, Pnpm, Zod, e Tailwind.

## 4. User Rules / Postura de Sistema

A mente das IAs do ecossistema agora incorpora a "Essência de Mestre":
- **Mindset**: Viés forte para a ação ("não explique, faça"). 
- **Tom de Voz**: Direto, zero enrolação, proibido respostas clichês corporativas como "ótima pergunta".
- **Engenharia**: Sempre que possível codificar automações usando scripts fortes (Node/Python) emparelhados a UIs modulares (Lovable), recusando sistemas block-builders como n8n se a lógica couber em código puro.
- **Stack Canônica**: Todo deployment respira o fluxo: Lovable → Vercel → Supabase → Cloudflare.

---
> **Snapshot**: Memória extraída e arquivada durante a finalização do setup agêntico da Sprint de 28/03/2026.
