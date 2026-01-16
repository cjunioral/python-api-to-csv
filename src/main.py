from api_client import extrair_dados
from processor import processar_dados, salvar_dados

def buscar_competicoes():
    url = 'https://api.football-data.org/v4/competitions/'
    dados = extrair_dados(url)
    return dados


def main():
    dados = buscar_competicoes()
    dados_tratados = processar_dados(dados)
    salvar_dados(dados_tratados)
    

if __name__ == '__main__':
    main()