from flask import Blueprint, render_template
from webapp.home_page.models import Route
from webapp.weather import weather_by_city
from flask_admin import form

blueprint = Blueprint('home_page', __name__)


@blueprint.route('/')
def index():
    home_page = Route.query.all()
    weather = weather_by_city("Sochi, Russia")
    return render_template(
        "index.html",
        home_page=home_page,
        thumbnail=form.thumbgen_filename,
        weather=weather
        )
