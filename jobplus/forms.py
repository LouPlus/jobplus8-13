from flask_wtf import FlaskForm
from wtforms import (StringField,PasswordField,SubmitField,BooleanField,ValadationError)
from wtforms.validators import Length,Email,EqualTo,Required
from jobplus.models import db,User

class UserregisterForm(FlaskForm):
    username = StringField('用户名'validators=[Required(),Length(3,24)])
    email = StringField('')
