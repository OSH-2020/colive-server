from flask_socketio.test_client import SocketIOTestClient

from colive_server.app import app
from colive_server.apis import socketio
from colive_server.db import Room

client = SocketIOTestClient(app, socketio)


def test_login(room: Room):
    client.connect()
    client.emit('login', {
        'room_id': room.id,
        'secret': 'test',
    })
    client.send({'test': 'test'})
    client.send({'test': 'test'})
    assert client.is_connected() is True
