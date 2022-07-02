import os
from flask_admin.contrib.sqla import ModelView
from flask import url_for
from flask_admin import form
from markupsafe import Markup
from wtforms import TextAreaField
from wtforms.widgets import TextArea

file_path = os.path.join(os.path.dirname(__file__), 'static')
try:
    os.mkdir(file_path)
except OSError:
    pass


class CKTextAreaWidget(TextArea):

    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class RouteImageView(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

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

    form_overrides = {
        'description': CKTextAreaField,
    }


class CoordinateModelView(ModelView):

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        filename = form.thumbgen_filename(model.path)
        url = url_for('static', filename=filename)
        return Markup(f'<img src="{url}">')

    column_formatters = {
        'path': _list_thumbnail
    }


class DetailModelView(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

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
            thumbnail_size=(520, 520, True),
        )
    }

    form_overrides = {
        'description': CKTextAreaField,
    }


class VisualModelView(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

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
            thumbnail_size=(520, 520, True),
        )
    }

    form_overrides = {
        'description': CKTextAreaField,
    }
