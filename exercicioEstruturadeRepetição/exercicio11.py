numero_um = int(input("Digite um numero: "))
numero_dois = int(input("Digite outro numero: "))


for i in range(numero_um, numero_dois, 1):
    print('\n'.format(i))
    soma = i + i
    print(soma)
# for i in range(numero_dois, numero_um, 1):
#     print(i)