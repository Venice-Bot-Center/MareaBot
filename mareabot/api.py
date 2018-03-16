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
    def __init__(self, previsione, estremale, tipo, valore):
        self.data_previsione = previsione
        self.data_estremale = estremale
        self.tipo = tipo
        self.valore = valore

    def short_string(self, soglia=-200):
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


def reading_api():
    input_dict = json.loads(requests.get(MAREA_API_URL).text)
    previsions = []
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"],
                       data["TIPO_ESTREMALE"], data["VALORE"])
        previsions.append(d)
    return previsions
