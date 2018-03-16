import logging

from telegram import ParseMode
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.ext import Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class BotManager:
    def __init__(self, token, port):
        logging.info("Init the bot")
        self.updater = Updater(token)
        self.token = token
        self.port = port

    def start(self, develop):
        logging.info("Starting the bot")
        if develop is False:
            self.updater.start_webhook(listen="0.0.0.0",
                                       port=self.port,
                                       url_path=self.token)
            self.updater.bot.setWebhook(
                "https://mareabot.herokuapp.com/" + self.token)
        else:
            self.updater.start_polling()
        self.updater.idle()

    def command_handler(self, name):
        def decorator(f):
            self.updater.dispatcher.add_handler(CommandHandler(name, f))
            return f

        return decorator

    def location_generator(self, name: str, text: str, latlon: object) -> function:
        @self.command_handler(name)
        def decoreted(bot, update):
            logging.info("Give the " + name + " info")
            bot.sendMessage(chat_id=update.message.from_user.id,
                            text=text, parse_mode=ParseMode.MARKDOWN)
            lat, lon = latlon
            bot.sendLocation(chat_id=update.message.from_user.id,
                             latitude=lat, longitude=lon)
        return decoreted

    def text_generator(self, name: str, text: str, keyboard: object = None) -> function:
        @self.command_handler(name)
        def decoreted(bot, update):
            logging.info("Press the " + name)
            if keyboard is not None:
                replymarkup = ReplyKeyboardMarkup(keyboard,
                                                  resize_keyboard=True,
                                                  one_time_keyboard=True)
                bot.sendMessage(chat_id=update.message.from_user.id,
                                text=text,
                                reply_markup=replymarkup, parse_mode=ParseMode.MARKDOWN)
            else:
                bot.sendMessage(chat_id=update.message.from_user.id,
                                text=text, parse_mode=ParseMode.MARKDOWN)
        return decoreted
