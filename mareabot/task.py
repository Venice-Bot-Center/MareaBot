# coding=utf-8

from mareabot import twitter,telegram
from mareabot.model import Previsione, PREV


def posting():
    shorted = ""
    estended= ""
    for s in PREV.previsions:
        shorted += s.short_string()
        estended += s.long_string()
    twitter.tweet_status(shorted)
    telegram.telegram_channel_send(estended)


def adding_data(input_dict):
    PREV.previsions = []
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        PREV.previsions.append(d)
        PREV.last = input_dict[0]["DATA_PREVISIONE"]
    posting()
