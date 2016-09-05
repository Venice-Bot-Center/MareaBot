import logging
import os

APP_NAME = "name"
APP_DIR = os.path.dirname(os.path.realpath(__file__))

DATABASE_NAME = "name.sqlite"
DATABASE = 'sqlite:///%s' % os.path.join(APP_DIR, DATABASE_NAME)

DEBUG = True  # Set to False for production
SECRET_KEY = '''Secret'''  # Used by Flask to encrypt session cookie.

# Logger Config
LOG_NAME = APP_NAME + ".log"
MAXBYTES = 1000
BACKUPCOUNT = 1
DEBUG_LEVEL = logging.DEBUG

# Twitter settings
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
