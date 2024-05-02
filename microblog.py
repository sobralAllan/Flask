from app import app
import os #Biblioteca para acesso a porta do sistema operacional

if __name__ == 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port) #Conectando a porta do Heroku


#FLASK_ENV=development - remove essa linha do arquvio .flaskenv quando for hospedar, enquanto estiver criando mantém essa linha.
#Coloquei a linha acima aqui, porque no arquivo não tem como deixar comentado
