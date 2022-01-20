from app.config import db 
from .fornecedor_material import fornecedor_material


class Material(db.Model):
    __tablename__ = "tb_material"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), nullable=False)
    cor = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    quantidade_disponivel = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    fornecedor_material = db.relationship('Fornecedor', secondary=fornecedor_material, lazy='subquery',
    backref=db.backref('materiais', lazy=True))

    def __init__(self, descricao, cor, tipo, categoria, quantidade_disponivel, preco, fornecedor_material):
        self.descricao = descricao
        self.cor = cor
        self.tipo = tipo
        self.categoria = categoria
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco
        self.fornecedor_material = fornecedor_material