import requests

try:
    # Timeout de 5 segundo
    resposta = requests.get('https://fabrica-plataforma-certificados-backend.onrender.com/ranking', timeout = 0.1)
    print(f"OK: {len(resposta.json())} posts")

except requests.exceptions.Timeout:
    print("O servidor demorou muito para responder")