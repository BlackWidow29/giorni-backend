from app.config import db 

class Cliente(db.Model):

    __tablename__ = 'tb_cliente'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    tipo_cliente = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    cpf_cnpj = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_endereco.id'), nullable=False)
