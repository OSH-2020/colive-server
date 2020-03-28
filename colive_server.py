from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

socketio = SocketIO(app)


@socketio.on('message')
def broadcast(msg):
    send(msg, broadcast=True, include_self=False)


if __name__ == '__main__':
    socketio.run(app)
