from flask import Flask
app = Flask(__name__)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vehiclelogs.db"
app.config["SQLALCHEMY_ECHO"] = True

db =SQLAlchemy(app)

from application import views

from application.vehicles import models
from application.vehicles import views

from application.auth import models
from application.auth import views

from application.logs import models
from application.logs import views

from application.auth.models import User
from application.auth.models import Role
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please, login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from flask_user import UserManager, SQLAlchemyAdapter

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)


db.create_all()

if not User.query.filter_by(username='akuankka').first():
    name = 'Aku Ankka'
    username = 'akuankka'
    pwd = 'akuankka'
    user1 = User(name, username, pwd)
    user1.roles.append(Role(name='ADMIN'))

    db.session().add(user1)
    db.session().commit()

