import logging
import requests

from telegram import ParseMode
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.ext import Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class BotManager:
    """Manage a telegram's bot
    """

    def __init__(self, token, port):
        logging.info("Init the bot")
        self.updater = Updater(token)
        self.token = token
        self.port = port

    def rapid_send(self, chat_id, text):
        """Send a text to a specific chat

        Arguments:
            chat_id {[int]} -- [Id of the chat (user or group)]
            text {[string]} -- [Text of the message sent]
        """
        params = {'chat_id': chat_id, 'text': text}
        url_worked = "https://api.telegram.org/bot" + \
            self.token+"/getUpdates/sendMessage"
        r = requests.get(url_worked, params=params)
        logging.info(r.status_code)

    def start(self, develop):
        """Start the bot and start the webhook or polling

        Arguments:
            develop {[boolean]} -- [If False use a webhook, if True use a polling]
        """
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
        """Add a command to the bot

        Arguments:
            name {[string]} -- [Name of the command]

        Returns:
            [function] -- [The same function registered]
        """
        def decorator(f):
            self.updater.dispatcher.add_handler(CommandHandler(name, f))
            return f

        return decorator

    def location_generator(self, name: str, text: str, latlon: object):
        """Send a Coordinate to a chat

        Arguments:
            name {str} -- [name of the command]
            text {str} -- [text send into the massege]
            latlon {object} -- [enupla with coordinater (lat,long) send into the message]

        Returns:
            [function] -- [function to send coordinate to a chat]
        """
        @self.command_handler(name)
        def decoreted(bot, update):
            logging.info("Give the " + name + " info")
            bot.sendMessage(chat_id=update.message.from_user.id,
                            text=text, parse_mode=ParseMode.MARKDOWN)
            lat, lon = latlon
            bot.sendLocation(chat_id=update.message.from_user.id,
                             latitude=lat, longitude=lon)
        return decoreted

    def text_generator(self, name, text, keyboard = None):
        """Regist a command to send a message

        Arguments:
            name {str} -- [name of the function]
            text {str} -- [text of the message]

        Keyword Arguments:
            keyboard {object} -- [Keyboard of the possibile action] (default: {None})
        """
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
