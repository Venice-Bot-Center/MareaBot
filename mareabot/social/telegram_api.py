import os

import telegram
from telegram import Message

TOKEN = os.environ.get("TELEGRAM_KEY", "")
CHANNEL = os.environ.get("TELEGRAM_CHANNEL", "")


def telegram_send(text: str, user: str):
    bot = telegram.Bot(TOKEN)
    bot.send_message(chat_id=user, text=text)


def telegram_channel_send(text: str) -> Message:
    bot = telegram.Bot(TOKEN)
    return bot.send_message(chat_id=CHANNEL, text=text)


def telegram_channel_delete_message(message_id: str, chat: str = CHANNEL) -> bool:
    bot = telegram.Bot(TOKEN)
    try:
        return bot.delete_message(chat_id=chat, message_id=message_id)
    except telegram.error.BadRequest:
        return False
