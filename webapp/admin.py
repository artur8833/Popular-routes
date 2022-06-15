import os
from flask_admin.contrib.sqla import ModelView
from flask import url_for
from flask_admin import form
from markupsafe import Markup


file_path = os.path.join(os.path.dirname(__file__), 'static',)
try:
    os.mkdir(file_path)
except OSError:
    pass


class RouteImageView(ModelView):
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
