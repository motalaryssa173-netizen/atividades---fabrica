from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        titulo  = "Página Inicial",
        mensagem = "Bem-vindo ao nosso site!",
        data = datetime.now().strftime('%d/%m/%Y/ %H:%M:%S')
    )

if __name__ == "__main__":
    app.run(debug=True)
