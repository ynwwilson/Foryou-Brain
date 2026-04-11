---
tags: [tipo/referencia, projeto/foryoucode]
data: 2026-03-31
---

# ORCHESTRATION.md — Como os Agentes se Comunicam

> Este arquivo define o protocolo de orquestração do sistema Jarvis.
> Lido pelo Stack Coordinator antes de qualquer delegação.

---

## Hierarquia

```
Mestre (José)
    └── Stack Coordinator ← ponto de entrada de toda tarefa grande
            ├── UX Agent
            ├── UI Agent
            ├── Frontend Agent
            ├── Backend Agent
            ├── Security Agent
            ├── Architect Agent
            ├── DevOps Agent
            ├── QA Agent
            ├── Vendas Agent
            ├── Data Agent
            └── Manus Agent
```

---

## Protocolo de handoff

Todo agente que termina seu trabalho **deve** criar ou atualizar `handoff.md` com:

```markdown
## Handoff de: [nome-do-agente]
### Para: [nome-do-próximo-agente]
### Data: YYYY-MM-DD

**O que foi feito:**
- [lista de outputs produzidos com caminhos de arquivo]

**O que você precisa saber:**
- [decisões tomadas]
- [restrições descobertas]
- [pontos de atenção]

**Seu próximo passo:**
1. [instrução clara]
2. [instrução clara]

**Arquivos gerados:**
- `[caminho/arquivo.md]` — [descrição]
```

---

## Fluxos canônicos

### Produto novo (app completo)
```
Stack Coordinator
  → UX Agent          [output: user-flows.md, personas.md]
  → UI Agent          [output: design-spec.md, tokens.css]
  → Architect Agent   [output: architecture.md]
  → Backend Agent     [output: API, banco de dados]
  → Frontend Agent    [output: UI implementada]
  ↔ integração Backend ↔ Frontend
  → QA Agent          [output: testes, validação]
  → Security Agent    [output: security-review.md]
  → DevOps Agent      [output: deploy em produção]
  → Stack Coordinator [relatório final para Mestre]
```

### Conteúdo + venda
```
Stack Coordinator
  → Vendas Agent      [output: proposta.md ou script]
  → Data Agent        [output: métricas de suporte]
  → Stack Coordinator [draft para aprovação do Mestre]
```

### Operação Meta
```
Stack Coordinator
  → lê Obsidian       [persona + funil + contexto]
  → Manus Agent       [executa: post / campanha / mensagem]
  → salva Obsidian    [resultado + print]
  → Stack Coordinator [relatório para Mestre]
```

### Análise de dados
```
Stack Coordinator
  → Data Agent        [output: relatório em Markdown]
  → Stack Coordinator [relatório para Mestre]
```

---

## Agentes por tipo de tarefa

| Tarefa recebida | Primeiro agente a acionar |
|---|---|
| "cria um app/sistema" | UX Agent |
| "faz o design de X" | UI Agent (se UX já feito) |
| "implementa a tela" | Frontend Agent |
| "cria a API" | Backend Agent |
| "configura o banco" | Backend Agent |
| "faz o deploy" | DevOps Agent |
| "revisa segurança" | Security Agent |
| "testa X" | QA Agent |
| "define a arquitetura" | Architect Agent |
| "cria proposta para X" | Vendas Agent |
| "analisa métricas" | Data Agent |
| "posta no Instagram" | Manus Agent |
| "cria anúncio" | Manus Agent |
| "não sei qual agente" | Stack Coordinator decide |

---

## Regras de paralelismo

**Pode rodar em paralelo:**
- Backend Agent + Frontend Agent (após UI spec estar pronta)
- Data Agent + Vendas Agent

**NÃO pode rodar em paralelo:**
- UX Agent e UI Agent (UI depende de UX)
- Frontend Agent e Security Agent (Security revisa Frontend)
- Qualquer agente e DevOps Agent (deploy sempre por último)

---

## Registro de orquestração

Cada delegação deve ser registrada em `Agentes/memória/sessions/YYYY-MM-DD.md`:

```markdown
## [HH:MM] Orquestração
- Tarefa: [descrição]
- Agente acionado: [nome]
- Input dado: [resumo]
- Output esperado: [resumo]
- Status: [pendente / concluído / bloqueado]
```

---

## Escalada para Mestre

Escalar imediatamente quando:
- Agente travou por mais de 2 tentativas
- Tarefa não se encaixa em nenhum agente conhecido
- Decisão de negócio necessária (novo cliente, pricing, parceria)
- Budget ou prazo em risco
- Erro em produção
