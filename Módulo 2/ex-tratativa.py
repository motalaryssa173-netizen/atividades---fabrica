import requests

url = 'https://jsonplaceholder.typicode.com/post/999999'

try:
    resposta = requests.get(url)
    resposta.raise_for_status() # lança exceção se status >= 400
    dados = resposta.json()
    print(dados['title'])

except requests.exceptions.HTTPError as e:
    print(f"Erro HTTPS: {e}")

except requests.exceptions.ConnectionError:
    print("Erro: Não foi possível conectar ao servidor")

except requests.exceptions.Timeout:
    print("Erro: A requisição excedeu o tempo livre")

except requests.exceptions.RequestsException as e:
    print(f"Erro na requisição: {e}")