print("### ALtura ideal ###")

altura = float(input("Digite sua altura: "))
sexo = input("Digite F para feminino e M para masculino: ")

altura_masculino = (72.7 * altura) - 58
altura_feminino = (62.1 * altura) - 44.7

if sexo == 'M' or sexo == 'm':
    print(" Seu sexo é masculino! Sua altura é: {}, logo então seu peso ideal deverá ser de: {}".format(altura, altura_masculino))
elif sexo == 'F' or sexo == 'f':
    print(" Seu sexo é feminino! Sua altura é: {}, logo então seu peso ideal deverá ser de: {}".format(altura, altura_feminino))
else:
    print("Não digitou a letra correspondente ao genero!")
