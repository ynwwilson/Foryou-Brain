# OPENCLAW_GUIDELINES.md
# Regras de Operação — Todos os Agentes

> Este arquivo é lei. Todo agente que acessa este vault deve ler e obedecer.
> Última atualização: 2026-03-31

---

## 1. ESTRUTURA DO VAULT

```
/Inbox/                   ← ÚNICA entrada. Todo agente deposita aqui. Humano também.
/Projetos/                ← Projetos ativos (um arquivo por projeto)
/Knowledge/               ← Base de conhecimento permanente da ForYou Code
/Atlas/                   ← Mapas visuais, canvas, arquitetura
/Sessões/                 ← Notas de sessões de trabalho diárias
/Agentes/
  /config/                ← IDENTITY, SOUL, USER, TOOLS, BOOTSTRAP
  /memória/
    /context/             ← decisions.md, lessons.md, business-context.md, people.md
    /feedback/            ← tone.json, content.json, tasks.json
    /projects/            ← memória por projeto (foryoucode.md, etc.)
    /sessions/            ← histórico de sessões do agente
/Referências/             ← Manuais, padrões, documentação fixa
/Arquivo/                 ← Tudo finalizado ou histórico
/Memória_Longo_Prazo/     ← Backup automático. NUNCA DELETAR. NUNCA EDITAR.
```

---

## 2. REGRAS DE ESCRITA (OBRIGATÓRIAS)

### Regra 1 — Inbox primeiro
Todo arquivo criado por agente vai para `/Inbox/` com prefixo de data:
```
Inbox/2026-03-30_nome-do-arquivo.md
```
Nunca escreva diretamente em `/Projetos/`, `/Knowledge/` ou qualquer outra pasta.
Exceção: atualizações em arquivos já existentes (ex: atualizar `memory/context/decisions.md`).

### Regra 2 — Um agente, um arquivo
Nunca dois agentes escrevem no mesmo arquivo simultaneamente.
Se precisar atualizar um arquivo que outro agente usa, crie um novo na Inbox com sufixo `_update`:
```
Inbox/2026-03-30_business-context_update.md
```

### Regra 3 — Nunca deletar
Nenhum agente pode deletar arquivos. Apenas mover para `/Arquivo/`.

### Regra 4 — Tags obrigatórias
Todo arquivo criado deve ter tags no frontmatter YAML:
```yaml
---
tags: [inbox, projeto/foryoucode, tipo/decisao]
data: 2026-03-30
agente: jarvis
---
```

**Tags de tipo válidas:**
- `tipo/decisao` — decisões tomadas
- `tipo/tarefa` — tarefas e TODOs
- `tipo/conhecimento` — base de conhecimento
- `tipo/sessao` — registro de sessão
- `tipo/referencia` — documentação fixa
- `tipo/projeto` — informações de projeto

**Tags de projeto válidas:**
- `projeto/foryoucode`
- `projeto/jarvis`
- `projeto/rainha-aprovacao`
- `projeto/smartcell`
- `projeto/ia-atendimento`

---

## 3. REGRAS DE LEITURA (ECONOMIZA TOKENS)

Para cada tipo de tarefa, leia APENAS estes arquivos:

| Tarefa | Arquivos a ler |
|--------|---------------|
| Contexto de negócio | `Agentes/memória/context/business-context.md` |
| Decisões anteriores | `Agentes/memória/context/decisions.md` |
| Lições aprendidas | `Agentes/memória/context/lessons.md` |
| Pessoas e clientes | `Agentes/memória/context/people.md` |
| Projeto específico | `Projetos/[nome-projeto].md` |
| Identidade do agente | `Agentes/config/IDENTITY.md` + `Agentes/config/SOUL.md` |
| Ferramentas disponíveis | `Agentes/config/TOOLS.md` |
| Conhecimento ForYou Code | `Knowledge/[tópico específico].md` |

**Nunca leia o vault inteiro. Nunca use glob recursivo em produção.**

---

## 4. MODELO POR TIPO DE TAREFA

| Tarefa | Modelo | Justificativa |
|--------|--------|---------------|
| Triagem de Inbox | claude-haiku-4-5-20251001 | Simples, barato |
| Classificação de arquivos | claude-haiku-4-5-20251001 | Simples, barato |
| Crons automáticos | claude-haiku-4-5-20251001 | Nunca usar Sonnet/Opus em cron |
| Análise de projeto | claude-sonnet-4-6 | Raciocínio necessário |
| Escrita longa | claude-sonnet-4-6 | Qualidade necessária |
| Arquitetura / decisão crítica | claude-sonnet-4-6 | Raciocínio profundo |

