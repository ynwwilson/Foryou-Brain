---
data: 2026-05-27
duração: ~6h
tipo: aprimoramento + planejamento estratégico
ferramentas: Claude Code (claude-nova)
participantes: Mestre (José/Wilson)
status: parcialmente concluído (instalações OK, motor empresa-IA pendente)
---

# Sessão 2026-05-27 — Aprimoramento Arsenal IA + Empresa-IA ForYou Code

## TL;DR

Sessão longa que começou com análise de prints de skills/plataformas em `Downloads/aprimoramento` e evoluiu pra duas coisas:

1. **Instalação massiva de arsenal IA** nas 4 contas (Claude×2 + Codex×2) — ~32 itens novos
2. **Planejamento de empresa-IA virtual** (8 departamentos + ~40 funcionários) pra ForYou Code

Tudo instalado tecnicamente, mas o "motor" (Coordinator, agentes departamentais, glossário) ainda **não foi construído** — ficou pra próximas sessões.

---

## O que foi feito (em ordem cronológica)

### Fase 1 — Análise inicial (prints `Downloads/aprimoramento`)

Analisei 39 prints que o Mestre tinha juntado. Identifiquei:
- **2 SaaS externos** (Okara — Reddit lead, Zernio — multi-publicação social)
- **~15 skills/plugins** de Claude Code virais
- **Ruflo / claude-flow** — orquestração multi-agente
- **Meta Ads AI Connectors** (descartado por enquanto)
- Vários outros (morning-report era ilustração, não existe; everything-claude-code era ruído, etc)

### Fase 2 — Primeira rodada de instalação (8 itens-base)

1. **yt-dlp** (CLI download de vídeo, com FFmpeg + Deno)
2. **caveman** (~65% economia de saída) — nas 4 contas
3. **Karpathy CLAUDE.md skill** (5 regras de qualidade)
4. **Superpowers oficial (obra)** — 14 skills bundle
5. **Playwright skill** (lackeyjb)
6. **find-skills** (vercel-labs)
7. **handoff** (ykdojo)
8. **Ruflo / claude-flow MCP** (314 tools, em todas as 4 contas)

### Fase 3 — Descoberta crítica: mapeamento das 4 contas

- `claude` (CLI) → `~/.claude/` (conta 1)
- `claude-nova` (function PowerShell) → `~/.claude-nova/` (conta 2, ativa agora)
- `codex` → `~/.codex/` (Codex 1)
- `~/.codex-plus-2/` (Codex 2, sem comando dedicado óbvio)

Alternância via `$env:CLAUDE_CONFIG_DIR`. Skills compartilhadas pro Codex vão pra `~/.agents/skills/`.

### Fase 4 — Segunda rodada (skills extras pedidas pelo Mestre)

Mestre pediu (após ver lista de skills disponíveis):
- **skill-creator** + **mcp-builder** + **webapp-testing** + **frontend-design** + 8 outras (via bundle `example-skills` do `anthropics/skills`)
- **ralph-wiggum** oficial Anthropic (loop autônomo via Stop hook)
- **Ralph TUI** suite (ralph-prd, ralph-tasks via wiggumdev/ralph)
- **agent-browser** (vercel-labs) — CDP multi-agent
- **browser-use** (dalbit-mir wrapper)

### Fase 5 — Bônus Anthropic oficial (5 plugins)

Do `claude-code-plugins`:
- **frontend-design** (plugin completo, substitui UI/UX Pro Max)
- **commit-commands** (/commit, /push, /pr)
- **code-review** (multi-agente com confidence scoring)
- **pr-review-toolkit** (6 reviewers especializados)
- **security-guidance** (warn XSS/injection)

### Fase 6 — Plugins finais Anthropic

- **hookify** (criar hooks custom)
- **plugin-dev** (criar plugins próprios)
- **feature-dev** (workflow feature)
- **document-skills** (xlsx/docx/pptx/pdf)
- **claude-api** (docs SDK Claude)

### Fase 7 — Sincronização Codex 2

Descoberto que `~/.codex-plus-2/agents/` estava **vazio**. Copiei os 33 agentes GSD do `~/.codex/agents/` (66 arquivos = 33 .md + 33 .toml).

### Fase 8 — Planejamento estratégico (empresa-IA)

Mestre esclareceu que quer agentes **organizacionais** (CTO, CMO, CRO, COO, CFO, CPO, CCO, CSO) com funcionários especialistas em cada departamento — não 3 agentes técnicos pontuais como eu sugeri inicialmente.

Discutimos:
- **Estrutura empresa-IA** (8 departamentos + ~40 funcionários)
- **Coordinator pattern** (mediador entre agentes)
- **Blackboard** (memória persistente como verdade compartilhada)
- **Regras anti-loop / anti-conflito** (5 regras técnicas)
- **Comunicação inter-agente** (CMO ↔ CRO via Coordinator)
- **Acessos/credenciais necessários por departamento**

