# QA ForYou Operacional — bugs corrigidos e GitHub bloqueado

**Data:** 2026-04-13 → 2026-04-14
**Projeto:** operacionalforyou.com.br (Lovable + Supabase)
**Repo local:** `C:/tmp/foryou-flow`
**Conta Claude:** ynwwilson@gmail.com (Pro)

---

## Objetivo da Sessão

Realizar QA 100% do app operacional ForYou Code: analisar código, banco de dados e edge functions, identificar e corrigir todos os bugs diretamente na branch main do repositório GitHub (`yngomesmarco-hue/foryou-flow`), sem intervenção manual do usuário.

---

## O que foi Implementado (sessão anterior + esta)

### Feature: Plano do Dia — melhorias completas
Gerados prompts Lovable para:
- Histórico com abas de status (Feitos / Incompletos / Não feitos)
- Delete cascade ao excluir plano
- Sub-abas de workspace na agenda
- Sync de status entre plano e tarefas individuais
- Seleção de incompletos por pessoa com matching inteligente via IA

### Correção do parser (micro-tasks)
O parser estava gerando centenas de micro-tarefas ao processar texto livre. Corrigido com lógica de agrupamento e limite de granularidade.

### Troca do provedor de IA
Substituído Anthropic API (caro) pelo gateway do próprio Lovable AI (`google/gemini-3-flash-preview`) na edge function `parse-plan`. Adicionado fallback para parser local quando a IA falha, com toast de aviso ao usuário.

---

## Bugs Identificados e Corrigidos (QA)

### Bug 1 — RLS bloqueia escrita direta em `workspace_agenda` (CRÍTICO)
- **Causa:** Policy `USING (false) WITH CHECK (false)` bloqueia 100% das escritas client-side
- **Impacto:** `PlanHistorySection` fazia `supabase.from('workspace_agenda').update(...)` diretamente — falhava silenciosamente sempre
- **Fix:** Adicionado helper `bulkUpdatePlanTasks()` que roteia pelo edge function `workspace-agenda` com JWT auth
- **Arquivo:** `src/components/tools/PlanHistorySection.tsx`

### Bug 2 — Tarefas incompletas invisíveis na aba "Incompletos"
- **Causa:** `handleToggleCheckbox` escreve marcador `⚠️ Incompleto (Marco): reason` mas `isIncomplete()` checava só `⚠️ Incompleto:` — nunca batia
- **Fix:** Atualizado `isIncomplete` e `getIncompleteReason` para aceitar ambos os formatos
- **Arquivo:** `src/components/workspace/NotionAgenda.tsx`

### Bug 3 — Status `'em_andamento'` não existe no sistema
- **Causa:** `handleToggleCheckbox` setava `newStatus = 'em_andamento'` que não existe no `AgendaStatus` type nem no CategoriesContext
- **Fix:** Trocado para `'fazendo'`
- **Arquivo:** `src/components/workspace/NotionAgenda.tsx`

### Bug 4 — `directed_at` NOT NULL com DEFAULT now()
- **Causa:** Todo novo `daily_plan` recebia `directed_at = now()` no INSERT, fazendo o guard "já direcionado" disparar erroneamente
- **Fix:** Migration que torna nullable + backfill de registros onde `directed_at ≈ created_at` (< 2s) para NULL
- **Arquivo:** `supabase/migrations/20260413180000_fix_directed_at_nullable.sql`

### Bug 5 — TaskSidePanel não detectava marcador de incompleto
- **Causa:** Regex incorreta para detectar linhas `⚠️ Incompleto`
- **Fix:** `const incompleteMarkers = notesLines.filter(l => /^⚠️ Incompleto/.test(l.trim()));`
- **Arquivo:** `src/components/workspace/TaskSidePanel.tsx`

### Bug 6 — Campo `material` sem update otimista
- **Causa:** `useWorkspaceAgenda.ts` não incluía `material` no optimistic update
- **Fix:** Adicionado `...(payload.material !== undefined && { material: payload.material })`
- **Arquivo:** `src/hooks/useWorkspaceAgenda.ts`

### Bug 7 — AgendaStatus type incompleto
- **Causa:** Faltavam status válidos no type `AgendaStatus`
- **Fix:** Adicionado `'a_completar'` e `'pendente'` ao union type
- **Arquivo:** `src/services/workspaceAgendaApi.ts`

---

## O que deu Errado

### Repositório GitHub deletado pelo usuário
- **Situação:** Lovable orientou o usuário a deletar o repo `yngomesmarco-hue/foryou-flow` para reconectar
- **Consequência:** Todos os 7 fixes já commitados e pushados foram perdidos no remote (existem apenas no clone local `C:/tmp/foryou-flow`)
- **Estado atual do remote:** `https://github.com/yngomesmarco-hue/foryou-flow` — **NÃO EXISTE MAIS**

### Lovable-GitHub sync quebrado
- **Sintoma:** Lovable fica em "Preparing to sync..." por minutos e depois retorna "Failed to sync"
- **Erro:** "We couldn't find the Lovable GitHub app installation for this account"
- **Tentativas:** Desconectar e reconectar GitHub, aba anônima, múltiplas contas — nenhuma funcionou
- **Causa provável:** Estado interno do Lovable corrompido após a deleção do repo; o app está instalado no GitHub mas o Lovable não consegue criar o novo repo

---

## Pendências

### BLOQUEADOR PRINCIPAL
- Lovable não consegue criar/conectar novo repositório GitHub
- **Próximo passo:** Criar repo vazio manualmente em `github.com/new` na conta `yngomesmarco-hue`, depois tentar conectar no Lovable selecionando repo existente
- **Alternativa:** Se Lovable permitir, configurar remote manualmente e usar `git push --force` do clone local

### Quando o GitHub conectar
- Fazer push do clone local (`C:/tmp/foryou-flow`) para o novo repo
- Todos os 7 fixes estão no commit `3d1f06c` ("fix: corrige bugs críticos de QA — RLS, status, parser e optimistic update")
- Verificar se a migration `20260413180000_fix_directed_at_nullable.sql` foi aplicada no Supabase

### Migration `directed_at`
- Verificar no dashboard Supabase se a migration foi aplicada
- Se não: executar manualmente via SQL Editor

---

## Estado do Repositório Local

```
Path:    C:/tmp/foryou-flow
Remote:  https://github.com/yngomesmarco-hue/foryou-flow (DELETADO)
Branch:  main
Commit:  3d1f06c — fix: corrige bugs críticos de QA
```

Todos os fixes estão commitados localmente. Assim que o GitHub estiver resolvido, um `git push` entrega tudo.

---

## Hooks de Auto-Save (configurados nesta sessão)

- **Stop hook:** `~/.claude/hooks/session-saver.js` — salva nota no Obsidian ao encerrar sessão
- **PostToolUse hook:** mesmo script — salva após cada ferramenta
- **Destino das notas:** `Claude 1/Sessões/` no vault Stark
- **Auto-context:** Ao iniciar sessão, Claude lê as últimas 30 linhas da nota mais recente para retomar contexto automaticamente

Configuração em: `~/.claude/settings.json`
