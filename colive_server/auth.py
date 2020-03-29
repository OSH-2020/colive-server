import uuid
import json
import functools

from flask_login import LoginManager, current_user, UserMixin

from .app import app
from .kv_db import kv_db

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, user_id: str, room_id: int):
        self.id = user_id
        self.room_id = room_id

    def __str__(self):
        return json.dumps({
            'id': self.id,
            'room_id': self.room_id,
        })

    @classmethod
    def from_str(cls, obj_str: str):
        return cls(**json.loads(obj_str))


@login_manager.user_loader
def load_user(user_id: str):
    user_str = kv_db.get(user_id)
    return None if user_str is None else User.from_str(user_str)


def add_user(room_id: int):
    user = User(str(uuid.uuid4()), room_id)
    kv_db.set(user.id, str(user))
    return user


def del_user(user_id: str):
    kv_db.delete(user_id)


def socket_login_required(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if current_user.is_authenticated:
            return f(*args, **kwargs)
        else:
            raise ConnectionRefusedError(1, 'Unauthorized.')
    return wrapped
