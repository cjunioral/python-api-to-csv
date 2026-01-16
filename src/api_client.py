import requests


def extrair_dados(url):
    try:
        response = requests.get(url)
        status = response.status_code
        print(f'API acessada com sucesso: {status}')
        return response.json()
    except Exception as e:
        print(f'Ocorreu um erro ao acessar a API: {status}')




