# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa.
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

import datetime

# Obter nome e idade atual
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade atual: "))

# Obter o ano atual
ano_atual = datetime.date.today().year

# Calcular o ano em que a pessoa completará 100 anos
ano_completa_100 = ano_atual + (100 - idade)

# Imprimir resultado
print(ano_completa_100)
