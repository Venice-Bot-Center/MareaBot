import os

import requests
from loguru import logger

TOKEN = os.environ.get("TELEGRAM_KEY", "")
CHANNEL = os.environ.get("TELEGRAM_CHANNEL", "")


def telegram_send(text: str, user: str) -> (int, bool):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    message = {
        "chat_id": user,
        "text": text,
        "parse_mode": "Markdown"
    }
    r = requests.post(url=url, json=message)
    logger.info(r.json())
    if r.json()["ok"] == True:
        return r.json()["result"]['message_id'], True
    else:
        return None, False


def telegram_channel_send(text: str) -> (int, bool):
    return telegram_send(text, CHANNEL)


def telegram_channel_delete_message(message_id: int, chat: str = CHANNEL) -> bool:
    url = f"https://api.telegram.org/bot{TOKEN}/deleteMessage"
    message = {
        "chat_id": chat,
        "message_id": message_id
    }
    r = requests.get(url=url, json=message)
    logger.info(r.json())
    if r.json()["ok"] == True:
        return True
    else:
        return False
