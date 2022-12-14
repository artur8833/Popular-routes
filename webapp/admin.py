import os
from flask_admin.contrib.sqla import ModelView
from flask import url_for
from markupsafe import Markup
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask_admin import form


file_path = os.path.join(os.path.dirname(__file__), 'static', 'media')
try:
    os.mkdir(file_path)
except OSError:
    pass


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs['required'] = False
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class RouteImageView(ModelView):
    extra_js = ['/static/js/ckeditor.js', '/static/js/admin.js']

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
            url_relative_path='media/',
            thumbnail_size=(320, 240, True),
        )
    }

    form_overrides = {
        'video': CKTextAreaField,
    }


class CoordinateModelView(ModelView):
    def _list_thumbnail(view, model):
        if not model.path:
            return ''
        filename = form.thumbgen_filename(model.path)
        url = url_for('static', filename=filename)
        return Markup(f'<img src="{url}">')

    column_formatters = {
        'path': _list_thumbnail
    }


class DescriptionRouteModelView(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    def _list_thumbnail(view, model):
        if not model.path:
            return ''
        filename = form.thumbgen_filename(model.path)
        url = url_for('static', filename=filename)
        return Markup(f'<img src="{url}">')

    column_formatters = {
        'path': _list_thumbnail
    }

    form_overrides = {
        'description_start': CKTextAreaField,
        'description_basic': CKTextAreaField,
    }


class CaruselModelView(ModelView):
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
            url_relative_path='media/',
            thumbnail_size=(520, 520, True),
        )
    }

    form_overrides = {
        'description': CKTextAreaField,
    }


class CoordinateformapModelView(ModelView):
    def _list_thumbnail(view, model):
        if not model.path:
            return ''
        filename = form.thumbgen_filename(model.path)
        url = url_for('static', filename=filename)
        return Markup(f'<img src="{url}">')

    column_formatters = {
        'path': _list_thumbnail
    }

    form_extra_fields = {
        'image_for_map': form.ImageUploadField(
            'Image',
            base_path=file_path,
            url_relative_path='media/',
            thumbnail_size=(520, 520, True),
        )
    }
