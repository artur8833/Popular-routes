from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from webapp.extensions import db, migrate
from webapp.user.model import User
from webapp.user.views import blueprint as user_blueprint
from webapp.admin import (RouteImageView, CoordinateModelView, DetailModelView,
                          VisualModelView, CoordinateformapModelView)
from webapp.head.view import blueprint as head_blueprint
from webapp.load.view import blueprint as load_blueprint
from webapp.description.view import blueprint as description_blueprint
from webapp.head.models import Route
from webapp.description.models import (Coordinate, Detail, Coordinateformap,
                                       Visual)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config["FLASK_ADMIN_SWATCH"] = 'cerulean'
    app.config['SECRET_KEY'] = '123456'
    app.register_blueprint(user_blueprint)
    register_extensions(app)
    admin = Admin(app, name='map_rout', template_mode='bootstrap4')
    register_admin_views(admin)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(head_blueprint)
    app.register_blueprint(load_blueprint)
    app.register_blueprint(description_blueprint)

    return app


def register_admin_views(admin):
    admin.add_view(RouteImageView(Route, db.session))
    admin.add_view(CoordinateModelView(Coordinate, db.session))
    admin.add_view(DetailModelView(Detail, db.session))
    admin.add_view(VisualModelView(Visual, db.session))
    admin.add_view(CoordinateformapModelView(Coordinateformap, db.session))


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
