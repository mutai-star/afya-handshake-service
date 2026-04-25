import sqlite3
import time
from app.security import get_cipher

DB_PATH = "instance/tokens.db"
cipher = get_cipher()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS handshake (
            id INTEGER PRIMARY KEY,
            token TEXT,
            expires_at REAL
        )
    """)
    conn.commit()
    conn.close()

def save_token(token, expires_in):
    encrypted = cipher.encrypt(token.encode()).decode()
    expires_at = time.time() + expires_in

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM handshake")
    c.execute("INSERT INTO handshake (token, expires_at) VALUES (?, ?)",
              (encrypted, expires_at))
    conn.commit()
    conn.close()

def load_token():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT token, expires_at FROM handshake LIMIT 1")
    row = c.fetchone()
    conn.close()

    if not row:
        return None

    token = cipher.decrypt(row[0].encode()).decode()

    return {
        "token": token,
        "expires_at": row[1]
    }
