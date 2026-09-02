import requests

parametros = {'userId' : 1, '_limit' : 5}

resposta = requests.get('https://jsonplaceholder.typicode.com/posts', params = parametros)

posts = resposta.json()
print(f"Retornados: {len(posts)} posts")
for post in posts:
    print(f"-{post['title'][:40]}...")

