from flask_socketio import SocketIO, emit, ConnectionRefusedError, join_room, leave_room
from flask_bcrypt import check_password_hash
from flask_login import login_user, logout_user, current_user

from . import app
from .db import db, Room, User

socketio = SocketIO(app)


@socketio.on('login')
def login_handler(msg):
    room_id = msg['room_id']
    password = str(msg['password'])
    addr = str(msg['addr'])
    if not validate_room_id(room_id):
        raise ConnectionRefusedError(1, 'Unauthorized')

    room = Room.query.get(room_id)
    if room and check_password_hash(room.password, password):
        user = User(addr=addr, room=room)
        login_user(user)
        join_room(room_id)
        emit('login', {
            'user_id': current_user.id,
            'addr_set': [u.addr for u in room.users if u.id != user.id],
        }, broadcast=False)
    else:
        raise ConnectionRefusedError(1, 'Unauthorized')


def validate_room_id(room_id: int) -> bool:
    if isinstance(room_id, int):
        return True
    else:
        return False


@socketio.on('disconnect')
def disconnect_handler():
    if not current_user.is_anonymous:
        info = {'user_id': int(current_user.id)}
        leave_room(current_user.room_id)
        logout_user()
        db.session.delete(current_user)
        db.session.commit()
        emit('logout', info, broadcast=True, include_self=False)
