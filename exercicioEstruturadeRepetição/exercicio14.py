n = 1
p = 0
i = 0

while n <= 10:
    numero = int(input())
    n + 1
    if numero % 2 == 0:
        numero = p
        p = p + 1
    else:
        numero = i
        i = i + 1

print("Quantidade de numeros pares é: {}".format(p))
print("Quantidade de numeros impares é: {}".format(i))