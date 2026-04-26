import requests
import time
from app.db import store_token, get_token

BASE_URL = "https://staging.collabmed.net/api/external"

PLATFORM_KEY = "afya_2d00d74512953c933172ab924f5073fa"
PLATFORM_SECRET = "e0502a5c052842cf19d0305455437b791d201761c88e2ad641680b2d5d356ba8"

def initiate_handshake():
    payload = {
        "platform_name": "Test Platform v2",
        "platform_key": PLATFORM_KEY,
        "platform_secret": PLATFORM_SECRET,
        "callback_url": "https://example.com/callback"
    }

    try:
        res = requests.post(f"{BASE_URL}/initiate-handshake", json=payload, timeout=10)

        if res.status_code != 200:
            return {"error": res.text}

        data = res.json()

        if data.get("success"):
            store_token(data["data"]["handshake_token"], time.time())

        return data

    except Exception as e:
        return {"error": str(e)}


def complete_handshake():
    token = get_token()

    if not token:
        return {"error": "No token found"}

    payload = {
        "handshake_token": token["token"],
        "platform_key": PLATFORM_KEY
    }

    res = requests.post(f"{BASE_URL}/complete-handshake", json=payload)
    return res.json()
