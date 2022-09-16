
from flask import Blueprint, render_template
from webapp.route_description.models import DescriptionRoute
from webapp.home_page.models import Route
from webapp.route_description.map import get_map

blueprint = Blueprint('description', __name__)


@blueprint.route('/<int:pk>')
def detail(pk):
    home_page = Route.query.filter_by(id=pk).first()
    description_routes = DescriptionRoute.query.filter_by(id=pk).first()
    folium_map = get_map(pk)

    return render_template(
        "detail.html",
        home_page=home_page,
        description_routes=description_routes,
        folium_map=folium_map._repr_html_()
        )
