"""
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos 
duplicados. Utilize a lista a seguir para testar sua função.
"""

conjunto = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

set_conjunto = set(conjunto)

print(list(set_conjunto))
