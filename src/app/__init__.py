from flask import Flask
from .config import db, login_manager, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY

from .controller.usuario_controller import api


from .model import fornecedor, usuario, material, fornecedor_material, servico, material_servico, endereco, cliente


def create_app(config):
    app = Flask(__name__)
    app.register_blueprint(api)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = SECRET_KEY

    db.init_app(app)

    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    return app
