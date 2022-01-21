from app.config import db 

class Telefone(db.Model):

    __tablename__ = "tb_telefone"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    numero = db.Column(db.String(11), nullable=False)