from config import db
class Usuario(db.Model):

    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    __nome = db.Column(db.String(150), nullable=False)
    __email = db.Column(db.String(150), unique=True, nullable=False)
    __senha = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha


    def __repr__(self):
        return f'Usuario(Nome:{self.__nome},email:{self.__email})'