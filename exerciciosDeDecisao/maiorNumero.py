print("### Maior Numero Digitado ###")

numero1 = int(input("Digite qualquer numero: "))
numero2 = int(input("Digite novamente qualquer numero: "))

if (numero1 > numero2):
    print("O numero maior é: {}, o primeiro digitado".format(numero1))
elif (numero1 < numero2):
    print("O numero maior é: {}, o segundo digitado.".format(numero2))
else:
      print("Numeros iguais!")
