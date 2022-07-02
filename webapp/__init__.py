from flask import Flask, render_template, request
from webapp.model import Route, Coordinate, Detail, Visual,Way
from webapp.extensions import db, migrate
from webapp.admin import RouteImageView, form, CoordinateModelView, DetailModelView, VisualModelView,WayView
from flask_admin import Admin
from webapp.weather import weather_by_city
import folium
from folium.plugins import MarkerCluster
from folium import IFrame
import base64
import json



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


    
    @app.route('/create', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            my_img = request.files['my-img']
            post = Coordinate()
            file_upload.save_files(post, files={ 'image': my_img })
            db.session.add(post)
            db.session.commit()
        posts = Coordinate.query.all()
        return render_template('create.html', **locals())

    @app.route('/media/<path:filename>')
    def media(filename):
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename,
            as_attachment=True
        )


    @app.route('/<int:pk>')
    def detail(pk):
        coordinates = Coordinate.query.filter_by(route_id=pk).all()
        start_location = next(iter(coordinates))
        if not start_location:
            raise 'NotFound'

        folium_map = folium.Map(location=[start_location.latitude, start_location.longitude],
                                zoom_start=10,
                                width=1000,
                                height=600,
                                left=200,
                                top=80)

        loc=[]
        with open('webapp/bzerp.json') as f:
            coordinate_for_json = json.load(f)
            for section, commands in coordinate_for_json.items():
                geometry=commands[0]
        spisok_coordinate=geometry['geometry']['coordinates']

        for coordanate in spisok_coordinate:
            longitude_for_route=coordanate[0]
            latitude_for_route=coordanate[1]
            loc.append((latitude_for_route, longitude_for_route))

        polyline_options= {
            'color': 'red',
            'weight': 5,
            'opacity': 0.8,
        }
        
        folium.PolyLine(loc, **polyline_options).add_to(folium_map)

        title = '<h2>Кемпинг<h2/>'
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
        detail_routes = Detail.query.filter_by(id=pk).first()
        return render_template("detail.html", maps_routes=maps_routes, detail_routes=detail_routes, thumbnail=form.thumbgen_filename, folium_map=folium_map._repr_html_())

    return app




def register_admin_views(admin):
    admin.add_view(RouteImageView(Route, db.session))
    admin.add_view(CoordinateModelView(Coordinate, db.session))
    admin.add_view(DetailModelView(Detail, db.session))
    admin.add_view(VisualModelView(Visual, db.session))
    admin.add_view(WayView(Way, db.session))


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None

