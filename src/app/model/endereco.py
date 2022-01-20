from app.config import db 

class Endereco(db.Model):
    __tablename__ = 'tb_endereco'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    logradouro = db.Column(db.String(150), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cliente = db.relationship('Cliente', backref='tb_endereco', lazy=True)

    def __init__(self, numero,cep,cidade,bairro,logradouro,estado):
        self.numero = numero
        self.cep = cep
        self.cidade = cidade
        self.bairro = bairro
        self.logradouro = logradouro
        self.estado = estado