### Fase 9 — Lista de credenciais a coletar

Montei lista direta de 26 credenciais que Mestre precisa pegar/salvar no Bitwarden.

### Fase 10 — Salvamento desta sessão no vault (agora)

---

## Status final do arsenal (nas 4 contas)

### Marketplaces ativos
- `anthropic-agent-skills` (anthropics/skills)
- `claude-code-plugins` (anthropics/claude-code) 
- `superpowers-marketplace` (obra)
- `caveman` (JuliusBrussee)
- `karpathy-skills` (forrestchang)
- `playwright-skill` (lackeyjb)
- `agent-browser` (vercel-labs)
- `ralph-marketplace` (wiggumdev/ralph)
- já existentes: `context-mode`, `dev-browser-marketplace`, `claude-plugins-official`

### Plugins ativos nas 2 Claudes (~20)
- **Anthropic oficial**: ralph-wiggum, frontend-design, commit-commands, code-review, pr-review-toolkit, security-guidance, hookify, plugin-dev, feature-dev, document-skills, claude-api, example-skills (12 sub-skills incluindo skill-creator + mcp-builder + webapp-testing)
- **Comunidade**: superpowers (14 sub-skills), caveman (7 sub-skills + MCP shrink), andrej-karpathy-skills, playwright-skill, agent-browser, ralph (ralph-prd + ralph-tasks)
- **Já existentes**: context-mode, dev-browser, vercel suite (~30), claude-video-vision

### Skills standalone (ativas nesta sessão confirmadas via system reminder)
- find-skills, handoff, browser-use

### MCPs ativos
- **claude-flow (Ruflo)** — 314 tools de orquestração, configurado nas 4 contas
- **caveman-shrink** — comprime saída de subagentes
- **context-mode**, **filesystem**, **browser** (Playwright), **vercel**, **supabase**, **context7**, **obsidian**

### Total estimado: ~150 skills + ~70 agentes (32 GSD + 25 dos plugins + 10 built-in) entre as 4 contas

---

## Pendências em aberto

### 🔴 Crítico — operacional (Sprint 1 do plano)
- [ ] **UptimeRobot/Better Uptime + alerta Telegram** pros 3 sites em prod (Smartcell, LocaMotoFácil, Imerso) — risco real de perder dinheiro do Smartcell
- [ ] **Backup automatizado Smartcell** — dados de pedidos/cadastros
- [ ] **Git dotfiles** — versionar `.claude/`, `.claude-nova/`, `.codex/`, `.codex-plus-2/` configs

### 🟡 Importantes (Sprint 2 do plano)
- [ ] **Testes E2E agendados** (GitHub Actions cron rodando Playwright contra Smartcell + LocaMotoFácil)
- [ ] **Vault como source-of-truth de projetos** (template + Dataview de pipeline)
- [ ] **Skill custom "novo cliente ForYou Code"** (acelera setup de 3 dias pra 30 min)

### 🔴 Crítico — empresa-IA (sem isso agentes não funcionam)
- [ ] **Glossário ForYou Code** (termos: MVP, ICP, lead quente, voz Marco/Eduardo/Mestre)
- [ ] **Tabela de stakeholders** (quem aprova o quê — Marco, Eduardo, Mestre, agentes)
- [ ] **Lista mestre de URLs de produção** (Smartcell, LocaMotoFácil, Imerso, ForYouCode, futuros)
- [ ] **Cofre de credenciais** (Bitwarden) — 26 itens listados (ver nota separada)
- [ ] **Coordinator Agent** (mediador entre agentes)
- [ ] **Blackboard Protocol** (formato fixo de mensagem entre agentes)
- [ ] **8 agentes departamentais** (CTO, CMO, CRO, COO, CFO, CPO, CCO, CSO)
- [ ] **~40 funcionários-IA** sub-especialistas

### 🟢 Pendências externas (Mestre decide)
- [ ] **Criar conta Okara** (Free tier) — monitor de leads Reddit
- [ ] **Criar conta Zernio** (Free 2 contas) — publicação multi-social
- [ ] **Avaliar Claude for Small Business** (trial 14 dias, US$25-150/seat) — pode resolver várias lacunas operacionais de uma vez

### 🟡 Documentação interna a criar (skill-creator pode ajudar)
- [ ] Stack Decision Matrix (Lovable vs Astro vs TanStack)
- [ ] Padrão DNS Cloudflare consolidado (DKIM cinza, etc)
- [ ] Glossário de voz dos 3 sócios
- [ ] Calendário editorial padrão
- [ ] Tabela de objeções de venda
- [ ] Sequência de follow-up
- [ ] Script de qualificação ICP
- [ ] Template padrão de projeto no vault
- [ ] Dataview de pipeline de projetos
- [ ] SLA por tipo de cliente
- [ ] Tabela de gastos com infra IA (todas as plataformas)
- [ ] Margem por projeto
- [ ] Regra de aprovação de budget
- [ ] Roadmap quarterly ForYou Code
- [ ] ICP detalhado saúde/estética
- [ ] Tom ForYou de resposta cliente
- [ ] Matriz de escalation
- [ ] Template contrato MVP
- [ ] Cláusulas LGPD clínica de saúde

