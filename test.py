class route_liste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.Unicode(128), nullable=False)


class routModelView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        filename = form.thumbgen_filename(model.path)
        url = url_for('media', filename=filename)

        return Markup(f'<img src="{url}">')

    column_formatters = {
        'path': _list_thumbnail
    }

    orm_extra_fields = {
        'image': form.ImageUploadField(
            'Image',
            base_path=file_path,
            thumbnail_size=(320, 320, True),
        )
    }
