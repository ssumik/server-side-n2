from flask import jsonify, request
from app import db
from app.models import Client
from app.routes import bp
from app.auth import token_required

@bp.route('/clients', methods=['GET'])
@token_required
def get_client(current_user):
    # recupera uma id de cliente que pode ter sido passado por parâmetro
    client_id = request.args.get('client_id')

    # se existir uma id de cliente
    if client_id:
        try:
            client = Client.query.get_or_404(client_id)
            return jsonify(client.to_dict()), 200 # sucesso na requisição
        except Exception as e:
            return jsonify({'erro': str(e)}), 500
    else:
        # se não tem um id, manda todos os clientes
        try:
            clients = Client.query.all()
            return jsonify([client.to_dict() for client in clients]), 200 # sucesso na requisição
        except Exception as e:
            return jsonify({'erro': str(e)})



@bp.route('/clients', methods=['POST'])
@token_required
def create_client(current_user):
    try:
        # recuperar o conteudo do json
        data = request.get_json() or {}

        if 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required'})
        if Client.query.filter_by(email=data['email']).first():
        # if Client.query.filter_by(email="andrei.carniel@catolicasc.com.br").first():
            return jsonify({'error': 'Email already exists'})

        client = Client(name=data['name'], email=data['email'])
        db.session.add(client)
        db.session.commit()

        return jsonify(client.to_dict()), 201 # sucesso na criação
    except Exception as e:
        return jsonify({'error': str(e)}), 500 # erro de servidor





