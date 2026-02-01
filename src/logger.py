from datetime import datetime
from config import LOG_FILE


def write_log(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {key}\n")
