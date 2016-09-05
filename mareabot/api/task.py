# coding=utf-8
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from mareabot.api import Previsione
from mareabot.api import db
from mareabot.api import reading_api
from mareabot.api.database import build_message


def set_task():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reading_api, 'interval', seconds=10)
    # Shut down the scheduler when exiting the app
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


def build_message(lista_previsioni):
    text = ""
    for elem in lista_previsioni:
        if elem.tipo == "min":
            text += DOWN
        else:
            text += UP
        text += " " + elem.data_estremale + " " + elem.valore + "/n"
    app.logger.debug(text)
    return text


def adding_data(input_dict):
    list_prev = []
    for data in input_dict:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        db.session.add(d)
        db.session.commit()
        list_prev.append(d)
    build_message(list_prev)
