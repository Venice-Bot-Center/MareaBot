from bs4 import BeautifulSoup
from loguru import logger


def get_vento(html_data: str) -> (float, float):
    try:
        bs = BeautifulSoup(html_data, "html.parser")

        vv_last = vvmax_last = None
        for row in bs.findAll("tr"):
            aux = row.findAll("td")
            if len(aux) == 6:
                gg, ora, liv, vv, vv_max, dv = aux
                if liv.text != "":
                    if vv.text == "":
                        vv_last = "0.0"
                    else:
                        vv_last = vv.text
                    if vv_max.text == "":
                        vvmax_last = "0.0"
                    else:
                        vvmax_last = vv_max.text
                else:

                    return float(vv_last) * 3.6, float(vvmax_last) * 3.6
        return 0.0, 0.0
    except ValueError as e:
        logger.error(e)
        return 0.0, 0.0
