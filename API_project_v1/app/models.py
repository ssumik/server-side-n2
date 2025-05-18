from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # precisa ser unico, como se fosse o login
    name = db.Column(db.String(100), index=True, unique=True)
    # precisa ser único
    email = db.Column(db.String(120), index=True, unique=True)

    def to_dict(self):
        # cria um dicionário do objeto
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }