---
tipo: referência
criado: 2026-05-27
atualizado: 2026-05-27
fonte: sessão "[[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]"
---

# Arsenal IA ForYou Code

Catálogo completo de skills, plugins, MCPs e ferramentas instalados nas 4 contas (Claude Code conta 1 + conta 2, Codex 1 + 2).

## 4 ambientes

| Ambiente | Comando | Diretório |
|---|---|---|
| Claude Code conta 1 | `claude` | `~/.claude/` |
| Claude Code conta 2 | `claude-nova` | `~/.claude-nova/` |
| Codex 1 | `codex` | `~/.codex/` |
| Codex 2 | (env var `CODEX_HOME`) | `~/.codex-plus-2/` |
| Skills compartilhadas Codex | — | `~/.agents/skills/` |

Alternância Claude via `$env:CLAUDE_CONFIG_DIR`.

---

## Por categoria

### 🧠 Economia de tokens / qualidade de saída

| Item | O que faz | Trigger |
|---|---|---|
| **caveman** | Corta ~65% saída do modelo | "caveman mode", "be brief" |
| **cavecrew** (3 subagentes) | Versão caveman pra subagentes | delegate via subagent |
| **caveman-shrink MCP** | Comprime saída entre agentes | automático |
| **karpathy-guidelines** | 5 regras Karpathy (pensar antes, simplicidade, mexer só no que precisa, dar metas, falar quando confuso) | auto ao codar |
| **RTK** (não é skill — é CLI externo) | Filtra saída de terminal | prefixar `rtk <cmd>` |

### 🎯 Workflow / disciplina (Superpowers — obra)

14 skills auto-trigger por contexto:

- **brainstorming** — refinar ideia ambígua
- **systematic-debugging** — debug sem chute
- **writing-plans** — plano antes de código
- **executing-plans** — executar plano com checkpoint
- **test-driven-development** — TDD obrigatório
- **requesting-code-review** — revisar antes PR
- **receiving-code-review** — receber revisão
- **subagent-driven-development** — dividir em subagentes
- **dispatching-parallel-agents** — paralelo sem conflito
- **verification-before-completion** — não diz "feito" sem prova
- **using-git-worktrees** — branches isolados
- **finishing-a-development-branch** — checklist final
- **using-superpowers** — meta
- **writing-skills** — criar skill nova

### 🛠️ Plugins oficiais Anthropic (claude-code-plugins)

9 instalados de 13 disponíveis:

- **ralph-wiggum** — loop autônomo via Stop hook
- **frontend-design** — design quality (substitui UI/UX Pro Max)
- **commit-commands** — `/commit`, `/push`, `/pr`
- **code-review** — review multi-agente com confidence scoring
- **pr-review-toolkit** — 6 reviewers focados
- **security-guidance** — warn XSS/injection ao editar
- **hookify** — cria hooks custom via markdown
- **plugin-dev** — toolkit pra criar plugins
- **feature-dev** — workflow completo de feature

Pulados (irrelevantes ou redundantes):
- claude-opus-4-5-migration (já em 4.7)
- explanatory-output-style / learning-output-style
- agent-sdk-dev

### 🤖 Skills oficiais Anthropic (anthropic-agent-skills)

3 plugins, 16 sub-skills:

**example-skills** (12): skill-creator, mcp-builder, webapp-testing, brand-guidelines, canvas-design, doc-coauthoring, frontend-design, internal-comms, theme-factory, web-artifacts-builder, algorithmic-art, slack-gif-creator

**document-skills** (4): xlsx, docx, pptx, pdf

**claude-api** (1): docs API Claude / SDK

### 🔄 Ralph TUI (wiggumdev/ralph)

- **ralph-prd** — gera PRD
- **ralph-tasks** — converte PRD em tarefas

### 🌐 Browser automation (4 opções, nichos diferentes)

| Skill | Nicho |
|---|---|
| **dev-browser** (sawyerhood) | Ad-hoc na sessão atual |
| **playwright-skill** (lackeyjb) | QA visual, screenshots, validação UI |
| **agent-browser** (vercel-labs) | CDP multi-agent, scraping, login com Chrome real |
| **browser-use** (dalbit-mir wrapper) | Sessão persistente cross-sessão, vision direct mode |

