from flask import Flask, render_template
from webapp.model import Route
from webapp.extensions import db, migrate
from webapp.admin import RouteImageView
from flask_admin import Admin


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config["FLASK_ADMIN_SWATCH"] = 'cerulean'
    app.config['SECRET_KEY'] = '123456'
    register_extensions(app)

    admin = Admin(app, name='map_rout', template_mode='bootstrap4')
    register_admin_views(admin)

    @app.route('/')
    def index():
        map_route = Route.query.all()
        return render_template("index2.html", map_route=map_route)

    @app.route('/<int:pk>')
    def detail(pk):
        maps_routes = Route.query.filter_by(id=pk).first()
        return render_template("detail.html", maps_routes=maps_routes)
    
    @app.route('/trail')
    def trail():
        return render_template("trail.html")

    return app


def register_admin_views(admin):
    admin.add_view(RouteImageView(Route, db.session))


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
