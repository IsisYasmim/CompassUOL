'''
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo
'''
import json

# Abre o arquivo JSON no modo de leitura
with open("person.json", "r") as arquivo:
    # Faz o parsing e imprime o conteúdo do JSON
    print(json.load(arquivo))
