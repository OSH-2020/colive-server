from flask import Flask


class AppConfig:
    DEBUG: bool = True
    SECRET_KEY: str = 'dev'

    DB_URI: str = 'sqlite:////tmp/colive.sqlite3'
    CREATE_TABLES: bool = True
    DROP_TABLES_BEFORE = DEBUG
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_URI: str = 'redis://user:password@localhost:6379'

    def check(self):
        pass


def configure_app(app: Flask):
    config = AppConfig()
    config.check()
    app.config.from_object(config)


app = Flask(__package__)
configure_app(app)
