# coding=utf-8
from mareabot.firebase_db import FirebaseDB

RED_CIRCLE = "🔴"
GRAY_CIRCLE = "🔘"
UP = "🔺"
DOWN = "🔻"
TIMEWATCH = "⌚"
CALENDAR = "📆"
STAR = "🌟"


class Previsione():
    def __init__(self, previsione, estremale, tipo, valore):
        self.data_previsione = previsione
        self.data_estremale = estremale
        self.date, self.time = self.data_estremale.split(" ")
        self.tipo = tipo
        self.valore = valore

    def min_max(self, hight=98):
        text = ""
        if self.tipo == "min":
            text += DOWN
        else:
            text += UP
        text += str(self.valore)
        if int(self.valore) >= int(hight):
            text += STAR
        return text

    def hour(self):
        return TIMEWATCH + str(self.time)

    def calendar(self):
        return CALENDAR + str(self.date)

    def long_string(self, hight=98):
        return self.calendar() + self.hour() + self.min_max(hight) + "\n"

    def __str__(self):
        return self.long_string()


class DBIstance:
    def __init__(self):
        self.firebase_istance = FirebaseDB().db
        self.prevision = []
        self.maximum = -400

    @property
    def maximum(self):
        return self.maximum.get()

    @maximum.getter
    def maximum(self):
        return self.firebase_istance.child("maximum").child("last").get().val()

    @maximum.setter
    def maximum(self, last):
        self.firebase_istance.child("maximum").set({"last": str(last)})

    @property
    def last(self):
        return self.last.get()

    @last.getter
    def last(self):
        return self.firebase_istance.child("prevision").child("last").get().val()

    @last.setter
    def last(self, last):
        self.firebase_istance.child("prevision").set({"last": str(last)})

    @property
    def message(self):
        return self.message.get()

    @message.getter
    def message(self):
        return self.firebase_istance.child("message").child("last").get().val()

    @message.setter
    def message(self, message):
        self.firebase_istance.child("message").set({"last": str(message)})

    @property
    def message_hight(self):
        return self.message_hight.get()

    @message_hight.getter
    def message_hight(self):
        return self.firebase_istance.child("message_hight").child("last").get().val()

    @message_hight.setter
    def message_hight(self, message_hight):
        self.firebase_istance.child("message_hight").set({"last": str(message_hight)})

    @property
    def instante(self):
        return self.instante.get()

    @instante.getter
    def instante(self):
        return self.firebase_istance.child("instante").child("last").get().val()

    @instante.setter
    def instante(self, instante):
        self.firebase_istance.child("instante").set({"last": str(instante)})
