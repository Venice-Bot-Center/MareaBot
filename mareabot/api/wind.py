from bs4 import BeautifulSoup


def get_vento(html_data: str) -> (float, float):
    bs = BeautifulSoup(html_data, "html.parser")

    vv_last = vvmax_last = None
    for row in bs.findAll("tr"):
        aux = row.findAll("td")
        if len(aux) == 6:
            gg, ora, liv, vv, vv_max, dv = aux
            if vv.text != "":
                vv_last = vv
                vvmax_last = vv_max
            else:
                return float(vv_last.text) * 3.6, float(vvmax_last.text) * 3.6
    return 0.0, 0.0