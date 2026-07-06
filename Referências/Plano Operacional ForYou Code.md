---
tipo: referência
criado: 2026-05-27
atualizado: 2026-05-27
fonte: sessão "[[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]"
status: pendente — nenhuma sprint executada ainda
---

# Plano Operacional ForYou Code

Plano de operação real. **Não é arsenal IA** — é o que tem que existir no MUNDO REAL pra ForYou Code não quebrar e escalar.

## Diagnóstico inicial

Após instalar arsenal cognitivo completo (~150 skills, ~70 agentes, MCPs), o gap principal é **operacional**, não tecnológico:

> "Mestre é construtor com motosserra premium mas sem capacete."

3 sites em prod (Smartcell, LocaMotoFácil, Imerso) sem observabilidade. Sem backup. Sem CRM. Sem testes regressão. Cliente real, dinheiro real, risco real.

---

## Modos de trabalho

| Modo | Quando | Stack de skills |
|---|---|---|
| **Supervisão (GSD)** | Feature com design, prod sensível | brainstorming → writing-plans → executing-plans → verification → finishing-branch |
| **Loop autônomo (Ralph)** | Tarefa longa com critério verificável (uptime, testes noturnos) | ralph-loop estrutura → dispatching-parallel-agents executa → verification gate |
| **Paralelo (subagentes)** | Sprints independentes em arquivos diferentes | subagent-driven-development + git-worktrees |

Regra: toda sprint fecha com `verification-before-completion`.

---

## FASE 0 — Setup já feito ✅

(Em 2026-05-27)
- ~150 skills + 8 marketplaces instalados nas 4 contas
- ~70 agentes ativos
- Ruflo (claude-flow) MCP nas 4 contas
- Codex 2 sincronizado com agentes do Codex 1

---

## FASE 1 — Stop the bleeding (esta semana, ~5h) — PENDENTE

### 🔴 Sprint 1.1 — Observabilidade prod (MAIS CRÍTICA)
**Objetivo:** Smartcell, LocaMotoFácil e Imerso alertam no Telegram em downtime.

**Tempo:** ~1h
**Stack:** brainstorming → writing-plans → browser-use (criar conta monitor) → executing-plans → verification

**Critério de sucesso verificável:** simular queda → receber Telegram <60s.

**Risco se ignorar:** Smartcell tem **20% de participação nos lucros**. Cai sem você ver = perde dinheiro real.

### 🟡 Sprint 1.2 — Git dotfiles
**Objetivo:** `.claude/`, `.claude-nova/`, `.codex/`, `.codex-plus-2/` configs versionados.

**Tempo:** ~1h
**Stack:** writing-plans → using-git-worktrees → executing-plans → requesting-code-review → verification

**Crítico:** **NUNCA** commitar `auth.json`, `.credentials.json`, `cap_sid`, `.codex-global-state.json`, `installation_id`.

### 🔴 Sprint 1.3 — Backup Smartcell
**Objetivo:** snapshot semanal do banco de pedidos/cadastros Smartcell.

**Tempo:** ~1-2h
**Stack:** brainstorming → systematic-debugging (entender onde dado vive) → writing-plans → TDD (script faz dump+restore?) → executing-plans → verification

---

## FASE 2 — Operação ferro (próximas 2 semanas, ~6-8h) — PENDENTE

### Sprint 2.1 — Testes E2E agendados (~2-3h)
Playwright + GitHub Actions cron 1x/dia rodando contra Smartcell e LocaMotoFácil. Falha → Telegram.

### Sprint 2.2 — Vault como source-of-truth (~2h)
Template padrão de projeto + Dataview dashboard mostrando todos os 5+ projetos com status, próximo passo, link prod, link git, % completo.

### Sprint 2.3 — Skill "novo cliente ForYou Code" (~1-2h)
Encapsular padrão de setup em skill custom usando **skill-creator** (já instalado). Próximo cliente sai de 3 dias pra 30 minutos.

---

## FASE 3 — Refino (mês 2, opcional) — PENDENTE

| Sprint | Skill principal |
|---|---|
| Time-tracking por sessão | skill-creator (tag automática em auto-save) |
| Runbooks automatizados | skill-creator + handoff |
| Custos consolidados infra IA | browser-use (login persistente em cada billing) + ralph-loop |
| SLA formal cliente | brainstorming + template no vault |

---

## Trilha paralela — empresa-IA

Plano operacional acima é o "negócio funcionando". Mas há outra trilha em paralelo: **construir a empresa-IA virtual** (8 C-Levels + funcionários).

Ver [[Empresa-IA ForYou Code — Estrutura]] pra detalhes.

Ordem sugerida:
1. Glossário ForYou Code (~30min)
2. Tabela de stakeholders (~30min)
3. Lista mestre URLs prod (~15min)
4. Coordinator Agent + Blackboard (~2h)
5. CMO + CRO (par mais doloroso) (~3h)
6. Validar cenário real
7. Escalar pros outros 6 C-Levels

**Trial Claude Small Business em paralelo** (14 dias grátis, https://claude.com/pricing) — pode resolver várias lacunas operacionais de uma vez (HubSpot, DocuSign, QuickBooks).

---

## Visualização de tempo

```
SEMANA 1: ████████░░░░  FASE 1 — uptime, dotfiles, backup
SEMANA 2: ░░░░░░░░████  Sprint 2.1 (testes E2E)
SEMANA 3: ░░░░░░████░░  Sprints 2.2 + 2.3
MÊS 2:    ░░░░░░░░░░░░  FASE 3 conforme demanda
```

Em paralelo (qualquer momento):
- Empresa-IA — glossário + Coordinator + CMO/CRO
- Trial SMB

---

## Riscos se não fizer FASE 1

| Risco | Probabilidade | Impacto |
|---|---|---|
| Smartcell cai e você não vê | 🔴 alta | Perde % do lucro mensal |
| LocaMoto form quebra silencioso | 🟡 média | Perde leads do investidor |
| Imerso pipeline Modal falha | 🟡 média | Cliente reclama 1º |
| Config Claude/Codex corrompe sem backup | 🟡 média | Perde 1 dia de trabalho de hoje |
| Banco Smartcell corrompe sem backup | 🟢 baixa | Perde dados de cliente — desastre |

---

## Conexões

- Sessão origem: [[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]
- Arsenal: [[Arsenal IA ForYou Code]]
- Estrutura empresa-IA: [[Empresa-IA ForYou Code — Estrutura]]
- Credenciais: [[Credenciais a Coletar]]
- Projetos afetados: [[Smartcell]], [[project_locamotofacil]], [[Imerso]], [[ForYou Code]]
