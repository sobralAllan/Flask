from flask import Flask
app = Flask(__name__) #Instanciando o objeto Flask
from app import routes
