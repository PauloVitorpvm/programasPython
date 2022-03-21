if __name__ == '__main__':
    produto_1 = float(input("Digite o valor do celular: "))
    produto_2 = float(input("Digite o valor do celular: "))
    produto_3 = float(input("Digite o valor do celular: "))

    if produto_1 < produto_2 and produto_1 < produto_3:
        print("O primeiro que digitou é mais barato. Valor: {}".format(produto_1))
    elif produto_2 < produto_1 and produto_2 < produto_3:
        print("O segundo que digitou é mais barato. Valor: {}".format(produto_2))
    elif produto_3 < produto_1 and produto_3 < produto_2:
        print("O terceiro que digitou é mais barato. Vapr {}".format(produto_3))
    else:
        print("Valor invalido!")