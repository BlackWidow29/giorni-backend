from app.config import db

servico_orcamento = db.Table('tb_servico_orcamento',
                              db.Column('servico_id', db.Integer, db.ForeignKey('tb_servico.id'), primary_key=True),
                              db.Column('orcamento.id', db.Integer, db.ForeignKey('tb_orcamento.id', primary_key=True)))