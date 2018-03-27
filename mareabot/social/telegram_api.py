import telegram

from mareabot.config import TELEGRAM_TOKEN as TOKEN, TELEGRAM_CHANNEL as CHANNEL


def telegram_send(text, user):
    bot = telegram.Bot(TOKEN)
    bot.send_message(chat_id=user, text=text)


def telegram_channel_send(text):
    bot = telegram.Bot(TOKEN)
    bot.send_message(chat_id=CHANNEL, text=text)


if __name__ == '__main__':
    telegram_send("prova", CHANNEL)
