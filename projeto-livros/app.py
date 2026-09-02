from flask import Flask, jsonify, request

app = Flask(__name__)

# Listar livros
livros = [
    {'id': 1, 'titulo': 'O Senhor Dos Aneis', 'autor': 'J.R.R. Tolkien', 'ano': 1954},
    {'id': 2, 'titulo': '1984', 'autor':'George Orwell', 'ano': 1949},
    {'id': 3, 'titulo': 'Dom Casmurro', 'autor' : 'Machado de Assis', 'ano': 1899} 
]

@app.route("/api/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

# Buscar livros por ID
@app.route("/api/livros/<int:id>", methods=["GET"])
def buscar_livros(id):
    livro = next((l for l in livros if l['id'] == id), None)
    if livro: 
        return jsonify(livro)
    return jsonify({"erro": "Livro nao encontrado"}), 404

@app.route("/api/livros", methods=["POST"])
def criar_livro():
    dados = request.get_json()
    novo_livro = {
        'id': len(livros) + 1,
        'titulo': dados['titulo'],
        'autor': dados['autor'],
        'ano': dados['ano']
    }
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route("/api/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    livro = next((l for l in livros if l['id'] == id), None)
    if not livro:
        return jsonify({"erro" : "Livro não encontrado."}), 404

    dados = request.get_json()
    livro["titulo"] = dados.get("titulo", livro["titulo"])
    livro["autor"] = dados.get("autor", livro["autor"])
    livro["ano"] = dados.get("ano", livro["ano"])
    
    return jsonify(livro)

@app.route("/api/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    global livros
    livro = next((l for l in livros if l['id'] == id), None)
    if not livro:
        return jsonify ({"erro": "Livro não encontrado."}), 404

    livros = [l for l in livros if["id"] != id]
    return jsonify({"mensagem": "Livro excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)