import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates():
    r = requests.get(f"{URL}/getUpdates")
    return r.json()

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", data={
        "chat_id": chat_id,
        "text": text
    })

if __name__ == "__main__":
    updates = get_updates()

    for update in updates.get("result", []):
        message = update.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        text = message.get("text", "")

        if chat_id and text:
            print(f"Mensaje recibido: {text}")
            send_message(
                chat_id,
                f"🏠 Estoy buscando pisos en Jaca...\n\nHas dicho: {text}"
            )
