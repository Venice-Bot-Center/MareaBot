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
MAREA_ISTANTANEA_API = "https://www.comune.venezia.it/it/content/centro-previsioni-e-segnalazioni-maree-beta"


def istantanea_marea():
    get_url = requests.get(MAREA_ISTANTANEA_API)
    get_text = get_url.text
    soup = BeautifulSoup(get_text, "html.parser")
    try:
        company = soup.findAll("b", class_="text-marea-line5")[0].text
    except:
        try:
            company = soup.findAll("b", class_="text-marea-line4")[0].text
        except:
            try:
                company = soup.findAll("b", class_="text-marea-line3")[0].text
            except:
                try:
                    company = soup.findAll("b", class_="text-marea-line2")[0].text
                except:
                    company = soup.findAll("b", class_="text-marea-line1")[0].text
    try:
        number = int(company.split("cm")[0].split("+ ")[1])
    except:
        number = int(company.split("cm")[0].split("- ")[1])
    return number


def posting_instant(db_istance, maximum=110):
    estended = ""
    hight = istantanea_marea()
    db_dato = int(db_istance.instante)
    if db_dato is None:
        db_dato  = 0
    if int(hight) == int(db_dato):
        return
    else:
        db_istance.instante = hight

    if int(maximum) <= int(hight):
        estended = "Ultima misurazione è cm " + str(hight)
    try:
        if db_istance.message_hight is not None:
            telegram_api.telegram_channel_delete_message(db_istance.message_hight)
    except Exception as e:
        logger.error(e)

    try:
        if estended != "":
            message = telegram_api.telegram_channel_send(estended)
            db_istance.message_hight = message.message_id
    except Exception as e:
        logger.error(e)


def reading_api():
    datas = json.loads(requests.get(MAREA_API_URL).text)
    db_istance = DBIstance()
    if db_istance.last != datas[0]["DATA_PREVISIONE"]:
        adding_data(datas, db_istance)
    if int(istantanea_marea()) >= 110:
        posting_instant(db_istance)


def posting(maximum, db_istance, hight=94):
    estended = ""
    if int(maximum) >= hight:
        for s in db_istance.prevision:
            estended += s.long_string(hight)
    try:
        if db_istance.message is not None:
            telegram_api.telegram_channel_delete_message(db_istance.message)
    except Exception as e:
        logger.error(e)

    try:
        if estended != "":
            message = telegram_api.telegram_channel_send(estended)
            db_istance.message = message.message_id
    except Exception as e:
        logger.error(e)


def adding_data(input_dict, db_istance):
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

