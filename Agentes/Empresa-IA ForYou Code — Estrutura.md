---
tipo: arquitetura
criado: 2026-05-27
atualizado: 2026-05-27
status: planejado — nenhum agente construído ainda
fonte: sessão "[[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]"
---

# Empresa-IA ForYou Code — Estrutura

Plano de empresa-IA virtual: **8 C-Levels** + **~40 funcionários** sub-especialistas pra rodar a ForYou Code.

## Filosofia

- **Você (Mestre) = CEO**: decide direção, aprova última instância
- **8 C-Levels** = diretores IA por área
- **~40 funcionários** = especialistas sob cada C-Level
- **Marco e Eduardo** = stakeholders com escopo limitado (CMO/CRO)

## Diagrama

```
                    VOCÊ (CEO / Mestre)
                          │
                  ┌───────┴────────┐
                  │  COORDINATOR   │  ← mediador único entre depts
                  │  (agente IA)   │
                  └───────┬────────┘
                          │
    ┌────┬─────┬─────┬────┼────┬─────┬─────┬─────┐
    │    │     │     │    │    │     │     │     │
   CTO  CMO   CRO   COO  CFO  CPO   CCO   CSO  ...
    │    │     │     │    │    │     │     │
  [func][func][func][func][func][func][func][func]

       ┌────────────────────────────────────┐
       │   BLACKBOARD (memória persistente) │
       │   todos escrevem/leem aqui         │
       └────────────────────────────────────┘
```

---

## Estrutura por departamento

### 🛠️ CTO — Tecnologia
Funcionários:
- Arquiteto (decide stack — Lovable vs Astro vs TanStack)
- Dev Frontend
- Dev Backend (Vercel Functions / Modal)
- DevOps (Cloudflare / Vercel / DNS)
- QA (Playwright / testes)
- Security (LGPD / OWASP)
- Migrator (Lovable → Vercel/Cloudflare)

### 📣 CMO — Marketing
Funcionários:
- Copywriter
- SEO
- Social Media Mestre (sua voz)
- Social Media Marco (voz dele)
- Social Media Eduardo (voz dele)
- Brand Guardian (paleta P&B editorial)
- Conteúdo (Infinity Content)
- Análise de tendências

### 💰 CRO — Vendas + Tráfego Pago
Funcionários:
- SDR (qualifica lead Okara/Zernio)
- Closer (fecha proposta)
- Negociador (preço/escopo R$1.500-2.000 saúde)
- Meta Ads
- Google Ads
- TikTok Ads
- Designer de criativos
- Analista de ROAS

### ⚙️ COO — Operações
Funcionários:
- Gestor de projetos (5+ clientes simultâneos)
- Onboarding (recebe cliente novo)
- SLA watcher (responde no prazo)
- Coordenador 3 sócios

### 💵 CFO — Financeiro
Funcionários:
- Precificador (R$1.500 vs 2.000 vs custom)
- Contas a pagar/receber
- Análise rentabilidade por cliente
- Impostos / MEI

### 📦 CPO — Produto
Funcionários:
- Research (entender ICP saúde/estética)
- Roadmap quarterly
- Feature dev (usa skill `feature-dev` Anthropic)
- Validador de ideia

### ❤️ CCO — Customer Success
Funcionários:
- Suporte 1º nível
- Retenção
- Upsell (modelo Smartcell 20%)
- Health check (uptime watchman)

### ⚖️ CSO — Estratégia + Jurídico
Funcionários:
- Análise competitiva trimestral
- Contratos (template MVP)
- LGPD (clínica saúde)
- Termos de uso

---

## Padrão de comunicação inter-agente

### Coordinator Pattern

Nenhum agente chama outro **direto**. Tudo passa pelo Coordinator.

### Blackboard

Toda decisão escrita em formato padrão na memória persistente:

```yaml
id: META-2026-05
status: definido | em_andamento | concluído
quem_escreveu: CRO
o_que: <decisão>
porque: <justificativa>
timestamp: 2026-05-27T23:45:00
referencias: [outros-ids]
```

