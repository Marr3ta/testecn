import urllib.request
import json

cnpj = input("Informe um CNPJ:")

with urllib.request.urlopen(f"https://receitaws.com.br/v1/cnpj/{cnpj}") as url:
    dados = json.loads(url.read().decode())


print('Nome: ' + dados['nome'])
print('Cnpj: ' + dados['cnpj'])
print('Situação: ' + dados['situacao'])
