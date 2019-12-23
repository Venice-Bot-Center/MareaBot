UP = "🔺"
DOWN = "🔻"
TIMEWATCH = "⌚"
CALENDAR = "📆"
STAR = "🌟"


class Previsione:
    def __init__(self, previsione, estremale, tipo, valore):
        self.data_previsione = previsione
        self.data_estremale = estremale
        self.date, self.time = self.data_estremale.split(" ")
        self.tipo = tipo
        self.valore = valore

    def min_max(self, hight=98) -> str:
        arrow = DOWN if self.tipo == "min" else UP
        star = STAR if int(self.valore) >= int(hight) else ""
        return f"{arrow}{self.valore}{star}"

    def hour(self):
        return TIMEWATCH + str(self.time)

    def long_string(self, hight=98):
        min_max = self.min_max(hight)
        return f"{CALENDAR}{self.date}{TIMEWATCH}{self.time}{min_max}\n"

    def __str__(self):
        return self.long_string()