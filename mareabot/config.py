import os

import configparser

config = configparser.ConfigParser()

APP_NAME = "name"
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqlite:///%s' % os.path.join(APP_DIR, 'mareabot.sqlite')

DEBUG = False
SECRET_KEY = '''It's a secret for EVERYBODY '''  # Used by Flask to encrypt session cookie.
