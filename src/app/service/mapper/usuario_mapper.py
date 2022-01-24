from app.model.usuario import Usuario
from service.dto.usuario_dto import UsuarioDto


def to_dto(usuario: Usuario):
    return UsuarioDto(usuario.id, usuario.email, usuario.login, usuario.senha)


def to_entity(usuario_dto: UsuarioDto):
    return Usuario(usuario_dto._email, usuario_dto._login, usuario_dto._senha, id=usuario_dto._id)
