from app.config import db 

material_servico = db.Table('tb_material_servico',
                                 db.Column('material_id', db.Integer, db.ForeignKey('tb_material.id'), primary_key=True),
                                 db.Column('servico_id', db.Integer, db.ForeignKey('tb_fornecedor.id'), primary_key=True))