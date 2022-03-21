print("## Programa numero decrescente ##")

entrada1 = int(input("Digite o numero: "))
entrada2 = int(input("Digite o numero: "))
entrada3 = int(input("Digite o numero: "))

#quando a primeira entrada for maior e a segunda maior do que a terceira
if entrada1 > entrada2 and entrada1 > entrada3:
    if entrada2 < entrada1 and entrada2 > entrada3:
        if entrada3 < entrada1 and entrada3 < entrada2:
            print(entrada1, entrada2, entrada3)
#Quando a segunda entrada for maior e a primeira menor do que a terceira
if entrada2 > entrada1 and entrada2 > entrada3:
    if entrada1 < entrada2 and entrada1 > entrada3:
        if entrada3 < entrada2 and entrada3 < entrada1:
            print(entrada2, entrada1, entrada3)
#quando a terceira for maior e a segunda maior que a primeira
if entrada3 > entrada1 and entrada3 > entrada2:
    if entrada2 < entrada3 and entrada2 > entrada1:
        if entrada1 < entrada3 and entrada1 < entrada2:
            print(entrada3, entrada2, entrada1)

if entrada3 > entrada1 and entrada3 > entrada2:
    if entrada1 > entrada2 and entrada1 < entrada3:
        if entrada2 < entrada3 and entrada2 < entrada1:
            print(entrada3, entrada1, entrada2)

if entrada1 > entrada2 and entrada1 > entrada3:
    if entrada3 < entrada1 and entrada3 > entrada2:
        if entrada2 < entrada1 and entrada2 < entrada3:
            print(entrada1, entrada3, entrada2)

