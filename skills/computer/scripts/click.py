"""
Clica em coordenadas na tela ou em texto visível (image search).
Uso:
  python click.py x y [button]          # clica em coordenada (button: left/right/middle)
  python click.py --text "Ok"           # localiza texto/imagem e clica (requer pytesseract)
  python click.py --window "terminal"   # foca janela e pressiona Enter
"""
import sys
import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1

args = sys.argv[1:]

if not args:
    print("Uso: click.py x y [button] | --window nome | --key tecla")
    sys.exit(1)

if args[0] == "--window":
    import pygetwindow as gw
    nome = " ".join(args[1:]).lower()
    wins = [w for w in gw.getAllWindows() if nome in w.title.lower()]
    if not wins:
        print(f"ERRO: janela '{nome}' não encontrada")
        print("Janelas abertas:")
        for w in gw.getAllWindows():
            if w.title:
                print(f"  - {w.title}")
        sys.exit(1)
    win = wins[0]
    win.activate()
    time.sleep(0.5)
    print(f"OK: janela '{win.title}' ativada")

elif args[0] == "--key":
    key = args[1] if len(args) > 1 else "enter"
    pyautogui.press(key)
    print(f"OK: tecla '{key}' pressionada")

elif args[0] == "--type":
    text = " ".join(args[1:])
    pyautogui.typewrite(text, interval=0.05)
    print(f"OK: digitado '{text}'")

elif args[0] == "--hotkey":
    keys = args[1:]
    pyautogui.hotkey(*keys)
    print(f"OK: hotkey {'+'.join(keys)}")

else:
    try:
        x, y = int(args[0]), int(args[1])
        button = args[2] if len(args) > 2 else "left"
        pyautogui.click(x, y, button=button)
        print(f"OK: clicou em ({x}, {y}) botão={button}")
    except (ValueError, IndexError):
        print(f"ERRO: argumentos inválidos: {args}")
        sys.exit(1)
