print("### PROGRAMA QUE  INFORMA O GENERO ESCOLHIDO ###")

entrada = input("Digite F para feminino ou M para masculino: ")

if (entrada == 'F') or (entrada == 'f'):
    print("Vocẽ escolheu Feminino!")
elif (entrada == 'M') or (entrada == 'm'):
    print("Você escolheu Masculino!")
else:
    print("SEXO INVALIDO!")