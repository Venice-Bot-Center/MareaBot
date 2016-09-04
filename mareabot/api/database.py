# coding=utf-8

from flask.ext.sqlalchemy import SQLAlchemy

from mareabot import app
from mareabot.config import DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
db = SQLAlchemy(app)

from mareabot.api.character import DOWN, UP
from mareabot.api.models import Previsione



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


def adding_data(datas):
    lista_previsioni = []
    for data in datas:
        d = Previsione(data["DATA_PREVISIONE"], data["DATA_ESTREMALE"], data["TIPO_ESTREMALE"], data["VALORE"])
        db.session.add(d)
        db.session.commit()
        lista_previsioni.append(d)
    build_message(lista_previsioni)
