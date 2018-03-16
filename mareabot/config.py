import os

NAME_CONFIG = 'mareabot.config'
DEFAULT_VALUE = None

# Telegram settings
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', DEFAULT_VALUE)
TELEGRAM_CHANNEL = os.getenv('TELEGRAM_CHANNEL', DEFAULT_VALUE)
