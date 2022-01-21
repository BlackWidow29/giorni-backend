from app.config import db 
from .servico_orcamento import servico_orcamento

class Orcamento(db.Model):
    
    __tablename__ = 'tb_orcamento'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    observacoes = db.Column(db.String(255), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('tb_cliente.id'), nullable=False)
    servico_orcamento = db.relationship('Servico', secondary=servico_orcamento, lazy='subquery',
    backref=db.backref('orcamentos'), lazy=True)
