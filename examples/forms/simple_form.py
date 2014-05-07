"""
Generate a simple form.
Requires flask.
"""

from flask import Flask, request, escape

from carpentry.contrib.forms import ModelForm
from carpentry import BaseObject, StringField


class MyModel(BaseObject):
    first_name = StringField()
    last_name = StringField()
    email = StringField()


app = Flask(__name__)


BASE_HTML = u"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css"><!-- # noqa -->
</head>
<body>{body_content}</body>
</html>
"""


FORM_PAGE = BASE_HTML.format(body_content=u"""
<div class="container">
    <h1>Insert your data here</h1>
    <div class="alert alert-warning">
    <strong>WARNING:</strong>
    You <strong>will</strong> be sent spam!</div>
    {form}
</div>
""")


RESULTS_PAGE = BASE_HTML.format(body_content=u"""
<div class="container">
    <h1>Spam has been sent to:</h1>

    {first} {last} &lt;{email}&gt;
</div>
""")


@app.route('/')
def landing_page():
    form = ModelForm(MyModel)
    return FORM_PAGE.format(form=form.render_html(form_action='/submit'))


@app.route('/submit', methods=['POST'])
def submitted_page():
    return RESULTS_PAGE.format(
        first=escape(request.form['first_name']),
        last=escape(request.form['last_name']),
        email=escape(request.form['email']))


if __name__ == '__main__':
    app.run(debug=True)
