import os

APP_NAME = "name"
APP_DIR = os.path.dirname(os.path.realpath(__file__))

DATABASE_NAME = "name.sqlite"
DATABASE = 'sqlite:///%s' % os.path.join(APP_DIR, DATABASE_NAME)

DEBUG = False
SECRET_KEY = '''Secret'''  # Used by Flask to encrypt session cookie.

#Logger Config
LOG_NAME=APP_NAME +".log"
MAXBYTES=1000
BACKUPCOUNT=1

#Twitter settings
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""