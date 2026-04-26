import json
import os

FILE = "/tmp/token_store.json"

def store_token(token, timestamp):
    with open(FILE, "w") as f:
        json.dump({"token": token, "time": timestamp}, f)

def get_token():
    if not os.path.exists(FILE):
        return None

    with open(FILE, "r") as f:
        return json.load(f)
