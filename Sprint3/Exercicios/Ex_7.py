'''
Faça um programa que gere uma nova lista contendo apenas números ímpares.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
Gerar nova lista com números ímpares 
(se o resto da divisão de 2 for diferente de 0)
'''
impar = [numero for numero in a if numero % 2 != 0]


# Imprimir a nova lista
print(impar)
