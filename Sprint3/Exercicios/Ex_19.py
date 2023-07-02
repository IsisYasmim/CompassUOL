"""
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada
na célula abaixo:
"""


import random

random_list = random.sample(range(500), 50)
random_list.sort()

mediana = 0
media = 0
valor_minimo = min(random_list)
valor_maximo = max(random_list)
tamanho = len(random_list)

# Valor médio
media = sum(random_list) / tamanho

# Mediana
mediana = (random_list[tamanho // 2 - 1] + random_list[tamanho // 2]) / 2

print(f"Media: {media}, Mediana: {mediana},", end=" ")
print(f"Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
