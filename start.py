# -*- coding: utf-8 -*-
from os import environ

from mareabot.bot import BotManager

TOKEN = environ.get('TOKEN')
PORT = int(environ.get('PORT', '5000'))
DEVELOP = environ.get('DEVELOP', False)

mybot = BotManager(TOKEN, PORT)

if __name__ == '__main__':
    mybot.start(DEVELOP)
