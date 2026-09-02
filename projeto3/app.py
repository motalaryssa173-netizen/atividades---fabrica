from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nome>")
def usuario(nome):
    return f"Seja bem-vindo {nome}!!"

@app.route("/quadrado/<int:numero>")
def quadrado(numero):
    quadrado = numero ** 2
    return f"O {numero} ao quadrado é {quadrado}"

if __name__ == "__main__":
    app.run(debug=True)