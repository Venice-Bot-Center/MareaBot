# coding=utf-8
import json

import requests
from tweepy import TweepError

from mareabot.model import Previsione, MemoPrev
from mareabot.social import telegram_api, twitter_api, facebook_api

MAREA_API_URL = "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"


def reading_api():
    prev = MemoPrev()
    datas = json.loads(requests.get(MAREA_API_URL).text)
    if not prev.previsions:
        adding_data(datas, prev)
    else:
        if prev.last != datas[0]["DATA_PREVISIONE"]:
            adding_data(datas, prev)


def posting(prev):
    shorted = ""
    estended = ""
    for s in prev.previsions:
        shorted += s.short_string()
        estended += s.long_string()
    broadcasting_text(shorted, estended)


def broadcasting_text(short, long):
    try:
        twitter_api.tweet_status(short)
    except TweepError as e:
        print (e.reason)
    try:
        telegram_api.telegram_channel_send(long)
    except Exception as e:
        print (e.message)

    try:
        facebook_api.facebook_post_page(long)
    except Exception as e:
        print (e.message)


def adding_data(input_dict, prev):
    prev.previsions = []
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        prev.previsions.append(d)
        prev.last = input_dict[0]["DATA_PREVISIONE"]
    posting(prev)
