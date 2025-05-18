from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import clients

# TODO: verificar o porque ele não está importando na tela de clients
