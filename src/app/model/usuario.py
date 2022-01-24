from app.config import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class Usuario(db.Model, UserMixin):
    __tablename__ = "tb_usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)

    def __init__(self, id, login, email, senha):
        self.id = id
        self.login = login
        self.email = email
        self.senha = generate_password_hash(senha)
    
    def __init__(self, login, email, senha):
        self.login = login
        self.email = email
        self.senha = generate_password_hash(senha)

    

    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)
