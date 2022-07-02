from webapp.extensions import db
from webapp.admin import JsonEncodedDict


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.Unicode(128), nullable=False)
    coordinates = db.relationship('Coordinate', backref='route', lazy=True)
    detail = db.relationship('Detail', backref='route', lazy=True)
    visuals = db.relationship('Visual', backref='route', lazy=True)
    way=db.relationship('Way', backref='route', lazy=True)

    def __repr__(self):
        return f'<Route {self.title}>'


class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    altitude = db.Column(db.Float, nullable=False)
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
    order = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Detail {self.description}>'


class Visual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Unicode(128), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)

    def __repr__(self):
        return f'<Visual {self.title}>'


class Way(db.Model):
    __tablename__ = 'way'
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    fancy_name = db.Column(JsonEncodedDict)