### Protocolo de mensagem entre agentes

Formato fixo (max 500 tokens):

```yaml
de: CMO
para: CRO
topic: <assunto>
context-id: <id no blackboard>
needed: <o que precisa>
deadline: <quando>
```

### Resposta também fixa:

```yaml
de: CRO
para: CMO (via Coordinator)
context-id: <mesmo>
decision: <resposta>
rationale: <por quê>
dependencies: <outros agentes a chamar>
```

---

## 5 regras técnicas anti-quebra

| # | Regra | Mata |
|---|---|---|
| 1 | Sempre via Coordinator | Loop infinito |
| 2 | Blackboard = verdade compartilhada | Perda de contexto |
| 3 | Max 3 rounds entre agentes | Discussão sem fim → escala pro CEO |
| 4 | Token cap 500/mensagem | Token explosion |
| 5 | Loop detector | Recursão (mesmo agente 2x na cadeia) |

---

## Cenário real — CMO ↔ CRO

**Mestre:** "preciso +R$10k até dia 30"

1. **Coordinator → CRO** → CRO define meta (5 vendas MVP)
2. **CRO escreve no blackboard** → meta documentada
3. **CRO → Coordinator → CMO** → CMO sugere 3 funis + budget R$2k + ROAS 5x
4. **CMO escreve no blackboard** → campanha documentada
5. **Coordinator detecta** budget >R$1k → precisa CFO aprovar
6. **Coordinator → CFO** → aprova com gate de revisão dia 30
7. **Coordinator → Você** → resumo 5 linhas + tudo registrado no vault

**Sem loop. Sem perda. Conflito resolvido pelo agente apropriado (CFO foi juiz no budget).**

---

## O que JÁ TEMOS pra construir

| Componente | Status |
|---|---|
| **claude-flow / Ruflo MCP** (314 tools, swarm coordination nativa) | ✅ instalado |
| **Memória persistente** (vira blackboard) | ✅ existe |
| **subagent-driven-development** skill | ✅ |
| **dispatching-parallel-agents** skill | ✅ |
| **skill-creator** | ✅ |
| **handoff** | ✅ |
| **verification-before-completion** | ✅ |

**Não precisa instalar nada novo.** Só construir.

---

## O que FALTA construir

### Fundação (~2-3h)
1. **Glossário ForYou Code** (vault) — MVP, ICP, voz Marco/Eduardo/Mestre, lead quente, etc
2. **Tabela de stakeholders** (vault) — quem aprova o quê
3. **Lista mestre URLs prod** (vault)
4. **Blackboard Protocol** (formato fixo de mensagem)
5. **Coordinator Agent** (mediador)

### MVP (~3h)
6. **CMO** agente + 2-3 funcionários básicos
7. **CRO** agente + 2-3 funcionários básicos
8. **Validar** com cenário real (campanha aquisição)

### Escala (~6-8h)
9. Demais 6 C-Levels
10. Funcionários sob demanda

**Total estimado:** ~11-14h em 2-3 semanas.

---

## Trade-off Claude Small Business

Se Mestre assinar **Claude for Small Business** (US$25-150/seat/mês, 14 dias trial):
- **Já vem com 15 workflows oficiais** divididos por dept (finance/ops/sales/marketing/HR/CS)
- **HubSpot integrado** (vira CRM)
- **DocuSign integrado** (contratos)
- **QuickBooks integrado** (financeiro)
- **Aprovação humana obrigatória** antes de ação externa
- **3 seats (você + Marco + Eduardo)** = ~R$1.700/mês

Decisão: **fazer trial primeiro**. Se vale, construir empresa-IA por cima dos workflows oficiais (não duplicar). Se não, construir do zero.

---

## Conexões

- Sessão origem: [[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]
- Plano operacional: [[Plano Operacional ForYou Code]]
- Arsenal: [[Arsenal IA ForYou Code]]
- Credenciais necessárias: [[Credenciais a Coletar]]
- Papéis dos sócios: [[ForYou Code]]
