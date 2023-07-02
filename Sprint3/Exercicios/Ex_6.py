'''
Escreva um programa para avaliar o que ambas as listas têm em comum 
(sem repetições)
'''

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Converter as listas em conjuntos
set_a = set(a)
set_b = set(b)

# Encontrar a interseção entre os conjuntos
intersecao = set_a & set_b

# Imprimir a lista de valores da interseção
print(list(intersecao))
