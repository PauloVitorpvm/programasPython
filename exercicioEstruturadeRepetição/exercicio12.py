# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
# deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

numero = float(input("Digite um numero entre 1 e 10 para mostrar a tabuada: "))
operacao = int(input("Escolha uma opção para mostrar a tabuáda!\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"
                     "Digite: "))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

#while numero <= 10 and operacao < 5:
if numero <= 10:
    if operacao == 1:
        print("Tabuada de soma")
        for i in lista:
            lista = i + numero
            print(lista, end=' ')

    elif operacao == 2:
        print("Tabuada de subtração")
        for i in lista:
            lista = i - numero
            print(lista, end=' ')

    elif operacao == 3:
        print("Tabuada de multiplicação")
        for i in lista:
            lista = i * numero
            print(lista, end=' ')

    elif operacao == 4:
        print("Tabuada de divisão")
        for i in lista:
            lista = i / numero
            print(lista, end=' ')
    else:
        print("Operação invalida")

else:
    print("Numero invalido")

    # numero = int(input("Digite um numero entre 1 e 10 para mostrar a tabuada: "))
    # operacao = int(
    #     input("Escolha uma opção para mostrar a tabuáda!\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"
    #           "Digite: "))


