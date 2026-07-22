from config import db
from modelos.usuarios import Usuario

class UsuarioDAO:

    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def listar_todos():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_cadastro(cadastro):
        return Usuario.query.filter_by(cadastro=cadastro).first()


