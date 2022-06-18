from flask import Flask, render_template
from webapp.model import Route
from webapp.extensions import db, migrate
from webapp.admin import RouteImageView, form
from flask_admin import Admin
from webapp.weather import weather_by_city
import folium
import os


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config["FLASK_ADMIN_SWATCH"] = 'cerulean'
    app.config['SECRET_KEY'] = '123456'
    register_extensions(app)

    admin = Admin(app, name='map_rout', template_mode='bootstrap3')
    register_admin_views(admin)

    @app.route('/')
    def index():
        map_rout = Route.query.all()
        weather = weather_by_city("Sochi, Russia")
        return render_template("index2.html", map_rout=map_rout, thumbnail=form.thumbgen_filename, weather=weather)

    @app.route('/<int:pk>')
    def detail(pk):
        maps_routes = Route.query.filter_by(id=pk).first()
        return render_template("detail.html", maps_routes=maps_routes)

    @app.route('/detailmap_ag')
    def detailmap_ag():
        folium_map = folium.Map(location=[43.6798, 40.2814], zoom_start=17)
        walkData = os.path.join('walk.json')
        folium.GeoJson(walkData, name='walk').add_to(folium_map)
        folium_map.save('templates/map.html')
        return render_template("detail.html")

    @app.route('/map')
    def map():
        return render_template('map.html')

    return app


def register_admin_views(admin):
    admin.add_view(RouteImageView(Route, db.session))


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
