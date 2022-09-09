
from flask import Blueprint, render_template
from webapp.description.models import Detail
from webapp.home_page.models import Route
from webapp.description.map import get_map

blueprint = Blueprint('description', __name__)


@blueprint.route('/<int:pk>')
def detail(pk):
    maps_routes = Route.query.filter_by(id=pk).first()
    detail_routes = Detail.query.filter_by(id=pk).first()
    folium_map = get_map(pk)

    return render_template(
        "detail.html",
        maps_routes=maps_routes,
        detail_routes=detail_routes,
        folium_map=folium_map._repr_html_()
        )
