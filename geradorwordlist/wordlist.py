import itertools

string = input("Palavra a ser perguntada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))