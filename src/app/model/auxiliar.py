from app.config import db 
from .auxiliar_servico import auxiliar_servico

class Auxiliar(db.Model):

    __tablename__ = "tb_auxiliar"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo_servico = db.Column(db.String(50), nullable=False)
    disponibilidade = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.Integer, db.ForeignKey('tb_telefone.id'), nullable=False)
    auxiliar_servico = db.relationship('Servico', secondary=auxiliar_servico, lazy='subquery',
    backref=db.backref('auxiliares', lazy=True))