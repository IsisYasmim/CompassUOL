# Escreva um código Python para imprimir todos os números primos entre 1 até 100.

for numero in range(2, 101):
        eh_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                eh_primo = False
                break
        if eh_primo:
            print(numero)
