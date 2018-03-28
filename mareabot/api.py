# coding=utf-8
import json

import requests

from mareabot.model import Previsione, DBIstance
from mareabot.social import telegram_api
import logging

logger = logging.getLogger("MareaBot")

MAREA_API_URL = "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"

DB_I = DBIstance()


def reading_api():
    datas = json.loads(requests.get(MAREA_API_URL).text)
    if DB_I.last != datas[0]["DATA_PREVISIONE"]:
        adding_data(datas)


def posting(maximum, hight=94):
    estended = ""
    if int(maximum) >= hight:
        for s in DB_I.prevision:
            estended += s.long_string(hight)
    try:
        if DB_I.message is None:
            telegram_api.telegram_channel_delete_message(DB_I.message)
    except Exception as e:
        logger.error(e)

    try:
        if estended != "":
            message = telegram_api.telegram_channel_send(estended)
            DB_I.message = message.message_id
    except Exception as e:
        logger.error(e)


def adding_data(input_dict):
    maximum = -400
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        maximum = max(int(maximum), int(data["VALORE"]))
        DB_I.prevision.append(d)
        DB_I.last = input_dict[0]["DATA_PREVISIONE"]
    posting(maximum=maximum)
