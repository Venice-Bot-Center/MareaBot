# coding=utf-8

import json
import requests

MAREA_API_URL = "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"

RED_CIRCLE = "🔴"
GRAY_CIRCLE = "🔘"
UP = "🔺"
DOWN = "🔻"
TIMEWATCH = "⌚"
CALENDAR = "📆"


class Previsione():
    """Class of the prevision
    """

    previsions = []
    maximum = -200
    date_prev = ""

    def __init__(self):
        self.reading_api()

    def reading_api(self):
        """Download the latest marea data from the api
        """
        input_dict = json.loads(requests.get(MAREA_API_URL).text)
        for data in input_dict:
            self.data_prev = data["DATA_PREVISIONE"]
            self.maximum = max(self.maximum, int(data["VALORE"]))
            d = self.DatoPrevisione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"],
                                    data["TIPO_ESTREMALE"], data["VALORE"])
            self.previsions.append(d)

    def get_previsione(self, print_all=False, allert_minimum=95, long=True):
        """Get the data in a formatted string

        Keyword Arguments:
            print_all {bool} -- [Print all value of the prevision ignoring the allert_minimum] (default: {False})
            allert_minimum {int} -- [Minimum int for be in the output] (default: {95})
            long {bool} -- [Long format string or short] (default: {True})

        Returns:
            [String] -- [String with the data of marea]
        """

        stringa = ""
        self.previsions.sort()
        if self.maximum >= allert_minimum:
            if print_all:
                allert_minimum = -500
            for element in self.previsions:
                if long:
                    stringa += element.long_string(allert_minimum)
                else:
                    stringa += element.short_string(allert_minimum)
        return stringa

    class DatoPrevisione():
        """ Single line of marea data
        """

        def __init__(self, previsione, estremale, tipo, valore):
            self.data_previsione = previsione
            self.data_estremale = estremale
            self.tipo = tipo
            self.valore = valore

        def short_string(self, soglia=-200):
            """Elaborate the data in a short string

            Keyword Arguments:
                soglia {int} -- [Minimum for be in the string] (default: {-200})

            Returns:
                [string] -- [String with the data]

            """
            date, time = self.data_estremale.split(" ")
            date = date.split("-")[2]
            t = time.split(":")
            time = t[0] + ":" + t[1]

            if len(self.valore) == 1:
                self.valore = "0" + self.valore

            text = ""
            if int(self.valore) > soglia:
                if self.tipo == "min":
                    text += DOWN
                else:
                    text += UP
                text += str(self.valore) + TIMEWATCH + str(time) + \
                    CALENDAR + str(date) + "\n"
            return text

        def long_string(self, soglia=-200):
            """Elaborate the data in a long string

            Keyword Arguments:
                soglia {int} -- [Minimum for be in the string] (default: {-200})

            Returns:
                [string] -- [String with the data]
            """

            date, time = self.data_estremale.split(" ")
            text = ""
            if int(self.valore) > soglia:
                if self.tipo == "min":
                    text += DOWN
                else:
                    text += UP
                text += str(self.valore) + " " + TIMEWATCH + \
                    str(time) + " " + CALENDAR + str(date) + "\n"
            return text

        def __lt__(self, other):
            return self.data_estremale < other.data_estremale
