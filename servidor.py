from flask import *
from daos.usuario_dao import UsuarioDAO
from blueprints.usuario_bp import usuario_bp
from modelos.usuarios import *

app = Flask(__name__)
app.register_blueprint(usuario_bp)
app.secret_key = 'LabOratoRe0%$#'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

with app.app_context():
    db.create_all()

usuarios = []
diatreino = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/planos')
def planos():
    return render_template('planos.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():

    if request.method == 'GET':
        return render_template('cadastrar.html')

    nome = request.form.get('nomeusuario')
    email = request.form.get('emailusuario')
    senha = request.form.get('senhausuario')
    print('nomeusuario', nome)
    print('emailusuario', email)

    novo_usuario = Usuario(nome, email, senha)

    UsuarioDAO.salvar(novo_usuario)

    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('emailusuario')
    senha = request.form.get('senhausuario')

    for u in usuarios:
        if login == u.get_email() and senha == u.get_senha():
            session['usuario'] = email
            return render_template('planos.html')

    return render_template(
        'planos.html',
        mensagem='Login ou senha incorretos')


@app.route('/listar')
def listar():
    if 'usuario' in session:
        x = 1
        return 'usuario 1 <br> usuario 2'
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        debug=True
    )