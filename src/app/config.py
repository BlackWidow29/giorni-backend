from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from distutils.debug import DEBUG
import os

db = SQLAlchemy()

login_manager = LoginManager()


file_path = os.path.abspath(os.getcwd())+"/database.db"

SQLALCHEMY_DATABASE_URI = "postgresql://root:root@localhost/giorni"

#SQLALCHEMY_DATABASE_URI = 'sqlite:////' + file_path
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'secret'
DEBUG = True
