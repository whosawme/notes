from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, TextAreaField


class DataForm(FlaskForm):
    message = StringField('Data', [validators.Required()])
    last_message = TextAreaField('LastMessage', default="add")
    submit = SubmitField('Submit')

class newForm(FlaskForm):
    message = TextAreaField('message')
    submit = SubmitField('Submit')