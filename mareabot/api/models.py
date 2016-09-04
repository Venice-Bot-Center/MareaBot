from mareabot.api.database import db


class Previsione(db.Model):
    __tablename__ = "previsione"
    id = db.Column(db.Integer, primary_key=True)
    data_previsione = db.Column(db.String(30))
    data_estremale = db.Column(db.String(30))
    tipo = db.Column(db.String(3))
    valore = db.Column(db.String(4))

    def __init__(self, previsione, estremale, tipo, valore):
        self.data_previsione = previsione
        self.data_estremale = estremale
        self.tipo = tipo
        self.valore = valore
