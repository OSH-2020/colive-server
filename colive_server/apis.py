from flask_socketio import SocketIO, send, emit, ConnectionRefusedError, join_room, leave_room
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
    if not validate_room_id(room_id):
        raise ConnectionRefusedError(1, 'Unauthorized.')

    room = Room.query.get(room_id)
    if room and check_password_hash(room.secret, secret):
        user = add_user(room_id)
        login_user(user)
        join_room(room_id)
        emit('login', {'user_id': current_user.id}, broadcast=False)
    else:
        raise ConnectionRefusedError(1, 'Unauthorized.')


def validate_room_id(room_id: int) -> bool:
    if isinstance(room_id, int):
        return True
    else:
        return False


@socketio.on('message')
@socket_login_required
def broadcast_handler(msg):
    send(msg, broadcast=True, include_self=False, room=current_user.room_id)


@socketio.on('disconnect')
def disconnect_handler():
    if not current_user.is_anonymous:
        info = {'user_id': int(current_user.id)}
        leave_room(current_user.room_id)
        logout_user()
        del_user(current_user.id)
        emit('logout', info, broadcast=True, include_self=False)
