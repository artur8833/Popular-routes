from http.client import NOT_FOUND
from xml.dom import NotFoundErr
from click import style
from flask import Flask, render_template
from webapp.model import Route, Coordinate, Detail, Visual
from webapp.extensions import db, migrate
from webapp.admin import RouteImageView, form, CoordinateModelView, DetailModelView, VisualModelView
from flask_admin import Admin
from webapp.weather import weather_by_city
import folium
from folium.plugins import MarkerCluster
from folium import IFrame
import os
import base64


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
        map_rout = Route.query.all()
        weather = weather_by_city("Sochi, Russia")
        return render_template("index.html", map_rout=map_rout, thumbnail=form.thumbgen_filename, weather=weather)

    @app.route('/<int:pk>')
    def detail(pk):
        coordinates = Coordinate.query.filter_by(route_id=pk).all()
        start_location = next(iter(coordinates))
        if not start_location:
            raise NOT_FOUND

        folium_map = folium.Map(location=[start_location.latitude, start_location.longitude],
                                zoom_start=10,
                                width=1000,
                                height=600,
                                left=200,
                                top=80)

        title = '<h2>Начало маршрута<h2/>'
        picture = base64.b64encode(open('./webapp/static/palatka/ko.png', 'rb').read()).decode()
        html = f'{title}<img src="data:image/JPG;base64,{picture}">'
        iframe = IFrame(html, width=632 + 20, height=420 + 20)
        popup = folium.Popup(iframe, max_width=1000)

        folium.Marker(
            location=[43.6949, 40.3554],
            popup=popup,
            icon=folium.Icon(icon='glyphicon-home', color="red"),
            draggable=False).add_to(folium_map)

        folium.Marker(location=[start_location.latitude, start_location.longitude],
                      popup="Начало маршрута",
                      icon=folium.Icon(icon='info-sign', color="red"),
                      draggable=False).add_to(folium_map)

        maps_routes = Route.query.filter_by(id=pk).first()
        return render_template("detail.html", maps_routes=maps_routes, folium_map=folium_map._repr_html_())

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
