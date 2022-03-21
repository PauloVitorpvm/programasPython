print("### Converter Fahrenheit para Celsus ###")

f = float(input("Digite a temperatura em Fahrenheit: "))

#c = 5 * ((f-32)/9)
c = (f - 32) * (5/9)
#f = (c * (9/5)) + 32

print("Temperatura em Fahrenheit: {}, temperatura convertida em Celsus: {}".format(f, c))


