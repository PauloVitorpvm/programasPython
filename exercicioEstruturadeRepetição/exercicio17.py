print("### NÚMERO FATORIAL ###")

numero = int(input("Digite o numero para da o resultado fatorial: "))
fatorial = numero - 1
for i in range(fatorial):
    numero = numero * fatorial
    fatorial = fatorial - 1
    #print(numero)
    #print(i)

print("O fatorial é: {}".format(numero))

    # if numero == 0 or numero == 1:
    #     print('Fatorial de {} é: 1'.format(numero))
    # else:
    #     numero = numero * fatorial
    #     print(numero)


