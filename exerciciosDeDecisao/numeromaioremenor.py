print("### Numero maior ###")

entrada1 = int(input("Digite um numero: "))
entrada2 = int(input("Digite outro numero: "))
entrada3 = int(input("Digite somente este numero: "))

def maiornumero():
    if entrada1 > entrada2 and entrada1 > entrada3:
        print("O maior numero é: {}. O primeiro numero digitado!".format(entrada1))
    elif entrada2 > entrada1 and entrada2 > entrada3:
        print("O maior numero é: {}. O segundo numero digitado!".format(entrada2))
    elif entrada3 > entrada1 and entrada3 > entrada2:
        print("O maior numero é: {}. O terceiro numero digitado!".format(entrada3))
    else:
        print("Não digitou numero!")
def menor_numero():
    if entrada1 < entrada2 and entrada1 < entrada3:
        print("O menor numero é: {}. O primeiro numero digitado!".format(entrada1))
    elif entrada2 < entrada1 and entrada2 < entrada3:
        print("O menor numero é: {}. O segundo numero digitado!".format(entrada2))
    elif entrada3 < entrada1 and entrada3 < entrada2:
        print("O menor numero é: {}. O terceiro numero digitado!".format(entrada3))
    else:
        print("Não digitou numero!")

maiornumero()
menor_numero()