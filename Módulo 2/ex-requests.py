import requests

# Requisição GET simples
resposta = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# A resposta já é interpretada automaticamente
print(f"Status: {resposta.status_code}")
print(f"Tipo de conteúdo: {resposta.headers['Content-Type']}")

# JSON já vem como dicionário Python - sem necessidade de json.loads()
dados = resposta.json()
print(f"Título: {dados['title']}")
print(f"Conteúdo: {dados['body']}")