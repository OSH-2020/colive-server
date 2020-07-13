from . import app, conf

if __name__ == '__main__':
    app.run(port=conf.PORT)
