---
tipo: knowledge
tags: [stack, antigravity, google, agentic, ide, ferramentas]
atualizado: 2026-03-25
---

# Google Antigravity

## O que é
IDE standalone da Google, lançado em 2025, com AI como fundação — não como complemento.
Fork do VS Code. Não é no-code: é **agentic-code** — você orquestra agentes que escrevem, testam e entregam código por você.
Substitui o Firebase Studio (descontinuado em 2027).
Site: antigravity.google

## Como funciona — 3 superfícies

| Superfície | O que faz |
|---|---|
| Editor | IDE com completions em linha — para edição direta |
| Terminal | Agentes rodam shell (Bash) para compilar, testar, debugar |
| Browser | Agente abre Chrome, interage com o app, tira screenshot, faz testes E2E |

## Dois modos de operação
- **Planning Mode:** agente gera plano com arquivos e estratégias antes de executar — você aprova
- **Fast Mode:** execução imediata para mudanças simples

## Manager Surface (Mission Control)
Orquestra múltiplos agentes em paralelo — um corrigindo bug no backend, outro refatorando frontend — ao mesmo tempo.

## Memória persistente
Pasta `.gemini/antigravity/brain/` guarda decisões arquiteturais do projeto. Agentes aprendem o projeto ao longo do tempo.

## Modelos suportados (grátis no preview)
Gemini 3 Pro · Claude Opus 4.6 · Claude Sonnet 4.6 · GPT-OSS 120B

## Stack que gera
- Frontend: React, Next.js, Flutter, Vue
- Backend: Node.js, Python, Go
- Estilos: Tailwind, Shadcn/UI
- Banco: Supabase (via MCP), Firebase
- Deploy: Vercel, Cloudflare Workers, Firebase Hosting

## Integração com nossa stack via MCP
- **Supabase MCP:** agente escreve migrations, debugs RLS, consulta schema live
- **Vercel MCP:** monitora deployments, lê build logs, faz debug server-side
- **Cloudflare MCP (Wrangler):** gerencia Workers, R2, tail logs de edge functions

## Integração com Google Stitch
Design em linguagem natural → Stitch gera telas → Antigravity converte para código React/Flutter.
Fluxo completo para apps simples: ~23 minutos.

## Como Lovable e Antigravity funcionam juntos (fluxo de trabalho)

Não são concorrentes — são fases do mesmo pipeline de entrega:

```
1. Lovable
   → Constrói o frontend rápido
   → Visualiza a UI em tempo real
   → Conecta ao repositório GitHub do projeto

2. Antigravity
   → Acessa o mesmo repositório GitHub
   → Melhora o código 20x com agentes autônomos
   → Refatora, adiciona lógica complexa, roda testes E2E

3. Claude Code
   → No mesmo repositório GitHub
   → Executa tarefas via terminal: automações, scripts, integrações,
     ajustes cirúrgicos, o que for mais rápido ou que os outros não alcançam

4. Lovable (preview atualizado)
   → Reflete automaticamente qualquer mudança commitada no GitHub
   → Não importa quem fez — Antigravity, Claude Code ou manual
```

**Os três trabalham no mesmo repositório. Nenhum substitui o outro.**
Lovable = velocidade e visão. Antigravity = profundidade e agentes. Claude Code = controle e precisão.

## Preços
- Free (preview): acesso com rate limits, inclui todos os modelos top
- AI Pro: ~$20/mês
- AI Ultra: $249,99/mês
- Créditos avulsos: $25 para 2.500

## Status
Em public preview (março 2026). Bugs e rate limits instáveis documentados.
Não usar para produção crítica ainda — ideal para greenfield e projetos novos.

## Benchmarks
- SWE-bench Verified: 76,2%
- Terminal-Bench 2.0: 54,2%
- Ranking LogRocket março 2026: 2º lugar entre todos os AI dev tools

## Atenção
Modo Auto pode executar comandos destrutivos sem avisar (ex: `chmod -R 777`).
Usar Planning Mode em projetos críticos — revisar o plano antes de aprovar execução.

## Links relacionados
- [[atlas/Decisoes de stack da ForYou Code|Decisões de stack]]
- [[atlas/Arquitetura do Jarvis|Arquitetura do Jarvis]]
