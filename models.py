from . import app, db
from flask_sqlalchemy import SQLAlchemy


class vue_event_disc_pays(db.Model):
    id_event = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_debut = db.Column(db.Date, nullable=False)
    date_fin = db.Column(db.Date, nullable=False)
    discipline = db.Column(db.String(20), nullable=False)
    pays = db.Column(db.String(20), nullable=False)
    img_p = db.Column(db.String(20), nullable=False, default='default.jpg')
    img_e = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f'{self.id_event} : {self.nom} : {self.description} : {self.date_debut} : {self.date_fin} : {self.discipline} : {self.pays} : {self.img_p} : {self.img_e}'


class vue_sportif_disc_pays(db.Model):
    id_sportif = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pays = db.Column(db.String(30), nullable=False)
    img_p = db.Column(db.String(30), nullable=False)
    discipline = db.Column(db.String(30), nullable=False)
    img_s = db.Column(db.String(30), nullable=False)
    id_event = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id_sportif} : {self.nom} : {self.prenom} : {self.age} : {self.pays} : {self.img_p} : {self.discipline} : {self.img_s} : {self.id_event}'
