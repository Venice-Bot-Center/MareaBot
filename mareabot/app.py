import os
from logging.handlers import RotatingFileHandler

from flask import (Flask)

from mareabot.config import APP_NAME, APP_DIR, LOG_NAME, MAXBYTES, BACKUPCOUNT, DEBUG_LEVEL

app = Flask(APP_NAME)

handler = RotatingFileHandler(os.path.join(APP_DIR, LOG_NAME), maxBytes=MAXBYTES, backupCount=BACKUPCOUNT)
handler.setLevel(DEBUG_LEVEL)
app.logger.addHandler(handler)
