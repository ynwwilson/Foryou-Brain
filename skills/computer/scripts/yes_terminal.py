"""
Caso de uso mais comum: aprovar prompts pendentes no terminal.
Foca na janela de terminal ativa e pressiona Y + Enter em todos os prompts visíveis.

Uso: python yes_terminal.py [--window "nome_janela"] [--times N]
"""
import sys
import time
import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = False

# Parse args
window_name = None
times = 1
args = sys.argv[1:]

i = 0
while i < len(args):
    if args[i] == "--window" and i + 1 < len(args):
        window_name = args[i + 1]
        i += 2
    elif args[i] == "--times" and i + 1 < len(args):
        times = int(args[i + 1])
        i += 2
    else:
        i += 1

# Encontra e ativa terminal
terminal_keywords = ["terminal", "powershell", "cmd", "bash", "python", "node", "npm"]

if window_name:
    wins = [w for w in gw.getAllWindows() if window_name.lower() in w.title.lower()]
else:
    wins = []
    for w in gw.getAllWindows():
        if w.title and any(k in w.title.lower() for k in terminal_keywords):
            wins.append(w)

if not wins:
    print("Nenhum terminal encontrado. Janelas abertas:")
    for w in gw.getAllWindows():
        if w.title:
            print(f"  - {w.title}")
    sys.exit(1)

win = wins[0]
print(f"Terminal encontrado: '{win.title}'")
win.activate()
time.sleep(0.8)

# Envia Y + Enter N vezes
for n in range(times):
    pyautogui.typewrite("y", interval=0.05)
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.3)
    print(f"  [{n+1}/{times}] Y + Enter enviado")

print("OK: aprovações enviadas")
