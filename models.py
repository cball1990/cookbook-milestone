from . import db
from flask_login import UserMixin

class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    email = db.column(db.String(60), unique=True)
    password = db.column(db.String(20))