import json

import requests
from sqlalchemy.exc import OperationalError

from mareabot import app
from mareabot.api.database import db
from mareabot.api.models import Previsione, adding_data

MAREA_API_URL = "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"


def reading_api():
    datas = json.loads(requests.get(MAREA_API_URL).text)
    app.logger.error("Start reading json")

    try:
        test = Previsione.query.filter_by(data_previsione=datas[0]["DATA_PREVISIONE"]).first()
        if test is None:
            adding_data(datas)
        else:
            app.logger.warn(test)
            app.logger.warn("Not update dates")
    except OperationalError:
        db.create_all()
        adding_data(datas)
