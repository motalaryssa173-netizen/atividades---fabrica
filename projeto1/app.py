from flask import Flask

# Cria a instância da aplicação
app = Flask(__name__)

# Define uma rota
@app.route('/')
def hello():
    return 'Olá, mundo!'

if __name__ == '__main__':
    app.run(debug=True)