from webapp.extensions import db
from flask_admin import form


class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    order = db.Column(db.Integer, nullable=False)


class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    description_start = db.Column(db.Text(), nullable=False)
    description_basic = db.Column(db.Text(), nullable=False)
    routestart = db.Column(db.Text(), nullable=False)
    workingmode = db.Column(db.Text(), nullable=False)
    order = db.Column(db.Integer, nullable=False)


class Visual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Unicode(128), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)

    @property
    def image_path(self):
        return f'media/{self.image}'

    @property
    def thumbnail_path(self):
        return f'media/{form.thumbgen_filename(self.image)}'


class Coordinateformap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    longitude_for_image = db.Column(db.Float, nullable=False)
    latitude_for_image = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(80), nullable=True)
    image_for_map = db.Column(db.Unicode(128), nullable=False)
    order = db.Column(db.Integer, nullable=False)
