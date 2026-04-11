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
- **IA Atendimento Rodrigo** (Concretize) — **Vendedor 3.1 Operacional**. Vercel ativo (HTTP 200), Cléo/profissional/08-18h, Redis+Supabase OK. Pendente: QR WhatsApp (Rodrigo) + image_url produtos.
- **Smartcell** — E-commerce eletrônicos Patos-PB, participação lucros.
- **ForYou Code** — Operação contínua.

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
*Ultima atualização: 2026-04-06*