---

## Decisões tomadas

### Sobre arsenal IA
- ✅ Instalar tudo que viraliza (caveman, karpathy, superpowers, playwright, find-skills, handoff)
- ✅ Aceitar bônus oficial Anthropic (frontend-design, security-guidance, etc)
- ✅ Configurar Ruflo / claude-flow MCP nas 4 contas
- ❌ **Pular Meta Ads MCP** — não vende gestão de ads agora
- ❌ **Pular everything-claude-code (ECC)** — 119 skills, vira ruído
- ❌ **Pular antigravity-install-all** — 1400 skills, mesmo problema
- ❌ **Pular UI/UX Pro Max** — frontend-design oficial Anthropic é melhor e bate com gosto P&B editorial

### Sobre estrutura organizacional IA
- ✅ Adotar modelo **empresa-IA com 8 C-Levels + ~40 funcionários**
- ✅ Pattern **Coordinator + Blackboard** pra comunicação inter-agente
- ✅ **5 regras técnicas anti-quebra**: max 3 rounds, token cap 500/msg, loop detector, todos via Coordinator, blackboard como verdade
- ✅ Construir **C-Levels primeiro**, funcionários conforme demanda

### Sobre segurança/credenciais
- ✅ **NUNCA** passar credenciais por chat de IA — risco de vazar pro vault auto-sync (Marco/Eduardo veem)
- ✅ **Bitwarden** como cofre humano mestre
- ✅ **.env por projeto** + env vars globais como fonte que agentes leem
- ⏳ Doppler/Infisical pra futuro (quando empresa-IA rodar 24/7)

### Sobre fluxo de execução
- ✅ Construir **motor da empresa-IA** (glossário + coordinator + protocolo) **antes** de credenciais — credenciais sem motor não servem
- ✅ Em paralelo, Mestre coleta credenciais offline no Bitwarden

---

## Memórias persistentes atualizadas

### Criadas
- `reference_skills_arsenal.md` — Arsenal completo de ~30 itens organizado por categoria
- `reference_4_contas_claude_codex.md` — Mapeamento 4 contas + comandos de instalação + pegadinhas

### Notas no vault (esta sessão)
- `Claude Nova/Sessões/2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code.md` — esta nota
- `Referências/Arsenal IA ForYou Code.md` — catálogo dos plugins/skills/MCPs (será criada)
- `Referências/Plano Operacional ForYou Code.md` — sprints/fases (será criada)
- `Referências/Credenciais a Coletar.md` — lista 26 credenciais (será criada)
- `Agentes/Empresa-IA ForYou Code — Estrutura.md` — diagrama + responsabilidades C-Levels (será criada)

---

## Próximos passos (na ordem)

### Imediato (próxima sessão)
1. **Mestre coleta credenciais no Bitwarden** (1-2h offline, sozinho)
2. **Construir glossário ForYou Code** no vault (~30min)
3. **Construir tabela de stakeholders** (~30min)
4. **Lista mestre de URLs prod** (~15min)

### Semana 1
5. **Coordinator Agent** + Blackboard Protocol (~2h)
6. **Sprint 1.1**: UptimeRobot + Telegram alert (~1h) — único risco que custa dinheiro
7. **Sprint 1.2**: Git dotfiles (~1h)

### Semana 2
8. **CMO + CRO** (par mais doloroso pra testar comunicação) (~3h)
9. **Validar com cenário real** (campanha de aquisição)

### Semana 3+
10. **Escalar pros outros 6 C-Levels** (~6-8h)
11. **Criar funcionários conforme gargalo aparecer**

### Avaliação paralela
12. **Trial Claude for Small Business** (14 dias) — pode resolver várias lacunas operacionais de uma vez

---

## Conexões

- Conecta com [[reference_skills_arsenal]] (memória persistente)
- Conecta com [[reference_4_contas_claude_codex]] (memória persistente)
- Conecta com [[ForYou Code]] (projeto principal)
- Conecta com [[Pipeline Comercial 2026]]
- Conecta com [[project_foryoucode_papeis_socios]] (memória — 3 sócios)
- Conecta com [[project_session_saver]] (memória — auto-save funcionando)
- Conecta com [[project_foryou_pacote_sites_mvp]] (memória — MVP R$1.500-2.000)
- Conecta com [[project_smartcell_entregue]] (memória — case + 20% participação)
- Conecta com [[project_locamotofacil]], [[project_imerso]], [[project_ag_estofados]], [[project_wm_noivas_site]]

---

_Sessão salva em 2026-05-27 ~23h45_
_Pasta: Claude Nova/Sessões/_
