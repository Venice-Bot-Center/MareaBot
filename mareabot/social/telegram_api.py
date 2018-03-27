import os

import telegram

TOKEN = os.environ.get("TELEGRAM_KEY", "")
CHANNEL = os.environ.get("TELEGRAM_CHANNEL", "")


def telegram_send(text, user):
    bot = telegram.Bot(TOKEN)
    bot.send_message(chat_id=user, text=text)


def telegram_channel_send(text):
    bot = telegram.Bot(TOKEN)
    return bot.send_message(chat_id=CHANNEL, text=text)


if __name__ == '__main__':
    telegram_send("prova", CHANNEL)


def telegram_channel_delete_message(message_id, chat=CHANNEL):
    bot = telegram.Bot(TOKEN)
    return bot.delete_message(chat_id=chat, message_id=message_id)
