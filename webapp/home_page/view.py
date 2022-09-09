from flask import Blueprint, render_template
from webapp.home_page.models import Route
from webapp.weather import weather_by_city
from flask_admin import form

blueprint = Blueprint('home_page', __name__)


@blueprint.route('/')
def index():
    map_rout = Route.query.all()
    weather = weather_by_city("Sochi, Russia")
    return render_template("index.html", map_rout=map_rout,
                           thumbnail=form.thumbgen_filename, weather=weather)
