# -*- coding: utf-8 -*-
from os import environ

from mareabot.bot import BotManager

TOKEN = environ.get('TELEGRAM_KEY')
PORT = int(environ.get('PORT', '5000'))
DEVELOP = environ.get('DEVELOP', False)

mybot = BotManager(TOKEN, PORT)

if __name__ == '__main__':
    flag = None
    if not DEVELOP:
        flag = False
    else:
        flag = True
    mybot.start(flag)
