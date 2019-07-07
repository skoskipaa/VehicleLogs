from application import db


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    log_type = db.Column(db.String(30), nullable=False)
    odometer = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, default=0)
    details = db.Column(db.String(200))

    driver_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                          nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'),
                           nullable=False)

    def __init__(self, log_type, odometer, driver_id, vehicle_id):
        self.log_type = log_type
        self.odometer = odometer
        self.driver_id = driver_id
        self.vehicle_id = vehicle_id
