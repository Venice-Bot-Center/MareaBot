# coding=utf-8
from tweepy import TweepError

from mareabot import twitter,telegram
from mareabot.model import Previsione


def posting(prev):
    shorted = ""
    estended= ""
    for s in prev.previsions:
        shorted += s.short_string()
        estended += s.long_string()
    try:
        twitter.tweet_status(shorted)
    except TweepError as e:
        print (e.reason)
    try:
        telegram.telegram_channel_send(estended)
    except Exception as e:
        print (e.message)


def adding_data(input_dict):
    PREV.previsions = []
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        PREV.previsions.append(d)
        PREV.last = input_dict[0]["DATA_PREVISIONE"]
    posting(PREV)
