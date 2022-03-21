print("### SUPERMERCADO TABAJARA ###\n")
print("ATE 5KG                     ACIMA DE 5KG\n")
print("Filé Duplo R$ 4,90    por   Kg R$ 5,80 por KG")
print("Alcatra    R$ 5,90    por   Kg R$ 6,80 por KG")
print("Filé Duplo R$ 6,90    por   Kg R$ 7,80 por KG")

tipo_carne = int(input("\nQual carne gostaria de comprar:\n1 - Alcatra\n2 - File Duplo\n3 - Picanha\nDigite o numero correspondente: "))
quantidade_carnes = int(input("Quantidade: "))
cartao = int(input("Digite 1 se vai pagar com cartão tabajara ou 2 sem desconto: "))

preco = tipo_carne
desconto_cartao = 0.05

# MAIOR QUE 5KG
if tipo_carne == 1 and quantidade_carnes > 5:
    preco = quantidade_carnes * 6.80
    valor_com_des = preco - (preco * desconto_cartao)
    if cartao == 1:
        print("PREÇO ACIMA DE 5kg. Você escolheu Alcatra e comprou essa quantidade: {}, valor a pagar com desconto de 5%: {}".format(
            quantidade_carnes, valor_com_des))
    elif cartao == 2:
        print("PREÇO ACIMA DE 5kg. Você escolheu Alcatra e comprou essa quantidade: {}, valor a pagar sem desconto de 5%: {}".format(
            quantidade_carnes, preco))
    else:
        print("Valor invalido!")

if tipo_carne == 2 and quantidade_carnes > 5:
    preco = quantidade_carnes * 5.80
    valor_com_des = preco - (preco * desconto_cartao)
    if cartao == 1:
        preco = preco - (preco * desconto_cartao)
        print("PREÇO ACIMA DE 5kg. Você escolheu File Duplo  e comprou essa quantidade: {}, com desconto de 5%: {}".format(
            quantidade_carnes, valor_com_des))
    elif cartao == 2:
        print("PREÇO ACIMA DE 5kg. Você escolheu File Duplo e comprou essa quantidade: {}, valor a pagar sem desconto de 5%: {}".format(
            quantidade_carnes, preco))
    else:
        print("Valor invalido!")

if tipo_carne == 3 and quantidade_carnes > 5:
    preco = quantidade_carnes * 7.80
    valor_com_des = preco - (preco * desconto_cartao)
    if cartao == 1:
        preco = preco - (preco * desconto_cartao)
        print("PREÇO ACIMA DE 5kg. Você escolheu Picanha e comprou essa quantidade: {}, por esta acima de 5kg valor a pagar com desconto de 5%: {}".format(
            quantidade_carnes, valor_com_des))
    elif cartao == 2:
        print("PREÇO ACIMA DE 5kg. Você escolheu Picanha e comprou essa quantidade: {}, por esta acima de 5kg valor a pagar sem desconto de 5%: {}".format(
            quantidade_carnes, preco))
    else:
        print("Valor invalido!")

# ATE %5KG
if tipo_carne == 1 and quantidade_carnes <= 5:
    preco = quantidade_carnes * 5.90
    valor_com_des = preco - (preco * desconto_cartao)
    if cartao == 1:
        print("PREÇO ABAIXO DE 5kg. Você escolheu Alcatra e comprou essa quantidade: {}, valor a pagar com desconto de 5%: {}".format(
            quantidade_carnes, valor_com_des))
    elif cartao == 2:
        print("PREÇO ABAIXO DE 5kg. Você escolheu Alcatra e comprou essa quantidade: {}, valor a pagar sem desconto de 5%: {}".format(
            quantidade_carnes, preco))
    else:
        print("Valor invalido!")

if tipo_carne == 2 and quantidade_carnes <= 5:
    preco = quantidade_carnes * 4.90
    valor_com_des = preco - (preco * desconto_cartao)
    if cartao == 1:
        preco = preco - (preco * desconto_cartao)
        print("PREÇO ABAIXO DE 5kg. Você escolheu File Duplo  e comprou essa quantidade: {}, valor a pagar com desconto de 5%: {}".format(
            quantidade_carnes, valor_com_des))
    elif cartao == 2:
        print("PREÇO ABAIXO DE 5kg. Você escolheu File Duplo e comprou essa quantidade: {}, valor a pagar sem desconto de 5%: {}".format(
            quantidade_carnes, preco))
    else:
        print("Valor invalido!")

if tipo_carne == 3 and quantidade_carnes <= 5:
    preco = quantidade_carnes * 6.90
    valor_com_des = preco - (preco * desconto_cartao)
    if cartao == 1:
        preco = preco - (preco * desconto_cartao)
        print("PREÇO ABAIXO DE 5kg. Você escolheu Picanha e comprou essa quantidade: {}, valor a pagar com desconto de 5%: {}".format(
            quantidade_carnes, valor_com_des))
    elif cartao == 2:
        print("PREÇO ABAIXO DE 5kg. Você escolheu Picanha e comprou essa quantidade: {}, valor a pagar sem desconto de 5%: {}".format(
            quantidade_carnes, preco))
    else:
        print("Valor invalido!")