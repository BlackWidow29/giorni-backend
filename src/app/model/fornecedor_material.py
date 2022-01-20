from app.config import db 

fornecedor_material = db.Table('tb_fornecedor_material',
                                 db.Column('fornecedor_id', db.Integer, db.ForeignKey('tb_fornecedor.id'), primary_key=True),
                                 db.Column('material_id', db.Integer, db.ForeignKey('tb_material.id'), primary_key=True))