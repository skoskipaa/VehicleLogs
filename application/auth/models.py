from application import db, bcrypt


class User(db.Model):

    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
  
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    logs = db.relationship("Log", backref='driver', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")
    
    def get_id(self):
        return self.id

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True