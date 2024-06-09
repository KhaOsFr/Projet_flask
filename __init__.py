from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a4c5f2c33a67ad735f86eb85ae096c6f'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://anonyme:anonyme@localhost/Projet'

db = SQLAlchemy(app)

from . import routes