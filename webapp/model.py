import os

from flask import url_for, app
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(app, db)

file_path = os.path.join(os.path.dirname(__file__), 'static',)
try:
    os.mkdir(file_path)
except OSError:
    pass


class route_liste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.Unicode(128), nullable=False)


class routImageView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        filename = form.thumbgen_filename(model.path)
        url = url_for('static', filename=filename)

        return Markup(f'<img src="{url}">')

    column_formatters = {
        'path': _list_thumbnail
    }

    form_extra_fields = {
        'image': form.ImageUploadField(
            'Image',
            base_path=file_path,
            thumbnail_size=(320, 240, True),
        )
    }


def __repr__(self):
    return '<route_liste {}{} >'.format(self.title, self.description, self.image)