### 🔌 Outras

- **find-skills** (vercel-labs) — meta-skill: discovery
- **handoff** (ykdojo) — passagem de contexto mid-sessão
- **context-mode** — economia de pesquisa (cache + search)
- **claude-video-vision** — analisar vídeo (Gemini + OpenAI fallback)
- **vercel** suite (~30 skills) — nextjs, deploy, env, shadcn, auth, ai-sdk, firewall, sandbox, workflow, etc

### 🎛️ MCP servers ativos

| MCP | Onde | Função |
|---|---|---|
| **claude-flow (Ruflo)** | 4 contas | Orquestração 314 tools — swarm, memory, routing |
| **caveman-shrink** | 2 Claudes | Comprime saída de subagentes |
| **context-mode** | todas | Pesquisa otimizada |
| **filesystem** | Codex | Operações de arquivo |
| **browser** (Playwright) | Codex | Browser via MCP |
| **vercel**, **supabase**, **context7**, **obsidian** | Codex | APIs externas |

---

## Agentes (~70 totais nas 4 contas)

### Built-in Claude Code (10)
claude, Explore, Plan, general-purpose, statusline-setup, claude-code-guide, claude-video-vision:frame-describer, vercel:ai-architect, vercel:deployment-expert, vercel:performance-optimizer

### GSD próprios (~33 — Codex 1 e 2, sincronizados em 2026-05-27)
Pesquisa: gsd-advisor-researcher, gsd-ai-researcher, gsd-domain-researcher, gsd-phase-researcher, gsd-project-researcher, gsd-ui-researcher, gsd-research-synthesizer
Código: gsd-code-fixer, gsd-code-reviewer, gsd-codebase-mapper, gsd-pattern-mapper, gsd-executor, gsd-framework-selector
Debug: gsd-debugger, gsd-debug-session-manager, gsd-assumptions-analyzer, gsd-integration-checker, gsd-nyquist-auditor
Docs: gsd-doc-classifier, gsd-doc-synthesizer, gsd-doc-verifier, gsd-doc-writer, gsd-intel-updater
Plan/Eval: gsd-planner, gsd-plan-checker, gsd-roadmapper, gsd-eval-planner, gsd-eval-auditor
Audit: gsd-security-auditor, gsd-ui-auditor, gsd-ui-checker, gsd-user-profiler, gsd-verifier

### Dos plugins (~25)
- **caveman/cavecrew** (3): builder, investigator, reviewer
- **feature-dev** (3): code-architect, code-explorer, code-reviewer
- **pr-review-toolkit** (6): code-reviewer, code-simplifier, comment-analyzer, pr-test-analyzer, silent-failure-hunter, type-design-analyzer
- **plugin-dev** (3)
- **hookify** (1)
- **ralph** (3)
- **skill-creator** (3)
- **vercel** (6)

---

## Decididamente NÃO instalado

| Item | Por quê |
|---|---|
| **everything-claude-code (ECC)** | 119 skills, vira ruído mesmo com selective-install |
| **antigravity install-all** | 1400 skills, mesmo problema |
| **UI/UX Pro Max** | Puxa pra "AI slop"; frontend-design Anthropic é melhor |
| **huashu-design** | Clone redundante |
| **Meta Ads MCP** | Não vende gestão de tráfego ainda |
| **yt-search, yt-pipeline, notebooklm, deep-research** | Redundantes com auto-context + Infinity Content |
| **morning-report** | Não existe como skill pública (era exemplo ilustrativo) |
| **mattpocock skills** | Marcado pra depois (TS pesado) |
| **impeccable, taste-skill** | Marcado pra depois (UI pesado) |
| **Gemini CLI extension caveman** | Não usa Gemini CLI |

---

## Conexões

- Sessão de origem: [[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]
- Plano operacional: [[Plano Operacional ForYou Code]]
- Estrutura empresa-IA: [[Empresa-IA ForYou Code — Estrutura]]
- Credenciais: [[Credenciais a Coletar]]
- ForYou Code projeto: [[ForYou Code]]
