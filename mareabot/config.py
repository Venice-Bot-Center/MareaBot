import os
NAME_CONFIG = 'mareabot.config'


class Configuration():

    def set_latest(self, latest):
        cfgfile = open(NAME_CONFIG, 'w')
        self.Config.set('Marea', 'Last', latest)
        self.Config.write(cfgfile)

    def get_latest(self):
        return self.Config.get('Marea', 'Last')

    def get_telegram(self):
        return os.environ.get("TELEGRAM_KEY",""), os.environ.get("TELEGRAM_CHANNEL","")

    def gettwitter(self):
        return self.Config.get('Twitter', 'CONSUMER_KEY'), self.Config.get(
            'Twitter', 'CONSUMER_SECRET'), self.Config.get(
                'Twitter', 'ACCESS_TOKEN'), self.Config.get(
                    'Twitter', 'ACCESS_TOKEN_SECRET')


TELEGRAM_TOKEN, TELEGRAM_CHANNEL = Configuration().get_telegram()
