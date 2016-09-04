import logging
from logging.handlers import RotatingFileHandler

from flask import (Flask)
from flask_sqlalchemy import SQLAlchemy

import task
from config import FILE_LOG, MAXBYTE, BACKUPCOUNT, APP_DIR, DATABASE, DEBUG, SECRET_KEY, LOGGING_LEVEL,APP_NAME

app = Flask(APP_NAME)
db = SQLAlchemy(app)
handler = RotatingFileHandler(FILE_LOG, maxBytes=MAXBYTE, backupCount=BACKUPCOUNT)
handler.setLevel(LOGGING_LEVEL)
app.logger.addHandler(handler)

if __name__ == '__main__':
    app.run()
