from webapp.extensions import db


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.Unicode(128), nullable=False)
    coordinates = db.relationship('Coordinate', backref='route', lazy=True)

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
        return f'<Coordinate {self.route_id}>'
