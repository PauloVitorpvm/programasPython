pais_a = 80000
taxa_anual_crescimento_a = 0.03
pais_b = 200000
taxa_anual_crescimento_b = 0.015



ano = 0
while pais_a < pais_b:
    pais_a= pais_a + (pais_a * taxa_anual_crescimento_a)
    pais_b = pais_b + (pais_b * taxa_anual_crescimento_b)
    ano = ano + 1

print("Precisaria de {} ano(S) para Pais A ultrapassar ou igualar a "
           "quantidade de habitantes no Pais B se continuar essa taxa de crescimento".format(ano))