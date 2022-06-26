from http.client import NOT_FOUND
from xml.dom import NotFoundErr
from click import style
from flask import Flask, render_template
from webapp.model import Route, Coordinate
from webapp.extensions import db, migrate
from webapp.admin import RouteImageView, form, CoordinateModelView
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
        start_location=next(iter(coordinates))
        if not start_location:
            raise NOT_FOUND
        
        folium_map=folium.Map(location=[start_location.latitude, start_location.longitude],
        zoom_start=10,
        width=1000,
        height=600,
        left=200,
        top=80) 


        tooltip_for_picture = 'Палаточная остановка'
        html_for_picture = '<img src="data:image/png;base64,{}">'.format
        
        
        #picture = base64.b64decode(open('./webapp/static/palatka/ko.png','rb').read()).decode()
        #iframe_for_picture = IFrame(html_for_picture(picture),width=600+20,height=400+20)
        #popup_for_picture = folium.Popup(iframe_for_picture, max_width=650)
        #icon_for_picture = folium.Icon(color='red', icon="glyphicon-home")
        #marker_for_picture=folium.Marker(location=[40.3554, 43.6949], popup=popup_for_picture, tooltip=tooltip_for_picture, icon=icon_for_picture).add_to(folium_map)

        folium.Marker(location=[start_location.latitude, start_location.longitude],
        popup="Начало маршрута",
        icon=folium.Icon(icon='info-sign', color="red"),
        draggable=False).add_to(folium_map)


        maps_routes = Route.query.filter_by(id=pk).first()
        return render_template("detail.html", maps_routes=maps_routes,folium_map=folium_map._repr_html_())

    return app


def register_admin_views(admin):
    admin.add_view(RouteImageView(Route, db.session))
    admin.add_view(CoordinateModelView(Coordinate, db.session))


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
