"""
Escreva uma função que recebe um número variável de parâmetros não nomeados e
um número variado de parâmetros nomeados e imprime o valor de cada parâmetro
recebido.
"""


def imprimir_parametros(*args, **kwargs):
    # Imprime os parâmetros não nomeados
    for parametro in args:
        print(parametro)

    # Imprime os parâmetros nomeados
    for valor in kwargs.values():
        print(valor)


# Chama a função com os parâmetros especificados
imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
