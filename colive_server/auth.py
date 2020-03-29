import functools

from flask_login import LoginManager, current_user

from .app import app

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: str):
    pass


def socket_login_required(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if current_user.is_authenticated:
            return f(*args, **kwargs)
        else:
            raise ConnectionRefusedError(1, 'Unauthorized.')
    return wrapped
