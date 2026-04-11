---
tipo: atlas
tags: [stack, decisoes, tecnico]
atualizado: 2026-03-28
---

# Decisoes de Stack da ForYou Code

> Cada ferramenta tem um papel especifico. Antigravity lidera a construcao. Lovable complementa com preview.

---

## Stack completa

| Camada | Ferramenta | Para que serve |
|---|---|---|
| **Construcao principal** | **Google Antigravity** | Constroi apps, sites e sistemas completos. Motor principal — logica complexa, testes E2E, refatoracao, agentes autonomos |
| Preview + ajustes rapidos | Lovable | Alteracoes basicas de UI, preview em tempo real. Reflete automaticamente qualquer commit no GitHub |
| Terminal agentico | Claude Code | Executa tarefas via terminal: automacoes, scripts, integracoes, ajustes cirurgicos |
| Deploy | Vercel | Frontend e serverless functions |
| CDN / DNS | Cloudflare | Edge, performance, Workers |
| Banco de dados | Supabase | PostgreSQL, auth, storage, realtime |
| Contratos | Autentique | Assinatura digital com clausula de omissoes |

> **Hierarquia:** Antigravity eh o motor principal de construcao. Lovable eh complementar — preview rapido e ajustes visuais basicos. Push no Git = atualiza no Lovable automaticamente.

---

## Fluxo de trabalho — todos no mesmo repositorio

```
Antigravity (motor principal)
→ Constroi apps e sistemas completos do zero
→ Logica complexa, refatoracao, testes E2E, agentes autonomos
→ Puxa e committa no GitHub

Lovable (preview + ajustes rapidos)
→ Edicoes visuais basicas, preview em tempo real
→ Reflete automaticamente qualquer commit feito por qualquer ferramenta
→ Conectado ao mesmo repo GitHub — push = atualiza preview

Claude Code (terminal + automacoes)
→ No mesmo repo, executa tarefas especificas via terminal
→ Automacoes, scripts, integracoes, ajustes cirurgicos
→ O que os outros nao alcancam ou o que for mais rapido aqui
```

Os tres trabalham no **mesmo repositorio GitHub**. Antigravity lidera a construcao. Lovable complementa com preview. Claude Code executa no terminal.

---

## Automacoes

- Filosofia: codigo direto via Claude Code — sem n8n
- Toda automacao ganha frontend em Lovable
- Bridge: Python conectando Claude Code a outros servicos

---

## Por que nao n8n
Decisao tomada em marco 2026.
Mais controle, menos dependencia de ferramenta visual, melhor integracao com Claude Code.

---

## Links relacionados
- [[knowledge/Google Antigravity e o IDE agentico da Google para construir apps com agentes de IA|Antigravity — detalhes completos]]
- [[knowledge/ForYou Code constroi o ecossistema digital que o cliente precisar dentro do proprio app dele|O que a ForYou Code entrega]]
- [[knowledge/Processo de entrega de projetos na ForYou Code|Processo de entrega]]
