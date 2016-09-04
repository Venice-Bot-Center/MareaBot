import logging
import os
import configparser

config = configparser.ConfigParser()

APP_NAME = "name"
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'mareabot.db')
DEBUG = False
SECRET_KEY = '''It's a secret for EVERYBODY '''  # Used by Flask to encrypt session cookie.

FILE_LOG = 'foo.log'
MAXBYTE = 10000

BACKUPCOUNT = 1

LOGGING_LEVEL = logging.INFO
