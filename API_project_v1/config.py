import os

# Caminho relativo para aplicação
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    # Buscar um arquivo na estrutura de arquivos contendo a chave secreta
    # Utilizamps o you-will-never-guess para acessar sem precisar gerar uma chave secreta
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Endereço do banco de dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Se quiser fazer log de todas as modificações
    SQLALCHEMY_TRACK_MODIFICATIONS = False