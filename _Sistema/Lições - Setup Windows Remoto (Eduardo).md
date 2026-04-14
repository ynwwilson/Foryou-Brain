---
date: 2026-04-14
tags: [sistema, lições, windows, powershell, setup]
---

# Lições Aprendidas — Setup Remoto Windows (Eduardo)

> Sessão de 2026-04-14. Setup que deveria levar 30 min levou horas por erros evitáveis.
> Este documento existe para que nunca se repita.

---

## REGRA DE OURO

**Nunca escrever strings longas no PowerShell do PC remoto.**
**Sempre criar arquivos no PC do Wilson, commitar no vault, e copiar com variáveis curtas.**

```powershell
# ✅ Único jeito confiável de copiar arquivos em Windows remoto
$s="C:\caminho\origem\arquivo.json"
$d="C:\caminho\destino\arquivo.json"
Copy-Item $s $d -Force
```

---

## ERROS E SOLUÇÕES

### 1. PowerShell quebra linhas longas e injeta newlines nas strings

**O que aconteceu:** Qualquer string com mais de ~80 caracteres no PowerShell quebra em múltiplas linhas. O terminal exibe `>>` (continuação), mas o conteúdo da string fica com `\n` embutido. Isso quebra JSON, código JavaScript e qualquer dado estruturado.

**Comandos que falharam por isso:**
- `Set-Content -Path "..." -Value '{"longJson":...}'`
- `[System.IO.File]::WriteAllText("...", '{"longJson":...}')`
- `node -e "require('fs').writeFileSync(...)"`
- `echo '{"transcript_path":"...longo..."}' | node script.js`

**Solução:** Criar o arquivo no PC do Wilson com a ferramenta Write, commitar no vault, Eduardo copia com `Copy-Item $s $d -Force` usando variáveis curtas.

---

### 2. `Set-Content -Encoding UTF8` adiciona BOM no PowerShell 5

**O que aconteceu:** O PowerShell 5 (padrão no Windows) adiciona BOM (`\uFEFF`) ao início do arquivo quando se usa `-Encoding UTF8`. O `JSON.parse()` no Node.js falha silenciosamente se houver BOM — o session-saver cai no fallback com o vault path do Wilson, tenta criar pasta em `C:/Users/ynwwi/...` que não existe no PC do Eduardo, falha silenciosamente, não salva nada.

**Como detectar:** `raw.charCodeAt(0) === 0xFEFF` → BOM presente.

**Solução:** 
- Usar `[System.IO.File]::WriteAllText()` — mas atenção ao item 1 (ainda quebra se string for longa)
- **Melhor solução:** criar o arquivo no vault (PC do Wilson) e copiar via `Copy-Item`

---

### 3. `@'...'@` here-string do PowerShell — usuário cola errado

**O que aconteceu:** O fechamento `'@` precisa estar em linha própria, sem espaços. Quando o usuário cola o bloco inteiro de uma vez, o `'@` vai para o final da linha anterior e o bloco nunca fecha. O PowerShell fica em modo `>>` esperando indefinidamente.

**Solução:** Não usar here-string para arquivos de configuração. Criar no vault e copiar.

---

### 4. `node -e "código longo"` quebra no PowerShell

**O que aconteceu:** O argumento `-e "..."` também sofre com o line wrapping do PowerShell. Se o código tiver mais de ~70 chars, o Node recebe o código com newlines embutidos e falha com `SyntaxError: Invalid or unexpected token`.

**Solução:** Salvar o script `.js` em arquivo e rodar com `node C:\script.js`.
Para criar o arquivo: usar o vault (criar no Wilson, copiar via git).

---

### 5. `echo '...' | node script.js` não funciona no PowerShell

**O que aconteceu:** PowerShell não suporta pipe com `echo` para executáveis externos da mesma forma que bash.

**Solução:**
```powershell
$json = '{"key":"value"}'
$json | & "C:/Program Files/nodejs/node.exe" "C:/caminho/script.js"
```
Mas atenção: se `$json` for atribuído com string longa, o problema do item 1 volta.

---

### 6. Session-saver.js versão antiga copiada para o PC remoto

**O que aconteceu:** Eduardo copiou os hooks do vault ANTES do git pull completar com as versões atualizadas. A versão antiga não tinha a lógica de `author` (subpastas por pessoa). O hook rodava sem erro mas salvava em local errado (ou em nenhum lugar).

