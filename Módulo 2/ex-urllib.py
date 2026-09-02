import urllib.request
import json

# URL da API de posts (publicacoes)
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Faz a requisicao GET
resposta = urllib.request.urlopen(url)

# Le e decotifica os dados
dados = resposta.read().decode('utf-8')

# Converte de JSON para dicionario python
post = json.loads(dados)

#exibe dados
print(f"Titulo: {post['title']}")
print(f"Conteudo: {post['body']}")