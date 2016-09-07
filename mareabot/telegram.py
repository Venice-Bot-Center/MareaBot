import telepot

from mareabot.config import TELEGRAM_TOKEN as token, TELEGRAM_CHANNEL as channel


def telegram_send(text, user):
    bot = telepot.Bot(token)
    bot.sendMessage(user, text)

def telegram_channel_send(text):
    bot = telepot.Bot(token)
    bot.sendMessage(channel, text)

if __name__ == '__main__':
    telegram_send("prova",channel)