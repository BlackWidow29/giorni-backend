from flask import Flask
from app.config import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


# db.create_all()
