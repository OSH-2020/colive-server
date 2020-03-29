from flask_socketio import SocketIO, send, ConnectionRefusedError
from flask_bcrypt import check_password_hash
from flask_login import login_user, logout_user, current_user

from .app import app
from .auth import socket_login_required, add_user, del_user
from .db import Room

socketio = SocketIO(app)


@socketio.on('login')
def login_handler(msg):
    room_id = msg['room_id']
    secret = msg['secret']

    room = Room.query.get(room_id)
    if room and check_password_hash(room.secret, secret):
        user = add_user(room_id)
        login_user(user)
    else:
        raise ConnectionRefusedError(1, 'Unauthorized.')


@socketio.on('message')
@socket_login_required
def broadcast_handler(msg):
    send(msg, broadcast=True, include_self=False)


@socketio.on('disconnect')
def disconnect_handler():
    if not current_user.is_anonymous():
        logout_user()
        del_user(current_user.id)
