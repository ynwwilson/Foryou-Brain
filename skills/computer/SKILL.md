---
name: computer
description: Controle remoto do desktop Windows — screenshot, clique, digitação, aprovação de prompts em terminal.
---

# Computer Control

Ferramentas para controlar o desktop do PC remotamente via Telegram.

Scripts disponíveis em `skills/computer/scripts/`:

## screenshot.py — capturar tela

```bash
python skills/computer/scripts/screenshot.py
# Salva PNG no TEMP e retorna o caminho
```

## send_photo.py — enviar imagem para o Telegram do Mestre

**SEMPRE usar após tirar screenshot.** Envia o arquivo diretamente para o chat do Mestre via API do Telegram.

```bash
# Fluxo completo: tirar screenshot E enviar
python skills/computer/scripts/screenshot.py > /tmp/path.txt
python skills/computer/scripts/send_photo.py "$(cat /tmp/path.txt)" "Screenshot da tela"

# Ou em uma linha (Windows):
python -c "
import subprocess, sys
r = subprocess.run(['python', 'skills/computer/scripts/screenshot.py'], capture_output=True, text=True)
path = r.stdout.strip()
subprocess.run(['python', 'skills/computer/scripts/send_photo.py', path, 'Screenshot da tela'])
"
```

## click.py — clicar, digitar, pressionar teclas

```bash
# Clicar em coordenada
python skills/computer/scripts/click.py 960 540

# Clicar com botão direito
python skills/computer/scripts/click.py 960 540 right

# Focar janela pelo nome (busca parcial, case-insensitive)
python skills/computer/scripts/click.py --window "powershell"
python skills/computer/scripts/click.py --window "terminal"

# Pressionar tecla
python skills/computer/scripts/click.py --key enter
python skills/computer/scripts/click.py --key y

# Digitar texto
python skills/computer/scripts/click.py --type "yes"

# Hotkey (ex: Ctrl+C)
python skills/computer/scripts/click.py --hotkey ctrl c
```

## yes_terminal.py — aprovar prompts pendentes no terminal

Caso de uso: usuário saiu de casa e tem um `[Y/n]` esperando no terminal.

```bash
# Aprovar 1x no primeiro terminal encontrado
python skills/computer/scripts/yes_terminal.py

# Aprovar múltiplas vezes (ex: npm install pedindo confirmações)
python skills/computer/scripts/yes_terminal.py --times 5

# Focar janela específica
python skills/computer/scripts/yes_terminal.py --window "Windows PowerShell"
```

## Fluxo recomendado para controle remoto

1. Tirar screenshot para ver o estado atual da tela
2. Identificar o que precisa ser feito (prompt aguardando, janela ativa, etc.)
3. Usar click.py ou yes_terminal.py para executar a ação
4. Tirar outro screenshot para confirmar o resultado

## Descobrir coordenadas

Se precisar clicar em posição específica, tire um screenshot, analise a imagem e estime as coordenadas. A resolução padrão do PC é visível no screenshot.

## Listar janelas abertas

```bash
python -c "import pygetwindow as gw; [print(w.title) for w in gw.getAllWindows() if w.title]"
```
