"""
Use Carpentry to build forms.
"""

from io import StringIO


class ModelForm(object):
    model = None

    def __init__(self, model=None):
        if model is not None:
            self.model = model

    def render_html(self, form_action='', form_method='POST'):
        """Generate bootstrap-compatible HTML forms"""

        # todo: we should render this using something better
        # For example, we could offer some hooks for using jinja templates..
        _output = StringIO()
        _output.write(u'<form action="{0}" method="{1}" role="form">'
                      .format(form_action, form_method))

        for name, field in self.model.iter_fields():
            field_id = u'field-{0}'.format(name)
            field_title = unicode(name).replace(u'_', u' ').title()
            if field.required:
                field_title += u' <span style="color:red;">*</span>'

            _output.write(u'<div class="form-group">')
            _output.write(u'<label for="{0}">'.format(field_id))
            _output.write(field_title)
            _output.write(u'</label>')
            _output.write(u'<input type="{field_type}" name="{field_name}"'
                          u' class="form-control" id="{field_id}"'
                          u' placeholder=""/>'
                          .format(field_type='text', field_id=field_id,
                                  field_name=name))
            _output.write(u'</div>')

        _output.write(u'<button type="submit" class="btn btn-default">'
                      u'Submit</button>')

        _output.write(u'</form>')
        return _output.getvalue()

    def __str__(self):
        return self.render_html().encode('utf-8')

    def __unicode__(self):
        return self.render_html()
