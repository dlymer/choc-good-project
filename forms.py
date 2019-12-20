from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField('Enter Username')
    password = PasswordField('Enter Password')
    submit = SubmitField('Signup!')