print("Inserindo uma nota entre zero e dez")

nota = -1
while nota < 0 or nota > 10:
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("valor invalido")