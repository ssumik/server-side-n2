from flask import Flask
from flask import request
from markupsafe import escape

#criando uma instância do flask
app = Flask(__name__, static_folder='public')

@app.route("/")
def index():
    return "<h1>Página root!</h1>"

@app.route("/teste")
def teste():
    return "<h1>Teste deu certo!</h1>"

def rule():
    return "teste2"

@app.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        data=request.form
        print(data['nome'])
        print(data['senha'])
        return 'OK - POST'
    if request.method == 'GET':
        return 'OK - GET'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login/<user>', methods=['GET', 'POST'])
def login(user):
    if request.method == 'GET':
        show_print(user)
        return f'Você enviou: {escape(user)}'
    else:
        return show_login_form(user)

def show_login_form(user):
    return f'''
           <form action="/login/{escape(user)}" method="post">
               <button type="submit">Enviar</button>
           </form>
        '''

def show_print(user):
    print(user)
    return user
app.add_url_rule('/rule','rule',rule)

if __name__ == '__main__':
    app.run(debug=True,port=4000)