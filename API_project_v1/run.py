from app import create_app, db
from app.models import Client
import config

#cria o aplicativo
app = create_app(config.Config)

@app.sheel_context_processor

def make_shell_context():
    # Pode executar comandos shell durante a execução do app
    return {'db':db, 'Client':Client}