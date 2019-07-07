from application import db


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    plate = db.Column(db.String(15), unique=True, nullable=False)
    nickname = db.Column(db.String(100), unique=True)
    make = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(50))
    year = db.Column(db.Integer, nullable=False)
    kilometers = db.Column(db.Integer, nullable=False)

    logs = db.relationship("Log", backref='vehicle', lazy=True)

    def __init__(self, plate, nickname, make, model, year, kilometers):
        self.plate = plate
        self.nickname = nickname
        self.make = make
        self.model = model
        self.year = year
        self.kilometers = kilometers
