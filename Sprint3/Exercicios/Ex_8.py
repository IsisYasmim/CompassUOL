"""
Verifique se cada uma das palavras da lista é ou não um palíndromo
"""

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    if palavra == palavra[::-1]:
        print("A palavra: {} é um palíndromo".format(palavra))
    else:
        print("A palavra: {} não é um palíndromo".format(palavra))
