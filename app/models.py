from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(140)) 
    email = db.Column(db.String(140), unique=True)
    city = db.Column(db.String(40))
    country = db.Column(db.String(40))
    state = db.Column(db.String(40))
    zip_code = db.Column(db.Integer)
    street = db.Column(db.String(140))
    number = db.Column(db.Integer)
    complement = db.Column(db.String(140))
    cpf = db.Column(db.Integer, unique=True)
    pis = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(140), nullable = False)
