from flask import Flask

from . import conf, apis, cli

app = Flask(__package__)
app.config.from_object(conf)
