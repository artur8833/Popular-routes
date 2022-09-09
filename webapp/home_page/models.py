from webapp.extensions import db
from flask_admin import form


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    video = db.Column(db.Text(), nullable=True)
    image = db.Column(db.Unicode(128), nullable=True)
    coordinates = db.relationship('Coordinate', backref='route', lazy=True)
    detail = db.relationship('Detail', backref='route', lazy=True)
    visuals = db.relationship('Visual', backref='route', lazy=True)
    coordinateformap = db.relationship('Coordinateformap', backref='route',
                                       lazy=True)

    @property
    def image_path(self):
        return f'media/{form.thumbgen_filename(self.image)}'
