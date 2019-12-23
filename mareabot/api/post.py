import json

import requests

from mareabot.model import DBIstance

MAREA_API_URL = (
    "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"
)


def posting():
    datas = json.loads(requests.get(MAREA_API_URL).text)
    db_istance = DBIstance()
    maximum = db_istance.adding_data(datas)
    db_istance.posting_actv()
    db_istance.posting_previsione(maximum=maximum)
    db_istance.posting_instant()
