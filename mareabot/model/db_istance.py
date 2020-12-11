from mareabot.api.mose import is_mose_up
import requests
import os
import pyrebase
from mareabot.model import Previsione
from mareabot.social import telegram_api

MAREA_ISTANTANEA_API = "https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Punta_Salute.html"

VENTO_ISTANTANEO_API = "https://www.comune.venezia.it/sites/default/files/publicCPSM2/stazioni/temporeale/Diga_Sud_Lido.html"
API_KEY = os.environ["FBKEY"]
AUTHDOMAIN = os.environ["FBAUTH"]
DATABASEURL = os.environ["FBDATABASE"]
STORAGEBUCKET = os.environ["FBSTORAGE"]


class FirebaseDB:
    config = {
        "apiKey": API_KEY,
        "authDomain": AUTHDOMAIN,
        "databaseURL": DATABASEURL,
        "storageBucket": STORAGEBUCKET,
    }

    db = pyrebase.initialize_app(config).database()


class DBIstance:
    def __init__(self):
        self.firebase_istance = FirebaseDB().db
        self.prevision = []
        self.actv_h = 0

    @property
    def actv_h(self):
        return self.actv_h.get()

    @actv_h.getter
    def actv_h(self):
        return self.firebase_istance.child("actv").child("hight").get().val()

    @actv_h.setter
    def actv_h(self, last):
        self.firebase_istance.child("actv").update({"hight": str(last)})

    @property
    def actv_mex(self):
        return self.actv_mex.get()

    @actv_mex.getter
    def actv_mex(self):
        return self.firebase_istance.child("actv").child("mex").get().val()

    @actv_mex.setter
    def actv_mex(self, last):
        self.firebase_istance.child("actv").update({"mex": str(last)})

    @property
    def actv_number(self):
        return self.actv_mex.get()

    @actv_number.getter
    def actv_number(self):
        return self.firebase_istance.child("actv").child("number").get().val()

    @actv_number.setter
    def actv_number(self, last):
        self.firebase_istance.child("actv").update({"number": str(last)})

    @property
    def last(self):
        return self.last.get()

    @last.getter
    def last(self):
        return self.firebase_istance.child("prevision").child("last").get().val()

    @last.setter
    def last(self, last):
        self.firebase_istance.child("prevision").update({"last": str(last)})

    @property
    def lastest(self):
        return self.lastest.get()

    @lastest.getter
    def lastest(self):
        return self.firebase_istance.child("prevision").child("lastest").get().val()

    @lastest.setter
    def lastest(self, last):
        self.firebase_istance.child("prevision").update({"lastest": str(last)})

    @property
    def message(self):
        return self.message.get()

    @message.getter
    def message(self):
        return self.firebase_istance.child("message").child("id").get().val()

    @message.setter
    def message(self, message):
        self.firebase_istance.child("message").update({"id": str(message)})

    @property
    def message_hight(self):
        return self.message_hight.get()

    @message_hight.getter
    def message_hight(self):
        return self.firebase_istance.child("message").child("hight").get().val()

    @message_hight.setter
    def message_hight(self, message_hight):
        self.firebase_istance.child("message").update({"hight": str(message_hight)})

    @property
    def message_mose(self):
        return self.message_mose.get()

    @message_mose.getter
    def message_mose(self):
        mose = self.firebase_istance.child("mose").child("message_mose").get().val()
        if mose is None:
            return 0
        return mose

    @message_mose.setter
    def message_mose(self, message_mose):
        self.firebase_istance.child("mose").update({"message_mose": str(message_mose)})

    @property
    def instante(self):
        return self.instante.get()

    @instante.getter
    def instante(self):
        return self.firebase_istance.child("prevision").child("hight").get().val()

    @instante.setter
    def instante(self, instante):
        self.firebase_istance.child("prevision").update({"hight": instante})

    def adding_data(self, input_dict: dict):
        maximum = -400
        self.lastest = self.last
        for data in input_dict:
            d = Previsione(
                data["DATA_PREVISIONE"],
                data["DATA_ESTREMALE"],
                data["TIPO_ESTREMALE"],
                data["VALORE"],
            )
            maximum = max(int(maximum), int(data["VALORE"]))
            self.prevision.append(d)
            self.last = input_dict[0]["DATA_PREVISIONE"]
        return maximum

    def posting_previsione(self, maximum: int, hight: int = 94):
        if self.lastest == self.last:
            return
        if self.message is not None:
            telegram_api.telegram_channel_delete_message(self.message)
        if int(maximum) >= hight:
            estended = ""
            for s in self.prevision:
                estended += s.long_string(hight)
            message, flag = telegram_api.telegram_channel_send(estended)
            if flag:
                self.message = message

    def posting_actv(self):
        from mareabot.api import get_istantanea_marea, get_actv

        hight = get_istantanea_marea(requests.get(MAREA_ISTANTANEA_API).text)
        actv_data, numb = get_actv(hight)

        try:
            if int(numb) == int(self.actv_number):
                return
        except Exception:
            pass
        if self.actv_mex is not None:
            telegram_api.telegram_channel_delete_message(self.actv_mex)
        self.actv_h = hight

        if actv_data:
            message, flag = telegram_api.telegram_channel_send(actv_data)
            if flag:
                self.actv_mex = message
        self.actv_number = numb

    def posting_instant(self, maximum: int = 110):
        from mareabot.api import get_istantanea_marea
        from mareabot.api import get_vento

        hight = get_istantanea_marea(requests.get(MAREA_ISTANTANEA_API).text)
        vento, vento_max = get_vento(requests.get(VENTO_ISTANTANEO_API).text)
        last_hight_db = 0 if self.instante is None else self.instante

        if int(hight) == int(last_hight_db):
            return

        self.instante = hight

        if self.message_hight is not None:
            telegram_api.telegram_channel_delete_message(self.message_hight)

        if int(maximum) <= int(hight):
            estended = f"Ultima misurazione è cm {hight}\nIl vento è {vento:.2f} km/h e al massimo il vento è {vento_max:.2f} km/h"
            message, flag = telegram_api.telegram_channel_send(estended)
            if flag:
                self.message_hight = message

    def posting_mose(self):
        if is_mose_up():
            if self.message_mose == 0:
                message, _ = telegram_api.telegram_channel_send(
                    "⛑️ Il mose é attualmente in funzione ⛑️"
                )
                self.message_mose = message
        else:
            if self.message_mose != 0:
                telegram_api.telegram_channel_delete_message(self.message_mose)
                self.message_mose = 0
