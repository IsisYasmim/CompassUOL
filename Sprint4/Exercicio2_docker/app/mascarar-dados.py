import hashlib

while True:
    input_string = input("Insira uma string: ")
    # Gerando o hash da string
    hash_obj = hashlib.sha1(input_string.encode())
    # Utilizando o método hexdigest
    print("Hash SHA-1 da palavra:", hash_obj.hexdigest())
