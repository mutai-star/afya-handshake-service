import base64, hashlib
from cryptography.fernet import Fernet
import os

def get_cipher():
    secret = os.getenv("SECRET_KEY", "default_key")
    key = base64.urlsafe_b64encode(hashlib.sha256(secret.encode()).digest())
    return Fernet(key)
