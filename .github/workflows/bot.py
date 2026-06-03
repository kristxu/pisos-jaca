import os
import requests
import json

TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

SEEN_FILE = "seen.json"

# -----------------------
# CONFIG (TU FILTRO)
# -----------------------
MAX_PRICE = 700
LOCATION = "Jaca"

def load_seen():
    try:
        with open(SEEN_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()

def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", data={
        "chat_id": chat_id,
        "text": text
    })

def get_chat_id():
    r = requests.get(f"{URL}/getUpdates").json()
    for u in r.get("result", []):
        if "message" in u:
            return u["message"]["chat"]["id"]
    return None

# -----------------------
# SIMULADOR (lo cambiamos luego por datos reales)
# -----------------------
def scraper_pisos():
    return [
        {"id": "1", "title": "Piso centro Jaca 2 hab larga estancia", "price": 650, "type": "larga"},
        {"id": "2", "title": "Piso temporada esquí Jaca 3 hab", "price": 700, "type": "temporada"},
        {"id": "3", "title": "Apartamento Jaca fijo 1 hab", "price": 720, "type": "larga"},
        {"id": "4", "title": "Piso alquiler anual Jaca 2 hab", "price": 680, "type": "larga"},
    ]

def is_valid(piso):
    # filtro precio
    if piso["price"] > MAX_PRICE:
        return False

    # excluir temporada
    if "temporada" in piso["type"]:
        return False

    if "esquí" in piso["title"].lower():
        return False

    return True

# -----------------------
# MAIN
# -----------------------
def main():
    def main():
    chat_id = get_chat_id()
    print("CHAT_ID DETECTADO:", chat_id)

    if not chat_id:
        print("No chat_id aún")
        return

    seen = load_seen()
    pisos = scraper_pisos()

    for p in pisos:
        if p["id"] in seen:
            continue

        if is_valid(p):
            send_message(
                chat_id,
                f"🏠 NUEVO PISO EN JACA\n\n"
                f"{p['title']}\n"
                f"💶 {p['price']}€\n"
                f"📍 {LOCATION}"
            )
            seen.add(p["id"])

    save_seen(seen)

if __name__ == "__main__":
    main()
