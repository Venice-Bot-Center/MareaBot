# coding=utf-8
import json

import requests

from mareabot.model import Previsione, DBIstance
from mareabot.social import telegram_api

MAREA_API_URL = "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"

DB_I = DBIstance()


def reading_api():
    datas = json.loads(requests.get(MAREA_API_URL).text)
    if DB_I.last != datas[0]["DATA_PREVISIONE"]:
        adding_data(datas)


def posting(hight=94):
    estended = ""
    for s in DB_I.prevision:
        if int(DB_I.max) >= hight:
            estended += s.long_string(hight)
    try:
        if estended == "":
            telegram_api.telegram_channel_delete_message(DB_I.message)
            message = telegram_api.telegram_channel_send(estended)
            DB_I.message = message.message_id
    except Exception as e:
        print(e)


def adding_data(input_dict):
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        DB_I.max = max(int(DB_I.max),int(data["VALORE"]))
        DB_I.prevision.append(d)
        DB_I.last = input_dict[0]["DATA_PREVISIONE"]
    posting()
