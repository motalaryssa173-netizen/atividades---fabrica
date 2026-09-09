from flask import Flask, request, jsonify

app = Flask(__name__)

musicas = [
    {
        "id": 1,
        "titulo": "Astronomia",
        "artista": "Tony Igy",
        "duracao": 236,
        "url": "https://example.com/tony-igy-astronomia"
    }
]

@app.route("/tracks", methods=["GET"])
def listar_musicas():
    return jsonify(musicas)

@app.route("/tracks/<id>", methods=["GET"])
def buscar_musica():
    musica = next((m for m in musicas if m ["id"] == id), None)
    if not musica:
        return jsonify({"erro": "Música não encontrada!"}), 404

    return jsonify(musica)

@app.route("/tracks", methods=["POST"])
def add_musica():
    dados = request.get_json()
    nova_musica = {
        "id": len(musicas) + 1,
        "titulo": dados["titulo"],
        "artista": dados["artista"],
        "duracao": dados["duracao"],
        "url": dados["url"]
    }

    musicas.append(nova_musica)
    return jsonify(nova_musica), 201

@app.route("/tracks/<id>", methods=["PUT"])
def atualizar_musica(id):
    musica = next((m for m in musicas if m["id"]), None)
    if not musica: 
        return jsonify({"erro": "Música não encontrada!"}), 404

    dados = request.get_json()
    musica["titulo"] = dados.get("titulo", musica["titulo"])
    musica["artista"] = dados.get("artista", musica["artista"])
    musica["duracao"] = dados.get("duracao", musica["duracao"])
    musica["url"] = dados.get("url", musica["url"])

    return jsonify(musica)

@app.route("/tracks/<id>", methods=["DELETE"])
def excluir_livro(id):
    global musicas
    musica = next((m for m in musicas if m["id"] == id), None)
    if not musicas:
       return jsonify({"erro": "Música não encontrada!"}), 404
    
    musica = [m for m in musicas if m["id"] != id]
    return jsonify({"mensagem": "Música excluída com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)