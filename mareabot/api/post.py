import requests
from loguru import logger
from mareabot.model import DBIstance

MAREA_API_URL = (
    "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"
)


def posting():
    r = requests.get(MAREA_API_URL)
    if 200 <= r.status_code < 400:
        datas = r.json()
        db_istance = DBIstance()
        maximum = db_istance.adding_data(datas)
        db_istance.posting_actv()
        db_istance.posting_previsione(maximum=maximum)
        db_istance.posting_instant()
        db_istance.posting_mose()
    else:
        logger.error(f"The marea api return {r.status_code}")
