import logging
import os
from logging.handlers import RotatingFileHandler

from flask import (Flask)

from config import APP_DIR,  DEBUG, SECRET_KEY, APP_NAME

app = Flask(APP_NAME)

handler = RotatingFileHandler(os.path.join(APP_DIR, 'marea.log'), maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

if __name__ == '__main__':
    from mareabot.api.task import set_task
    set_task()
    app.logger.info('Start thre app')
    app.run()
