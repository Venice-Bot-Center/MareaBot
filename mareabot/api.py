# coding=utf-8
import json

import requests

from mareabot.model import Previsione, MemoPrev
from mareabot.social import telegram_api

MAREA_API_URL = "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"


def reading_api():
    prev = MemoPrev()
    datas = json.loads(requests.get(MAREA_API_URL).text)
    if prev.last != datas[0]["DATA_PREVISIONE"]:
        adding_data(datas, prev)


def posting(prev):
    shorted = ""
    estended = ""
    flag = False
    for s in prev.previsions:
        if int(s.valore) >= 100:
            flag = True
        if len(shorted) + len(s.short_string()) > 132:
            broadcasting_text("1/2 \n" + shorted, "", False)
            shorted = "2/2 \n"
        shorted += s.short_string()
        estended += s.long_string()
    broadcasting_text(shorted, estended, flag)


def broadcasting_text(short, long, flag):
    if flag == True:
        try:
            telegram_api.telegram_channel_send(long)
        except Exception as e:
            print(e)


def adding_data(input_dict, prev):
    prev.previsions = []
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        prev.previsions.append(d)
        prev.last = input_dict[0]["DATA_PREVISIONE"]
    posting(prev)
