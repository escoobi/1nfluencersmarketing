from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

class form_users_update(FlaskForm):


    label_name = StringField("Fullname: ")



    label_email = StringField("Email......:")




    label_password = StringField("Password: ")
    input_password = PasswordField("password", validators=[DataRequired(), validators.Length(min=8, max=18)])

