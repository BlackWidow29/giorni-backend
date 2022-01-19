from flask import Flask
from .config import db, login_manager, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY

from .model import User


def create_app(config):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = SECRET_KEY

    db.init_app(app)

    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    return app


"""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager(app)
db = SQLAlchemy(app)
db.init_app(app)
"""
