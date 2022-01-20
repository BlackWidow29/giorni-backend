from app.config import db
from .material_servico import material_servico


class Servico(db.Model):

    __tablename__ = 'tb_servico'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), nullable=False)
    valor_mao_de_obra = db.Column(db.Float, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    data_inicial = db.Column(db.Date, nullable=False)
    data_final = db.Column(db.Date, nullable=False)
    material_servico = db.relationship('Material', secondary= material_servico, lazy='subquery',
    backref=db.backref('servicos', lazy=True))

    def __init__(self,descricao,valor_mao_de_obra,valor_total,data_inicial,data_final, material_servico):
        self.descricao = descricao
        self.valor_mao_de_obra = valor_mao_de_obra
        self.valor_total = valor_total
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.material_servico = material_servico
