"""
Tira screenshot da tela e salva como PNG.
Uso: python screenshot.py [caminho_saida]
"""
import sys
import os
import pyautogui
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace") if hasattr(sys.stdout, "reconfigure") else None

output = sys.argv[1] if len(sys.argv) > 1 else None

if not output:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    output = os.path.join(os.environ.get("TEMP", "/tmp"), f"jarvis_screen_{ts}.png")

img = pyautogui.screenshot()
img.save(output)
print(output)