**Regra de ouro: cron = Haiku. Sempre.**

---

## 5. SEPARAÇÃO HUMANO vs AGENTE

| Pasta | Dono | Quem escreve |
|-------|------|-------------|
| `/Projetos/` | Humano | Humano + agente (via Inbox) |
| `/Knowledge/` | Humano | Humano + agente (via Inbox) |
| `/Atlas/` | Humano | Humano |
| `/Sessões/` | Humano | Humano |
| `/Agentes/memória/` | Agente | Apenas agentes |
| `/Agentes/config/` | Humano | Apenas humano (SOUL, IDENTITY, USER) |
| `/Inbox/` | Neutro | Qualquer um |
| `/Memória_Longo_Prazo/` | Sistema | Apenas script de backup |

---

## 6. CONSOLIDAÇÃO AUTOMÁTICA

O script `consolidar_obsidian.py` roda todo dia às 03:00 e:
1. Faz backup de tudo em `/Memória_Longo_Prazo/YYYY-MM-DD/`
2. Classifica arquivos da Inbox por tags e conteúdo
3. Move para a pasta correta
4. Nunca deleta nada
5. Usa Haiku para classificação quando necessário

---

## 7. CONVENÇÃO DE NOMES

```
# Arquivos de projeto
Projetos/ForYou Code.md
Projetos/Jarvis.md

# Arquivos de Knowledge
Knowledge/processo-vendas.md
Knowledge/precificacao.md

# Sessões
Sessões/2026-03-30.md

# Inbox (com data)
Inbox/2026-03-30_decisao-stack-backend.md
```

---

## 8. O QUE NÃO FAZER

- ❌ Criar arquivos na raiz do vault (exceto arquivos .md de configuração global)
- ❌ Usar modelos caros (Sonnet/Opus) em crons ou tarefas de triagem
- ❌ Deletar qualquer arquivo
- ❌ Escrever em arquivos de outro agente sem criar `_update` na Inbox
- ❌ Ler pastas inteiras para encontrar contexto — use os caminhos específicos acima
- ❌ Criar subpastas dentro de `/Memória_Longo_Prazo/` manualmente

---

## 9. ARQUITETURA HÍBRIDA — DOIS AGENTES

### Modelo Final

| Agente | Papel |
|--------|-------|
| **Jarvis / OpenClaw** | Cérebro central, memória, orquestrador |
| **Manus** | Executor Meta + navegação visual |
| Claude Cowork/Dispatch | Opcional — não é prioridade agora |

---

### Função do Jarvis
- Ponto principal de interação (Telegram)
- Mantém toda memória no Obsidian (projetos, clientes, decisões, histórico)
- Planejamento, análise, criação de apps/stack, crons
- Decide o que faz sozinho e o que delega ao Manus
- Salva todo resultado final no Obsidian

### Função do Manus
- Tudo relacionado à Meta: Instagram (posts, stories, reels), Meta Ads, WhatsApp Business, Creator Marketplace
- Execução visual no desktop via "Meu Navegador"
- Integração nativa com Meta — melhor performance, menor risco de bloqueio
- Sempre recebe contexto rico do Jarvis antes de agir (tom da marca, persona, estágio do funil)

---

### Regras de Delegação

- Se a tarefa envolver **Instagram, Meta Ads, WhatsApp Business, Creator Marketplace ou execução visual no navegador** → delega para o **Manus**, enviando o contexto necessário do Obsidian
- Para **planejamento, raciocínio complexo, criação de apps/stack, análise de projetos ou crons** → Jarvis executa diretamente
- **Sempre inclua contexto do Obsidian** ao delegar para o Manus (persona, funil, histórico da campanha)
- **Todo resultado final** deve ser salvo na pasta correta do Obsidian

---

### Exemplos Práticos

| Pedido | Quem executa |
|--------|-------------|
| "Cria um app de agendamento" | Jarvis (sozinho) |
| "Faz 5 posts para Instagram sobre Rainha da Aprovação" | Jarvis → Manus |
| "Verifica métricas das campanhas de hoje e sugere ajustes" | Jarvis → Manus |
| "Planeja a próxima semana de conteúdo com base no que funcionou" | Jarvis (usa Obsidian) |
| "Busca creators para campanha Smartcell, nicho tech, 50k-200k seguidores" | Jarvis → Manus |
| "Gera proposta comercial para novo cliente" | Jarvis (sozinho) |

---

*Este arquivo não deve ser editado por agentes. Apenas pelo humano (Mestre).*
