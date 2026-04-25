import requests
import os
from app.db import save_token, load_token
import time

BASE_URL = os.getenv("BASE_URL")
PLATFORM_NAME = os.getenv("PLATFORM_NAME")
PLATFORM_KEY = os.getenv("PLATFORM_KEY")
PLATFORM_SECRET = os.getenv("PLATFORM_SECRET")

def initiate_handshake():
    url = f"{BASE_URL}/initiate-handshake"

    payload = {
        "platform_name": PLATFORM_NAME,
        "platform_key": PLATFORM_KEY,
        "platform_secret": PLATFORM_SECRET,
        "callback_url": "https://your-domain.com/callback"
    }

    res = requests.post(url, json=payload)
    data = res.json()

    if data.get("success"):
        save_token(
            data["data"]["handshake_token"],
            data["data"]["expires_in_seconds"]
        )

    return data

def complete_handshake():
    token_data = load_token()

    if not token_data:
        return {"error": "No token found"}

    if time.time() > token_data["expires_at"]:
        return {"error": "Token expired"}

    url = f"{BASE_URL}/complete-handshake"

    payload = {
        "handshake_token": token_data["token"],
        "platform_key": PLATFORM_KEY
    }

    res = requests.post(url, json=payload)
    return res.json()
