from flask import Flask, render_template
from flask_admin import Admin, form
from webapp.model import db, route_liste, routImageView
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.config["FLASK_ADMIN_SWATCH"] = 'cerulean'
    app.config['SECRET_KEY'] = '123456'
    admin = Admin(app, name='map_rout', template_mode='bootstrap3')
    admin.add_view(routImageView(route_liste, db.session))
    Migrate(app, db)

    @app.route('/')
    def index():
        map_rout = route_liste.query.all()
        return render_template("index2.html", map_rout=map_rout, thumbnail=form.thumbgen_filename)

    @app.route('/<int:pk>')
    def detail(pk):
        maps_routes = route_liste.query.filter_by(id=pk).first()
        return render_template("detail.html", maps_routes=maps_routes)
    
    @app.route('/trail')
    def trail():
        return render_template("trail.html")

    return app
