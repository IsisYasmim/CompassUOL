"""
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas:
a lista recebida dividida em 3 partes iguais.
Teste sua implementação com a lista abaixo
"""


def dividir_lista(lista):
    tamanho = len(lista)
    tamanho_novalista = tamanho // 3  # Tamanho da nova lista
    partes = []

    for i in range(0, tamanho, tamanho_novalista):
        parte = lista[i:i+tamanho_novalista]  # Seleciona a parte da lista
        partes.append(parte)  # Adiciona a parte à lista de partes

    return partes


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(dividir_lista(lista))
