---
date: 2026-07-06
description: Passo a passo por pessoa para o vault sincronizar 100% automático nos 3 PCs — pull + commit + push a cada 5 min, com alerta visível quando travar
tags: [brain, runbook]
---

# Setup Sync Automático (por PC)

Objetivo: cada PC **envia e recebe** sozinho, a cada 5 min, mesmo com Obsidian fechado. Antes só tinha pull agendado (recebia mas não enviava) + obsidian-git (só com Obsidian aberto).

O script novo faz: commit do que mudou → pull (merge) → push → confere se subiu. Se travar em conflito, ele **não fica preso em silêncio** (o erro de antes): cria um arquivo `VAULT SYNC TRAVADO - LEIA.txt` no Desktop apontando pro [[Runbook — Destravar sync do vault (2026-07-06)|runbook]].

---

## ⚡ Jeito fácil — instalador de 1 clique (use este)

Os instaladores fazem TODO o roteiro abaixo sozinhos (Passo 0 + agendador + teste). Na pasta do vault, abrir `_Sistema/Scripts/` e:

- **Eduardo (Windows):** duplo clique em `instalar-sync.bat`.
- **Marco (macOS):** duplo clique em `instalar-sync.command`.

A janela mostra o progresso e termina com "TUDO PRONTO". Se pedir login do GitHub, logar (GitHub Desktop ou `gh auth login`) e rodar o instalador de novo — pode rodar quantas vezes quiser, é seguro repetir.

O roteiro manual abaixo fica só como **fallback** se o instalador falhar.

---

## PASSO 0 — todos (uma vez): destravar e subir o que tem

No terminal, **na pasta do vault**:

```bash
git status
```

- Se aparecer `unmerged paths` ou `diverged` → seguir o [[Runbook — Destravar sync do vault (2026-07-06)|runbook]] primeiro.
- Se aparecer arquivos modificados/untracked (coisa local que nunca subiu):

```bash
git add -A
git commit -m "vault: sync inicial do meu PC"
git pull origin main --no-rebase
git push origin main
```

- Se o push der erro de autenticação → logar uma vez (`gh auth login` ou usar GitHub Desktop) e repetir o push. A credencial precisa de **permissão de escrita** no repo Foryou-Brain.

---

## Eduardo (Windows)

1. Fazer o Passo 0.
2. Apagar a task antiga de pull (se souber o nome dela; senão deixa, é inofensiva).
3. Criar a task nova (PowerShell **como administrador**, ajustar o caminho do vault se for diferente):

```powershell
schtasks /create /f /tn "VaultSyncFull" /sc minute /mo 5 /tr "powershell -NoProfile -WindowStyle Hidden -File \"C:\CAMINHO\DO\VAULT\_Sistema\Scripts\sync-vault.ps1\""
```

4. Testar: `schtasks /run /tn "VaultSyncFull"` e conferir `git log -1` na pasta do vault.

## Marco (macOS)

1. Fazer o Passo 0.
2. Dar permissão de execução ao script:

```bash
chmod +x "/CAMINHO/DO/VAULT/_Sistema/Scripts/sync-vault.sh"
```

3. Editar `~/Library/LaunchAgents/com.foryou.vaultsync.plist`: em `ProgramArguments`, trocar o comando de pull pelo script:

```xml
<key>ProgramArguments</key>
<array>
    <string>/bin/bash</string>
    <string>/CAMINHO/DO/VAULT/_Sistema/Scripts/sync-vault.sh</string>
</array>
```

4. Recarregar:

```bash
launchctl unload ~/Library/LaunchAgents/com.foryou.vaultsync.plist
launchctl load ~/Library/LaunchAgents/com.foryou.vaultsync.plist
```

## Wilson (Windows)

Task `VaultSyncFull` já instalada em 2026-07-06 (mesmo comando do Eduardo). obsidian-git continua ativo por cima — os dois convivem (o script sai se o git estiver ocupado).

---

## Regras pra nunca mais travar

1. **Arquivo `VAULT SYNC TRAVADO - LEIA.txt` apareceu no Desktop** → resolver no mesmo dia (runbook). Cada dia parado = mais divergência.
2. **Token/API key nunca em nota** — o GitHub bloqueia o push do vault inteiro por causa de 1 secret. Guardar em `_Sistema/Cofre Local/` (pasta fora do git, só existe no PC de cada um).
3. Conflito real agora só acontece se **2 pessoas editarem a mesma nota ao mesmo tempo** — caches que causavam os 112 conflitos já estão fora do git.

## Relacionados

- [[Runbook — Destravar sync do vault (2026-07-06)]]
- [[⚠️ Watchers Offline]]
