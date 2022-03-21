print("### Loja de tintas ###")

cobertura_tinta = 3
capacidade_lata = 18
valor_tinta = 80.0

tamanho_area = float(input("Insira o tamanho da area em m²: "))
litro = tamanho_area / cobertura_tinta
latas = int(litro / capacidade_lata)

if(litro % capacidade_lata != 0):
    latas += 1

valor_total = latas * valor_tinta

print("A Quantidade de latas de tintas: {}, valor total: {}.".format(latas, valor_total))