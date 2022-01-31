from crypt import methods
from src.app.service import usuario_service
from flask import request, Blueprint

api = Blueprint('api', __name__,url_prefix='/api')

@api.route('/usuario', methods=['POST'])
def cadastrar_usuario():
    usuario = request.data
    print(usuario)