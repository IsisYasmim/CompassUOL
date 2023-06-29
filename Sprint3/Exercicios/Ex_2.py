#Escreva um código Python para verificar se três números digitados na entrada 
#padrão são pares ou ímpares. 

# Solicitar três números do usuário
numeros = []
for i in range(3):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Verificar se cada número é par ou ímpar e imprimir a saída
for numero in numeros:
    if numero % 2 == 0:
        print("Par:", numero)
    else:
        print("Ímpar:", numero)
