from flask import Flask


class AppConfig:
    SECRET_KEY: str = 'dev'
    DB_URI: str = 'sqlite:////tmp/colive.sqlite3'
    SQLALCHEMY_DATABASE_URI = DB_URI
    REDIS_URI: str = 'redis://user:password@localhost:6379'

    def check(self):
        pass


def configure_app(app: Flask):
    config = AppConfig()
    config.check()
    app.config.from_object(config)


app = Flask(__package__)
configure_app(app)
