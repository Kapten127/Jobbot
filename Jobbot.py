import requests
import time

# Din Telegram-bot token
TOKEN = '8096869303:AAFbIwiiD_Uwugpkxu4lT_rvfPW_kuWZPzw'
CHAT_ID = 'me'  # 'me' skickar till dig själv

def hamta_jobben(yrke, plats):
    url = "https://jobsearch.api.jobtechdev.se/search"
    params = {
        "q": yrke,
        "region": plats,
        "limit": 5
    }
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, params=params, headers=headers)
    resultat = []
    if response.status_code == 200:
        data = response.json()
        for annons in data.get("hits", []):
            titel = annons['headline']
            länk = annons['webpage_url']
            resultat.append(f"{titel}\n{länk}")
    return resultat

def skicka_telegrammeddelande(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

# Hämta jobb
lagerjobb = hamta_jobben("lager", "Stockholm")
butiksjobb = hamta_jobben("butik", "Stockholm")

# Skicka till Telegram
skicka_telegrammeddelande("📦 Lagerjobb i Stockholm:")
for jobb in lagerjobb:
    skicka_telegrammeddelande(jobb)
    time.sleep(1)

skicka_telegrammeddelande("🛒 Butiksjobb i Stockholm:")
for jobb in butiksjobb:
    skicka_telegrammeddelande(jobb)
    time.sleep(1)