**Como detectar:**
```powershell
$f="C:\Users\eduar\.claude\hooks\session-saver.js"
Select-String "author" $f
```
Sem output = versão antiga.

**Solução:** Sempre fazer git pull ANTES de copiar os hooks. Ou usar Node.js para copiar diretamente do vault após pull confirmado.

---

### 7. pm2 watchers errando — chokidar não instalado

**O que aconteceu:** O `package.json` não foi copiado junto com os hooks (esqueceu no Copy-Item). Sem `node_modules/chokidar`, os watchers crasham em loop.

**Solução:** Sempre copiar `package.json` junto e rodar `npm install` na pasta dos hooks.

**Verificação:**
```powershell
pm2 list  # status deve ser "online", não "errored"
```

---

### 8. Task Scheduler — username "eduar" não reconhecido

**O que aconteceu:** `Register-ScheduledTask -User "eduar"` falhou com erro de mapeamento de segurança.

**Solução:**
```powershell
$fullUser = "$env:USERDOMAIN\$env:USERNAME"
Register-ScheduledTask ... -User $fullUser
```

---

### 9. Vim abrindo durante git pull (merge commit)

**O que aconteceu:** `git pull` após conflito resolvido abre o Vim para confirmar a mensagem do merge commit. Usuário não sabia o que fazer.

**Solução:** Digitar `:wq` e Enter para salvar e sair.

---

### 10. Eduardo rodando claude de dentro do vault

**O que aconteceu:** Claude rodado de `C:\Users\eduar\Foryou-Brain\` carrega o `CLAUDE.md` do vault (Wilson's), tratando Eduardo como "Mestre".

**Solução:** Eduardo deve rodar o claude da pasta home:
```powershell
cd C:\Users\eduar
claude
```

---

### 11. config.json com path errado no fallback

**O que aconteceu:** Quando o `config.json` falha (BOM ou JSON inválido), o `loadConfig()` do session-saver retorna um objeto padrão hardcoded com `vaultPath: 'C:/Users/ynwwi/...'` — o vault do Wilson. No PC do Eduardo esse path não existe, a criação da pasta falha silenciosamente, e nenhuma nota é salva.

**Lição:** O fallback do loadConfig deveria falhar ruidosamente ou usar o homedir. Por ora, garantir que o config.json seja sempre válido.

---

### 12. Conflito no vault do Eduardo — .smart-env e community-plugins.json

**O que aconteceu:** Esses arquivos estavam sendo rastreados pelo git mas são gerados localmente pelo Obsidian. Cada máquina gera versões diferentes, causando conflito em todo pull.

**Solução aplicada:** Adicionados ao `.gitignore`:
```
.smart-env/
.obsidian/community-plugins.json
.obsidian/graph.json
```
E removidos do tracking com `git rm -r --cached`.

---

## FLUXO CORRETO PARA SETUP EM WINDOWS REMOTO

```
1. Criar TODOS os arquivos de config no PC do Wilson
2. Commitar no vault com git push
3. PC remoto: git pull
4. PC remoto: Copy-Item com variáveis curtas
5. Nunca tentar criar/editar arquivos de config diretamente no PC remoto via PowerShell
```

### Arquivos que devem existir no vault para cópia:

| Arquivo no vault | Destino no PC remoto |
|---|---|
| `_Sistema/eduardo-config.json` | `C:\Users\eduar\.session-saver\config.json` |
| `_Sistema/eduardo-settings.json` | `C:\Users\eduar\.claude\settings.json` |
| `_Sistema/eduardo-settings.json` | `C:\Users\eduar\.claude-nova\settings.json` |
| `_Sistema/Scripts/session-saver.js` | `C:\Users\eduar\.claude\hooks\session-saver.js` |
| `_Sistema/Scripts/codex-watcher.js` | `C:\Users\eduar\.claude\hooks\codex-watcher.js` |
| `_Sistema/Scripts/antigravity-watcher.js` | `C:\Users\eduar\.claude\hooks\antigravity-watcher.js` |
| `_Sistema/Scripts/package.json` | `C:\Users\eduar\.claude\hooks\package.json` |

---

## APLICAR PARA MARCO (macOS)

No macOS os problemas de PowerShell não existem. Mas aplicar:
- Criar configs no vault, copiar via `cp` com variáveis
- Fazer git pull antes de copiar scripts
- Rodar claude da home (`~/`), não do vault
- LaunchAgent em vez de Task Scheduler
