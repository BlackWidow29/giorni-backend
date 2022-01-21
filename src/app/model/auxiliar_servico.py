from app.config import db 

auxiliar_servico = db.Table('tb_auxliar_servico',
                                 db.Column('auxiliar_id', db.Integer, db.ForeignKey('tb_auxiliar.id'), primary_key=True),
                                 db.Column('servico_id', db.Integer, db.ForeignKey('tb_servico.id'), primary_key=True))