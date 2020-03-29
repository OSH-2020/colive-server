from flask_socketio import SocketIO, send

from .app import app

socketio = SocketIO(app)


@socketio.on('message')
def broadcast_handler(msg):
    send(msg, broadcast=True, include_self=False)
