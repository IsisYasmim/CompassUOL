'''
Faça um programa que imprima o dados na seguinte estrutura: 
"índice - primeiroNome sobreNome está com idade anos".
'''

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, primeiroNome in enumerate(primeirosNomes):
    sobreNome = sobreNomes[indice]
    idade = idades[indice]
    print(f"{indice} - {primeiroNome} {sobreNome} está com {idade} anos")
