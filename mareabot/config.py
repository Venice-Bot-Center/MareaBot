try:
    import ConfigParser as configparser
except:
    import configparser

NAME_CONFIG = 'mareabot.config'


class Configuration():
    Config = configparser.ConfigParser()

    def __init__(self, name):
        try:
            self.Config.readfp(open(name))
        except IOError:
            self.new_config(name)

    def new_config(self, name):
        cfgfile = open("example" + name, 'w')
        self.Config.add_section('Twitter')
        self.Config.set('Twitter', 'CONSUMER_KEY', "")
        self.Config.set('Twitter', 'CONSUMER_SECRET', "")
        self.Config.set('Twitter', 'ACCESS_TOKEN', "")
        self.Config.set('Twitter', 'ACCESS_TOKEN_SECRET', "")

        self.Config.add_section('Telegram')
        self.Config.set('Telegram', 'TOKEN', "")
        self.Config.set('Telegram', 'Channel', "")

        self.Config.add_section('Marea')
        self.Config.set('Marea', 'Last', "")
        self.Config.write(cfgfile)
        cfgfile.close()

    def set_latest(self, latest):
        cfgfile = open(NAME_CONFIG, 'w')
        self.Config.set('Marea', 'Last', latest)
        self.Config.write(cfgfile)

    def get_latest(self):
        return self.Config.get('Marea', 'Last')

    def get_telegram(self):
        return self.Config.get("Telegram", "TOKEN"), self.Config.get(
            "Telegram", "Channel")

    def gettwitter(self):
        return self.Config.get('Twitter', 'CONSUMER_KEY'), self.Config.get(
            'Twitter', 'CONSUMER_SECRET'), self.Config.get(
                'Twitter', 'ACCESS_TOKEN'), self.Config.get(
                    'Twitter', 'ACCESS_TOKEN_SECRET')


c = Configuration(NAME_CONFIG)

# Twitter settings
CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = c.gettwitter(
)
TELEGRAM_TOKEN, TELEGRAM_CHANNEL = c.get_telegram()
