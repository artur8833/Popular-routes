from flask import Flask, render_template
from flask_admin import Admin
from flask_login import LoginManager
from webapp.admin import RouteImageView, form, CoordinateModelView, DetailModelView, VisualModelView
from webapp.extensions import db, migrate
from webapp.model import Route, Coordinate, Detail, Visual
from webapp.user.model import User
from webapp.user.views import blueprint as user_blueprint
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config["FLASK_ADMIN_SWATCH"] = 'cerulean'
    app.config['SECRET_KEY'] = '123456'
    register_extensions(app)
    admin = Admin(app, name='map_rout', template_mode='bootstrap3')
    register_admin_views(admin)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        map_rout = Route.query.all()
        weather = weather_by_city("Sochi, Russia")
        return render_template("index.html", map_rout=map_rout, thumbnail=form.thumbgen_filename, weather=weather)

    @app.route('/<int:pk>')
    def detail(pk):
        maps_routes = Route.query.filter_by(id=pk).first()
        detail_routes = Detail.query.filter_by(id=pk).first()
        return render_template("detail.html", maps_routes=maps_routes, detail_routes=detail_routes)

    return app


def register_admin_views(admin):
    admin.add_view(RouteImageView(Route, db.session))
    admin.add_view(CoordinateModelView(Coordinate, db.session))
    admin.add_view(DetailModelView(Detail, db.session))
    admin.add_view(VisualModelView(Visual, db.session))


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None

