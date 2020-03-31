from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash

from .app import app

db = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String(60), nullable=False)

    def __init__(self, room_id: int, secret: str):
        super().__init__()
        self.id = room_id
        self.secret = generate_password_hash(secret)

    def __unicode__(self):
        return str(self.id)
