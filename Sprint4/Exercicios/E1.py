# Lendo os números inteiros do arquivo e armazenando em uma lista
with open("number.txt", "r") as file:
    numeros = list(map(int, file.readlines()))

# Filtrando apenas os números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Ordenando os números pares em ordem decrescente
numeros_pares_sorted = sorted(numeros_pares, reverse=True)
cinco_maiores = numeros_pares_sorted[:5]

# Calculando a soma dos 5 maiores números pares
soma = sum(cinco_maiores)

print(f'{cinco_maiores}')
print(f'{soma}')
