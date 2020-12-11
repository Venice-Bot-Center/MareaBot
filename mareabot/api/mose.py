from typing import Tuple
import requests
from statistics import mean
from loguru import logger

API_URL_MOSE = (
    "https://dati.venezia.it/sites/default/files/dataset/opendata/livello.json"
)

STAZIONI_LAGUNA = [
    "01025",
    "01030",
    "01033",
    "01036",
    "01037",
    "01028",
    "01032",
    "01045",
    "01029",
]
STAZIONI_MARE = ["01023", "01024", "01022", "01021"]


def get_api_mose() -> Tuple[float, float]:
    r = requests.get(API_URL_MOSE)

    st_lag = []
    st_mare = []
    for stazione in r.json():
        if stazione["ID_stazione"] in STAZIONI_LAGUNA:
            st_lag.append(float(stazione["valore"].split(" ")[0]))
        else:
            st_mare.append(float(stazione["valore"].split(" ")[0]))
    lag = mean(st_lag)
    mare = mean(st_mare)
    logger.info(f"La media lagunare é di {lag} e quella di mare é {mare}")
    return lag, mare


def is_mose_up() -> bool:
    lag, mare = get_api_mose()
    return abs(lag - mare) > 0.1
