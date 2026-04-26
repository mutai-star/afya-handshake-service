import time

def is_expired(timestamp):
    return time.time() - timestamp > 900
