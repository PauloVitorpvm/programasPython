print("### PROGRAMA QUE INFORMA QUE TIPO É O TRIANGULO! ###")

a = float(input("Valor do primeiro lado: "))
b = float(input("Valor do segundo lado: "))
c = float(input("Valor do terceiro lado: "))

if a < b + c and b < c + a and c < a + b:
    print("É triangulo!\n")
    if a == b and a == c and b == c:
        print("Triangulo equilátero!\n")
    if a != b and a != c and b != c:
        print("Triangulo Escaleno")
    if (a == b or a == c or b == c) and (a > b or a > c or b > a or b > c or c > a or c > b):
        print("Triangulo Isóscesle")
else:
    print("Não é triangulo!")