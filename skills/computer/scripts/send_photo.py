"""
Envia uma imagem para o Telegram do Mestre.
Uso: python send_photo.py <caminho_da_imagem> [caption]

Exemplo:
  python send_photo.py C:\Temp\screenshot.png "Aqui está a tela"
"""
import sys
import os
import requests

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8312200804:AAEhBD1G2dooVoeU7WfrVtWKhIyox5PJ4S8")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "5340740837")

def send_photo(image_path: str, caption: str = "") -> bool:
    if not os.path.exists(image_path):
        print(f"ERRO: arquivo não encontrado: {image_path}", file=sys.stderr)
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as f:
        resp = requests.post(url, data={"chat_id": CHAT_ID, "caption": caption}, files={"photo": f})

    if resp.status_code == 200:
        print(f"OK: imagem enviada — {image_path}")
        return True
    else:
        print(f"ERRO {resp.status_code}: {resp.text}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python send_photo.py <caminho> [caption]", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    caption = sys.argv[2] if len(sys.argv) > 2 else ""
    ok = send_photo(path, caption)
    sys.exit(0 if ok else 1)
