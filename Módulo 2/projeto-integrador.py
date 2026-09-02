import requests 

def obter_coodernadas(cidade):
    """ Obter latitude e longitude de uma cidade"""
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {'name':cidade, 'count': 1, 'language': 'pt', 'format':'json'}

    resposta = requests.get(url, params=params, timeout=5)
    resposta.raise_for_status()

    dados = resposta.json()
    if 'results' not in dados or not dados['results']:
        return None

    resultado = dados['results'][0]
    return {
        'nome': resultado['name'],
        'pais': resultado.get('country','desconhecido'),
        'latitude': resultado['latitude'],
        'longitude': resultado['longitude']
    }

def obter_clima(latitude, longitude):
    """ Obtem dados climáticos atuais."""
    url = 'https://api.open-meteo.com/v1/forecast'
    params ={ 
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m, relative_humidity_2m, apparent_temperature, wind_speed_10m',
        'timezone': 'auto'
    }

    resposta = requests.get(url, params=params, timeout=5)
    resposta.raise_for_status()
    return resposta.json()['current']

def main():
    print('=== Consutor de clima ===')
    cidade = input('Digite o nome de uma cidade: ')

    coords = obter_coodernadas(cidade)
    if not coords: 
        print(f"Cidade '{cidade}' não encontrada.")
        return

    print(f"Localizando:{ coords['nome']}, {coords['pais']}")

    clima = obter_clima(coords['latitude'], coords['longitude'])

    print("\n --- Dados Atuais ---")
    print(f"Temperatura: {clima['temperature_2m']} °C")
    print(f"Sensação térmica: {clima['apparent_temperature']} °C")
    print(f"Umidade: {clima['relative_humidity_2m']}%")
    print(f"Vento: {clima['wind_speed_10m']} km/h")

if __name__ == '__main__':
    main()