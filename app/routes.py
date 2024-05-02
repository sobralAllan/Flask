from app import app
from flask import render_template
from flask import request

@app.route('/') #Definindo a raiz do projeto
@app.route('/index', defaults={"nome":"usuário"}) #Quando não quero passar nenhum nome como parâmetro
@app.route('/index/<nome>')
def index(nome):
    dados = {"profissao":"Professor", "area":"T.I."}
    return render_template('index.html', nome=nome, dados=dados, titulo="Página Principal")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get("usuario")
    senha   = request.args.get("senha")
    return f"Usuário: {usuario}\n Senha: {senha}"

