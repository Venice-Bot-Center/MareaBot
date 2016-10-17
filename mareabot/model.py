from mareabot.character import DOWN, TIMEWATCH, UP, CALENDAR
from mareabot.config import c


class Previsione():
    def __init__(self, previsione, estremale, tipo, valore):
        self.data_previsione = previsione
        self.data_estremale = estremale
        self.tipo = tipo
        self.valore = valore

    def short_string(self):
        date, time = self.data_estremale.split(" ")
        date = date.split("-")[2]
        t = time.split(":")
        time = t[0] + ":" + t[1]

        if len(self.valore) == 1:
            self.valore = "0" + self.valore

        text = ""
        if self.tipo == "min":
            text += DOWN
        else:
            text += UP
        text += str(self.valore)
        text += TIMEWATCH
        text += str(time)
        text += CALENDAR + str(date) + "\n"
        return text

    def long_string(self):
        date, time = self.data_estremale.split(" ")

        text = ""
        if int(self.valore) > 94:
            if self.tipo == "min":
                text += DOWN
            else:
                text += UP
            text += str(self.valore) + " " + TIMEWATCH + str(time) + " " + CALENDAR + str(date) + "\n"
        return text


class MemoPrev(object):
    def __init__(self):
        self.last = c.get_latest()
        self.previsions = []

    @property
    def last(self):
        return self.last

    @last.getter
    def last(self):
        return c.get_latest()

    @last.setter
    def last(self, last):
        c.set_latest(last)
