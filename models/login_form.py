from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email

class form_login(FlaskForm):

    label_email = StringField("Email:......")
    input_email = StringField("email", validators=[DataRequired(), Email()])

    label_password = StringField("Password: ")
    input_password = PasswordField("password", validators=[DataRequired(), Email(), validators.Length(min=8, max=18)])

