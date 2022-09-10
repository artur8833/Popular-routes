from flask import Blueprint, request, flash, redirect, url_for
from webapp.route_description.models import Coordinate
from webapp.home_page.models import Route
from webapp.extensions import db
import json


blueprint = Blueprint('load', __name__)


@blueprint.route('/load/<int:pk>', methods=['GET', 'POST'])
def upload_file(pk):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        try:
            if file:
                read_file = file.read().decode('utf-8')
                coordinate_for_file = json.loads(read_file)
                route = next(iter(coordinate_for_file.get("features", [])),
                             None)
                route_coordinates = route.get('geometry', {}).get('coordinates',[])
                route = Route.query.filter_by(id=pk).first()

                for position, coordinates in enumerate(route_coordinates):
                    coordinates = Coordinate(
                        latitude=coordinates[1],
                        longitude=coordinates[0],
                        route_id=route.id,
                        order=position)
                    db.session.add(coordinates)
                db.session.commit()
        except(AttributeError):
            return 'Маршрут не найден'
    flash('маршрут добавлен')
    return redirect(url_for('home_page.index'))
