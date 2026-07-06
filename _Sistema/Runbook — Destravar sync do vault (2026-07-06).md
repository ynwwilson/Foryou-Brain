---
date: 2026-07-06
description: Como destravar o sync git do vault quando o obsidian-git para por merge conflict — incidente de 22/05 a 06/07 no PC do Wilson
tags: [brain, runbook]
---

# Runbook — Destravar sync do vault

## O que aconteceu (incidente 2026-05 → 2026-07)

O sync do vault é feito pelo plugin **obsidian-git** (commit a cada 10min, pull/push a cada 5min — só roda com Obsidian aberto). Em ~13/05 um commit remoto removeu os caches `.smart-env/` e `graph.json` do repo. O PC do Wilson ainda modificava esses caches localmente → o pull seguinte criou um **merge com 112 conflitos** (todos em arquivos de cache, zero conteúdo real). O obsidian-git não resolve conflito sozinho (`mergeStrategy: none`) e ficou travado em silêncio desde 22/05: nada subia, nada descia. Resultado: 365 notas só no PC do Wilson, 10 commits só no remoto.

## Como verificar se um PC está travado

No terminal, na pasta do vault:

```bash
git status
```

Sinais de travamento:
- `You have unmerged paths` / `fix conflicts and run "git commit"` → merge travado
- `Your branch and 'origin/main' have diverged` → commits presos dos dois lados

## Como destravar (Marco / Eduardo)

1. Fechar o Obsidian (para o plugin não competir com você).
2. Na pasta do vault:

```bash
git fetch origin
git status
```

3. **Se houver conflitos só em `.smart-env/` ou `.obsidian/graph.json`** (cache — seguro):

```bash
git rm --cached -r .smart-env
git rm --cached .obsidian/graph.json
git commit -m "merge: resolve conflitos de cache"
```

4. **Se houver conflito em nota `.md` real**: abrir o arquivo, escolher/mesclar o conteúdo, depois `git add <arquivo>` e `git commit`.
5. Integrar e subir:

```bash
git pull origin main --no-rebase
git push origin main
```

6. Reabrir o Obsidian. O plugin volta a sincronizar sozinho.

## Prevenção (já aplicada em 06/07)

- `.gitignore` agora ignora: `.smart-env/`, `.obsidian/graph.json`, `workspace.json`, `node_modules/`, `*.tmp.*` (temps de watcher), credenciais do obsidian-git.
- Esses arquivos eram a fábrica de conflitos — sem eles versionados, conflito real fica raro.
- **Regra de ouro**: se o Obsidian mostrar notice de erro do obsidian-git ("conflicts", "merge"), não ignorar — rodar este runbook no mesmo dia. Cada dia travado = mais divergência.

## Relacionados

- [[⚠️ Watchers Offline]]
