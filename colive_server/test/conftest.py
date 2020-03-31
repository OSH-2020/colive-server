from pytest import fixture

from colive_server.db import db, Room


@fixture(scope='session')
def room():
    room = Room(1, 'test')
    db.session.add(room)
    db.session.commit()
    return room
