import requests 

url = 'https://jsonplaceholder.typicode.com/posts'

# Dados a enviar - requests converte automaticamente para JSON
novo_post = {
    'title' : 'Aprendendo requests',
    'body' : 'É muito mais fácil que urllib!',
    'userId' : 1
}

resposta = requests.post(url, json=novo_post)

print(f"Status: {resposta.status_code}")
print(f"Dados retornados: {resposta.json()}") 