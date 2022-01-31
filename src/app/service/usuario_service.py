from ast import Return
from src.app.service.dto.usuario_dto import UsuarioDto
from src.app.model.usuario import Usuario
from src.app import app, db

def save(usuario_dto: UsuarioDto):
    try:    
        usuario = Usuario(email=usuario_dto._email, login=usuario_dto._login, senha=usuario_dto._senha)
        db.session.add(usuario)
        db.session.commit()
        return 'Usuario salvo com sucesso!'
    except:
        return 'Ocorreu um erro na hora de salvar este usuário'