import requests


cep = '08431-800'

link = f'http://viacep.com.br/ws/{cep}/json/'



requisicao = requests.get(link)
print(type(requisicao))

endereco = requisicao.json()

print(type(endereco))
print(requisicao.json())

