---
updated: '2026-05-22'
last_project_context: >-
  IA Atendimento Rodrigo / Concretize — produção Meta Cloud API, imagens, frete
  e contexto corrigidos
---
# MEMORY.md — HOT Layer

> Bootstrap de contexto. Carregado no início de cada sessão. Max 6KB.
> MOC completo em: [[🧠 Meu Cerebro]]

---

## Quem e o Usuario
- **Mestre** — co-fundador ForYou Code, builder não-técnico, Brasil (GMT-3)
- Parceiros: Marco e Eduardo
- Estilo: direto, sem enrolação, automação primeiro, high-ticket

## Sistema Jarvis
- PC: Wilson-PC node, SSH tunnel porta 18790
- Controle remoto PC: funcionando (screenshot, click, type, yes_terminal)
- Telegram: Configurações pendentes de token no @BotFather.

## Empresa
- ForYou Code — ecossistema white-label B2B
- Stack fixada: Lovable / Antigravity / Claude Code / Vercel / Cloudflare / Supabase / Autentique
- Nunca sugerir n8n. Automações são código direto.

## Projetos Ativos
- **IA Atendimento Rodrigo** (Concretize) — produção ativa com Meta WhatsApp Cloud API oficial. Backend `concretize-ia.vercel.app`, painel `concretize-insight-hub.vercel.app`, provider `meta-whatsapp`, número `+55 34 9718-3001`, catálogo 30/30 imagens. Em 2026-05-22 foram corrigidos: imagem WebP/Supabase rejeitada pela Meta, duplicidade de respostas, promessa insegura de entrega hoje, regras de frete local e follow-up que perguntava cidade mesmo com rua no histórico. Nota atual: [[IA Concretize — Handoff Produção Meta e Entrega 2026-05-22]]. Segurança: revogar/rotacionar tokens usados na sessão.
- **Smartcell** — E-commerce eletrônicos Patos-PB, participação lucros.
- **ForYou Code** — Operação contínua.
- **ForYou Leads** — Sistema autônomo de prospecção no Instagram. Next.js + Vercel + Neon + AdsPower local + Claude Sonnet 4.6 + Playwright via CDP. Operacional em foryou-leads.vercel.app. Worker manda DMs com texto + vídeo, recovery automático com Claude Vision. Roadmap pós-auditoria em 5 fases — [[ForYou Leads — Roadmap Pós-Auditoria]]. Notas: [[Pipeline de Leads ForYou]].

## Aprendizados Críticos
- **Vercel Timeout:** Ocupado com `maxDuration: 30` para suportar delays de humanização de até 20s.
- **Dual-API Fallback:** Sempre implementar fallback Anthropic -> OpenAI para alta disponibilidade.
- **Mirroring:** IA deve adaptar tom ao cliente; proibido emojis e frases robóticas.
- **Resiliência:** Tratar mensagens < 15 chars ignorando lead scoring para economizar tokens.

## Ciclo de Memoria
```
Conversa -> memory/YYYY-MM-DD.md (raw)
         -> cron 02h processa
         -> atualiza MEMORY.md + notas Obsidian
         -> MOC atualizado semanalmente
```

---
*Ultima atualização: 2026-05-22*
