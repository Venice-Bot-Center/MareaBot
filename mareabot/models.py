from mareabot import db


class Previsione(db.Model):
    __tablename__ = "previsione"
    id = db.Column(db.Integer, primary_key=True)
    data_previsione = db.Column(db.String(30))
    data_estremale = db.Column(db.String(30))
    tipo = db.Column(db.String(3))
    valore = db.Column(db.Integer(4))

