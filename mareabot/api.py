# coding=utf-8
import json
import logging
import re
from bs4 import BeautifulSoup

import requests

from mareabot.model import Previsione, DBIstance
from mareabot.social import telegram_api

logger = logging.getLogger("MareaBot")

MAREA_API_URL = (
    "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"
)
MAREA_ISTANTANEA_API = "https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Punta_Salute.html"

VENTO_ISTANTANEO_API = (
    "https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/trimestrale"
    "/Stazione_DigaSudLido.html"
)


def get_vento(html_data: str) -> (float, float):
    bs = BeautifulSoup(html_data, "html.parser")

    vv_last = vvmax_last = None
    for row in bs.findAll("tr"):
        aux = row.findAll("td")
        if len(aux) == 6:
            gg, ora, liv, vv, vv_max, dv = aux
            if vv.text != "":
                vv_last = vv
                vvmax_last = vv_max
            else:
                return float(vv_last.text) * 3.6, float(vvmax_last.text) * 3.6
    return 0.0, 0.0


def get_istantanea_marea(html_data: str) -> int:
    bs = BeautifulSoup(html_data, "html.parser")

    liv_last = None
    for row in bs.findAll("tr"):
        aux = row.findAll("td")
        if len(aux) == 4:
            gg, ora, liv, th2o = aux
            if liv.text != "":
                liv_last = liv
            else:
                return int(float(liv_last.text) * 100)
    return 0


def posting_instant(db_istance: DBIstance, maximum: int = 110):
    estended = ""
    hight = get_istantanea_marea(requests.get(MAREA_ISTANTANEA_API).text)
    vento, vento_max = get_vento(requests.get(VENTO_ISTANTANEO_API).text)
    db_dato = 0 if db_istance.instante is None else db_istance.instante

    if int(hight) == int(db_dato):
        return

    db_istance.instante = hight

    if int(maximum) <= int(hight):
        estended = f"Ultima misurazione è cm {hight}\nIl vento è {vento:.2f} km/h e al massimo il vento è {vento_max:.2f} km/h"

    if db_istance.message_hight is not None:
        telegram_api.telegram_channel_delete_message(db_istance.message_hight)

    if estended != "":
        message, flag = telegram_api.telegram_channel_send(estended)
        if flag:
            db_istance.message_hight = message.message_id


def reading_api():
    datas = json.loads(requests.get(MAREA_API_URL).text)
    db_istance = DBIstance()
    adding_data(datas, db_istance)
    posting_instant(db_istance)


def posting(maximum: int, db_istance: DBIstance, hight: int = 94):
    estended = ""
    if int(maximum) >= hight:
        for s in db_istance.prevision:
            estended += s.long_string(hight)
    try:
        if db_istance.message is not None:
            telegram_api.telegram_channel_delete_message(db_istance.message)
    except Exception as e:
        logger.error(e)

    if estended != "":
        message, flag = telegram_api.telegram_channel_send(estended)
        if flag:
            db_istance.message = message.message_id


def adding_data(input_dict: dict, db_istance: DBIstance):
    if db_istance.last == input_dict[0]["DATA_PREVISIONE"]:
        return
    maximum = -400
    for data in input_dict:
        d = Previsione(
            data["DATA_PREVISIONE"],
            data["DATA_ESTREMALE"],
            data["TIPO_ESTREMALE"],
            data["VALORE"],
        )
        maximum = max(int(maximum), int(data["VALORE"]))
        db_istance.prevision.append(d)
        db_istance.last = input_dict[0]["DATA_PREVISIONE"]
    posting(maximum=maximum, db_istance=db_istance)
