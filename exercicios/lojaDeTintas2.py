cobertura_tinta = 6
capacidade_lata = 18
valor_lata = 80.0
capacidade_galoes = 3.6
valor_galoes = 25.0

tamanho_metros = float(input("Digite o tamanho em m²: "))

qt_tinta = tamanho_metros / cobertura_tinta

apenas_latas = int(qt_tinta / capacidade_lata)
valor_tinta_latas = apenas_latas * valor_lata

if(apenas_latas % capacidade_lata != 0):
     apenas_latas += 1

apenas_galoes = int(qt_tinta / capacidade_galoes)
valor_tinta_galoes = apenas_galoes * valor_galoes

if(apenas_galoes % capacidade_galoes != 0):
     apenas_galoes += 1

print("Tamanho em m²: {}. "
      "quantidade de tinta: {}. "
      "quantidade somente com latas: {}. "
      "quantidades somente com galões: {}.".format(tamanho_metros, qt_tinta, apenas_latas, apenas_galoes))
print("Valor lata: {}\nValor galões: {}".format(valor_tinta_latas, valor_tinta_galoes))