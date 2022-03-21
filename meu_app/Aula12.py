import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print('Bairro: {}'.format(dados_cep['bairro']))
    print('Cidade: {}'.format(dados_cep['localidade']))
    print('Rua: {}'.format(dados_cep['logradouro']))
    return dados_cep

if __name__ == '__main__':
    retorna_dados_cep('40220310')
