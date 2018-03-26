import telegram

from mareabot.config import TELEGRAM_TOKEN as token, TELEGRAM_CHANNEL as channel


def telegram_send(text, user):
    bot = telegram.Bot(token)
    bot.send_message(chat_id=user, text=text)


def telegram_channel_send(text):
    bot = telegram.Bot(token)
    bot.send_message(chat_id=channel, text=text)


if __name__ == '__main__':
    telegram_send("prova", channel)
