import telepot

from mareabot.config import TELEGRAM_TOKEN


def telegram_send(text, user):
    bot = telepot.Bot(TELEGRAM_TOKEN)
    bot.sendMessage(user, text)
