print("### PROGRAMA QUE IMPRIME NUMEROS ###")

def sequencial():
    contador = 0
    while contador <= 20:
        print(contador)
        contador = contador + 1

def ladoALado():
    contador = 0
    while contador <= 20:
        print(contador, end=" ")
        contador = contador + 1

sequencial()
ladoALado()