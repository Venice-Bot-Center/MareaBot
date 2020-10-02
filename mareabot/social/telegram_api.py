import os

import telegram
from telegram import Message

TOKEN = os.environ.get("TELEGRAM_KEY", "")
CHANNEL = os.environ.get("TELEGRAM_CHANNEL", "")


def telegram_send(text: str, user: str):
    bot = telegram.Bot(TOKEN)
    bot.send_message(chat_id=user, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
    bot.delete_webhook()


def telegram_channel_send(text: str) -> (Message, bool):
    bot = telegram.Bot(TOKEN)
    try:
        out =  (
            bot.send_message(
                chat_id=CHANNEL, text=text, parse_mode=telegram.ParseMode.MARKDOWN
            ),
            True,
        )
        bot.delete_webhook()
        return out
    except telegram.TelegramError:
        return None, False


def telegram_channel_delete_message(message_id: str, chat: str = CHANNEL) -> bool:
    bot = telegram.Bot(TOKEN)
    try:
        out= bot.delete_message(chat_id=chat, message_id=message_id)
        bot.delete_webhook()
        return out
    except telegram.TelegramError:
        return False
