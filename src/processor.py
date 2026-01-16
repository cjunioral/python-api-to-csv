import csv


def processar_dados(dados):
    dados_tratados = []
    
    for dado in dados['competitions']:
        dados_tratados.append({
            'nome': dado.get('name'),
            'codigo': dado.get('code'),
            'pais': dado.get('area', {}).get('name')
        })
        
    return dados_tratados


def salvar_dados(dados_tratados):
    with open('data/dados_tratados.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=dados_tratados[0].keys())
        writer.writeheader()
        
        writer.writerows(dados_tratados)

        