from bs4 import BeautifulSoup


def get_istantanea_marea(html_data: str) -> int:
    bs = BeautifulSoup(html_data, "html.parser")

    liv_last = None
    for row in bs.findAll("tr"):
        aux = row.findAll("td")
        if len(aux) == 4:
            gg, ora, liv, th2o = aux
            if liv.text != "":
                liv_last = liv
            else:
                return int(float(liv_last.text) * 100)
    return 0
