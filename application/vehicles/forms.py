from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators


class VehicleForm(FlaskForm):
    plate = StringField("License plate", [validators.Length(min=1, max=15)])
    nickname = StringField("Nickname", [validators.Length(max=100)])
    make = StringField("Make", [validators.Length(min=1, max=30)])
    model = StringField("Model", [validators.Length(max=50)])
    year = IntegerField("Year", [validators.InputRequired(),
                                 validators.NumberRange(min=1900, max=2019)])
    kilometers = IntegerField("Odometer reading",
                              [validators.InputRequired(),
                               validators.NumberRange(min=0, max=999999)])
 
    class Meta:
        csrf = False    
# Nykyinen vuosi maksimiksi vuosimallille??
