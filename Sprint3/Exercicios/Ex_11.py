'''
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt 
imprime o seu conteúdo.
'''
# Abre o arquivo no modo de leitura
with open("arquivo_texto.txt", "r", encoding='utf-8') as arquivo:
    # Imprime o conteúdo do arquivo
    print(arquivo.read())
