from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])

    class Meta:
        csrf = False


class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=4, max=50)])
    username = StringField("Username", [validators.Length(min=4, max=50)])
    password = PasswordField("Password", [validators.Length(min=8, max=50)])
    password_conf = PasswordField("Confirm password", [validators.Length(min=8, max=50)])
    role = SelectField("Role", choices=[("ADMIN", "ADMIN"), ("USER", "USER")], default="USER")

    class Meta:
        csrf = False
