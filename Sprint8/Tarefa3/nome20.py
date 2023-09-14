'''
Em Python, declare e inicialize uma lista contendo o nome de 20 animais.
Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um
(você pode utilizar list comprehension aqui).  Na sequência, armazene o
conteúdo da lista em um arquivo de texto, um item em cada linha,
no formato CSV.
'''
import csv

nomes = ("vaca", "cachorro", "gato", "cavalo", "hipopotamo", "coelho",
         "pato", "peixe", "golfinho", "tubarao", "falcao", "galinha", "ovelha",
         "borboleta", "grilo", "tamandua", "tatu", "capivara", "foca",
         "estrela-do-mar")

nomes_ordenado = sorted(nomes)
[print(nome) for nome in nomes_ordenado]

with open("animais.csv", "w", newline="") as arquivo:
    csvwriter = csv.writer(arquivo)
    csvwriter.writerows([[animal] for animal in nomes_ordenado])
