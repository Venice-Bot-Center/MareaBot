import json

import requests

from mareabot.config import c
from mareabot.model import PREV

MAREA_API_URL = "http://dati.venezia.it/sites/default/files/dataset/opendata/previsione.json"

from mareabot.task import adding_data
def reading_api():
    datas = json.loads(requests.get(MAREA_API_URL).text)
    if not PREV.previsions:
        adding_data(datas)
    else:
        if PREV.last != datas[0]["DATA_PREVISIONE"]:
            adding_data(datas)



