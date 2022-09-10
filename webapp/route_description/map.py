from webapp.route_description.models import Coordinate, Coordinateformap
import folium
from folium import IFrame
import base64
from pathlib import Path
import os


def get_map(pk):
    coordinates = Coordinate.query.filter_by(route_id=pk).all()
    coordinates_for_rout = Coordinateformap.query.filter_by(route_id=pk).all()
    loc = [(c.latitude, c.longitude) for c in coordinates]
    try:
        folium_map = folium.Map(location=loc[0],
                                zoom_start=13,
                                width=1000,
                                height=600,
                                top=80
                                )

        polyline_options = {
            'color': 'blue',
            'weight': 5,
            'opacity': 0.8,
            }

        folium.PolyLine(loc, **polyline_options).add_to(folium_map)

        folium.Marker(
            location=loc[0],
            popup="Начало маршрута",
            icon=folium.Icon(icon='info-sign', color="red"),
            draggable=False).add_to(folium_map)

    except (IndexError):
        folium_map = folium.Map(location=[64.6863136, 97.7453061],
                                zoom_start=4,
                                width=1000,
                                height=600,
                                top=80
                                )

    base_dir = Path(__file__).resolve().parent
    for coordinate_map in coordinates_for_rout:
        image_file = coordinate_map.image_for_map
        image_path = os.path.join(base_dir, '..', 'static', 'media',
                                  image_file)
        title = f'{coordinate_map.title}'
        picture = base64.b64encode(open(image_path, 'rb').read()).decode()
        html = f'{title}<img src="data:image/JPG;base64,{picture}">'
        iframe = IFrame(html, width=632 + 20, height=420 + 20)
        popup = folium.Popup(iframe, max_width=1000)

        folium.Marker(
            location=(
                coordinate_map.longitude_for_image,
                coordinate_map.latitude_for_image
                ),
            popup=popup,
            icon=folium.Icon(icon='info-sign', color="blue"),
            draggable=False
            ).add_to(folium_map)

    return folium_map
