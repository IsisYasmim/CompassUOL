"""
Implemente a função my_map(list, f) que recebe uma lista como 1º argumento
e uma função como 2º argumento. Esta função aplica a função recebida
para cada elemento da lista recebida e retorna o resultado em uma nova lista.
"""


# Função que calcula a potência de 2 para um número
def potencia_de_2(numero):
    return numero ** 2


def my_map(lista, f):
    # Lista vazia para armazenar os resultados
    resultado = []

    # Percorre cada elemento da lista
    for numero in lista:
        # Aplica a função no elemento e adiciona ao resultado
        resultado.append(f(numero))

    # Retorna a nova lista com os resultados
    return resultado


# Lista de entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chama a função my_map e imprime o resultado
print(my_map(lista, potencia_de_2))
