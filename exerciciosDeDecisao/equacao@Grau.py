print("### EQUAÇÃO SEGUNDO GRAU ###")

a = float(input("Valor um: "))
b = float(input("Valor dois: "))
c = float(input("Valor três: "))

delta = b**2 -4*a*c
if delta > 0:
    print("Delta: {}".format(delta))
raizdelta = delta**0.5



if a == 0:
    print("Não é equação de segundo grau!")
elif delta < 0:
        print("A equação não possui raizes reais")
elif delta == 0:
    x1 = (-b + raizdelta) / (2 * a)
    print(x1)
elif delta > 0:
    x1 = (-b+raizdelta) / (2*a)
    print("X1: {}".format(x1))
    x2 = (-b-raizdelta) / (2*a)
    print("X2: {}".format(x2))

