from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, validators


class LogForm(FlaskForm):
    log_type = SelectField("Log type", choices=[("Drive", "Drive"),
                                                ("Maintenance", "Maintenance"),
                                                ("Fill up", "Fill up")],
                           default="Drive")
    odometer = IntegerField("Odometer",
                            [validators.NumberRange(min=1, max=999999)])
    cost = IntegerField("Total Cost", [validators.NumberRange(min=0)], default=0)
    details = StringField("Details")

    class Meta:
        csrf = False
