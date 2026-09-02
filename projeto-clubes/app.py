from flask import Flask, jsonify, request

app = Flask(__name__)
 
clubes = [
    {
        'id': 1,
        'nome': 'Clube de Robótica',
        'descricao': 'Projetos de robótica e automação',
        'coordenador': 'Prof. Silva',
        'membros': 25
    },
    {
        'id': 2,
        'nome': 'Clube de Programação',
        'descricao': 'Desenvolvimento de software e algoristmos',
        'coordenador': 'Prof. Oliveira',
    }
]

@app.route("/api/clubes", methods=["GET"])
def listar_clubes():
    return jsonify(clubes)

@app.route("/api/clubes/<int:id>", methods=["GET"])
def buscar_clubes(id):
    clube = next((l for l in clubes if l['id'] == id), None)
    if clube: 
        return jsonify(clube)
    return jsonify({"erro": "Clube nao encontrado"}), 404

    # If not clube:
        #return jsonify({"erro": "Clube nao encontrado"}), 404
    #return jsonify(clube)

@app.route("/api/clubes", methods=["POST"])
def criar_clube():
    dados = request.get_json()
    novo_clube = {
        'id': len(clubes) + 1,
        'nome': dados['nome'],
        'descricao': dados['descricao'],
        'coordenador': dados['coordenador'],
        'membros': dados['membros']
    }
    clubes.append(novo_clube)
    return jsonify(novo_clube), 201

@app.route("/api/clubes/<int:id>", methods=["PUT"])
def atualizar_clube(id):
    clube = next((l for l in clubes if l['id'] == id), None) 
    if not clube:
        return jsonify({"erro" : "Clube não encontrado."}), 404

    dados = request.get_json()
    clube["nome"] = dados.get("nome", clube["nome"])
    clube["descricao"] = dados.get("descricao", clube["descricao"])
    clube["coordenador"] = dados.get("coordenador", clube["coordenador"])
    clube["membros"] = dados.get("membros", clube["membros"])

    return jsonify(clubes)

@app.route("/api/clubes/<int:id>", methods=["DELETE"])
def excluir_clube(id):
    global clubes
    clube = next((c for c in clubes if c['id'] == id), None)
    if not clube:
        return jsonify ({"erro": "Clube não encontrado."}), 404

    clubes = [c for c in clubes if c ["id"] != id]
    return jsonify({"mensagem": "Clube excluído com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)