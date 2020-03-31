from flask.cli import AppGroup

from .app import app
from .db import db

db_cli = AppGroup('db')


@db_cli.command('drop-tables')
def cmd_drop_tables():
    db.drop_all()


@db_cli.command('create-tables')
def cmd_create_tables():
    db.create_all()


app.cli.add_command(db_cli)
