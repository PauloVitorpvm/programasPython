
#União de conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
#interseção de conjuntos
conjunto_intercesecao = conjunto.intersection(conjunto2)
print(conjunto_intercesecao)
#Diferença de conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca)
#Diferença simetrica
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_dif_simetrica)
#pertinencia
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)
# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)