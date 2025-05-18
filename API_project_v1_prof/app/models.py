from app import db

class Client(db.Model): # cria o modelo de objeto para db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    # converte o objeto para um dicionário
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

