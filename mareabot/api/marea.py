import requests
from bs4 import BeautifulSoup
from loguru import logger

MAREA_ISTANTANEA_API = "https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Punta_Salute.html"


def get_istantanea_marea() -> int:
    html_data = requests.get(MAREA_ISTANTANEA_API).text
    bs = BeautifulSoup(html_data, "html.parser")

    liv_last = None
    level = 0
    for row in bs.findAll("tr"):
        aux = row.findAll("td")
        if len(aux) == 4:
            gg, ora, liv, th2o = aux
            if liv.text != "":
                liv_last = liv
            else:
                level = int(float(liv_last.text) * 100)
    logger.info(f"La marea istantanea é di {level}")
    return level


def get_percentuale_allagamento(liv=None) -> int:
    if liv is None:
        liv = get_istantanea_marea()
    perc = 0
    if 90 < liv <= 100:
        perc = 2
    elif 100 < liv <= 110:
        perc = 5
    elif 110 < liv <= 120:
        perc = 12
    elif 120 < liv <= 130:
        perc = 28

    elif 130 < liv <= 140:
        perc = 46

    elif 140 < liv <= 150:
        perc = 59

    elif 150 < liv <= 160:
        perc = 70

    elif 160 < liv <= 170:
        perc = 77

    elif 170 < liv <= 180:
        perc = 82

    elif 180 < liv <= 190:
        perc = 85

    elif 190 < liv <= 200:
        perc = 88

    elif 200 < liv:
        perc = 91
    logger.info(f"La percentuale di allagamento é di {perc}%")
    return perc
