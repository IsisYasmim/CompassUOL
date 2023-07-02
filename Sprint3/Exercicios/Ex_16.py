"""
Escreva uma função que recebe uma string de números separados por vírgula e
retorne a soma de todos eles. Depois imprima a soma dos valores.
"""


def soma_numeros(string_numeros):
    # Divide a string em uma lista de números
    numeros = string_numeros.split(',')
    soma = 0
    for numero in numeros:
        soma += int(numero)  # Converte cada número para inteiro e soma
    return soma


string_numeros = "1,3,4,6,10,76"
print(soma_numeros(string_numeros))
