from webapp.admin import  form
from webapp.extensions import db
from flask_admin import form


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    image = db.Column(db.Unicode(128), nullable=True)
    coordinates = db.relationship('Coordinate', backref='route', lazy=True)
    detail = db.relationship('Detail', backref='route', lazy=True)
    visuals = db.relationship('Visual', backref='route', lazy=True)
    coordinateformap =  db.relationship('Coordinateformap', backref='route', lazy=True)
    
    @property
    def image_path(self):
        return f'media/{form.thumbgen_filename(self.image)}'

    @property
    def image_path(self):
        return f'media/{form.thumbgen_filename(self.image)}'

    def __repr__(self):
        return f'<Route {self.title}>'


class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    order = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Coordinate {self.longitude}>'


class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.Unicode(128), nullable=False)
    routestart = db.Column(db.Text(), nullable=False)
    workingmode = db.Column(db.Text(), nullable=False)
    longitude_for_pictutre = db.Column(db.Float, nullable=True)
    latitude_for_picture = db.Column(db.Float, nullable=True)
    order = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return f'<Detail {self.description}>'


class Visual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Unicode(128), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    
    @property
    def image_path(self):
        return f'media/{form.thumbgen_filename(self.image)}'

    @property
    def image_path(self):
        return f'media/{form.thumbgen_filename(self.image)}'

    def __repr__(self):
        return f'<Visual {self.title}>'


class Coordinateformap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    longitude_for_image = db.Column(db.Float, nullable=False)
    latitude_for_image = db.Column(db.Float, nullable=False)
    image_for_map = db.Column(db.Unicode(128), nullable=False)
    order = db.Column(db.Integer, nullable=False)
