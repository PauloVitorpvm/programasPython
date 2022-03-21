print("Ano bisexto!!!")

ano = int(input("Digite o ano: "))
bisexto = ano % 4
bisexto2 = ano % 100
bisexto3 = ano % 400

if (bisexto == 0 and bisexto2 != 0) or (bisexto == 0 and bisexto2 == 0 and bisexto3 == 0):
    print("Ano bisexto: {}".format(ano))
else:
    print("Não é ano bisexto!")