from app import app
from flask import render_template

@app.route('/') #Definindo a raiz do projeto
@app.route('/index')
def index():
    dados = {"profissao":"Professor", "area":"T.I."}
    return render_template('index.html', nome='Allan', dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
