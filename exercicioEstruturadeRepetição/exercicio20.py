print("### NÚMERO FATORIAL ###")
quantidade = True
while quantidade:
    numero = int(input("Digite o numero para da o resultado fatorial: "))
    fatorial = numero - 1
    if numero <= 16 and numero > 0:
        for i in range(fatorial):
            numero = numero * fatorial
            fatorial = fatorial - 1
            #print(numero)
            #print(i)
        print("O fatorial é: {}".format(numero))
    else:
        print("So pode menor que 16 e numeros positvos")

