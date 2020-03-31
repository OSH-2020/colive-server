from flask_admin import Admin, AdminIndexView as IndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_bcrypt import generate_password_hash

from .app import app
from .db import Room, db


class AdminMixin:
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class AdminIndexView(AdminMixin, IndexView):
    pass


admin = Admin(app, template_mode='bootstrap3', index_view=AdminIndexView())


class AdminModelView(AdminMixin, ModelView):
    def is_accessible(self):
        # return current_user.is_authenticated and current_user.is_admin
        return True


class AdminRoomView(AdminModelView):
    def create_model(self, form):
        model: Room = super().create_model(form)
        model.secret = generate_password_hash(model.secret)
        db.session.commit()
        return model


admin.add_view(AdminRoomView(Room, db.session))
