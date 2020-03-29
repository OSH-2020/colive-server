from flask_sqlalchemy import SQLAlchemy

from .app import app

db = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String(60), nullable=False)
