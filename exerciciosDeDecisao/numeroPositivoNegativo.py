print("## PROGRAMA VERIFICADOR SE É NEGATIVO OU POSITIVO O NUMERO DIGITADO ##")

digiteNumero = int(input("Digite o numero negativo ou positivo: "))

if digiteNumero > 0:
    print("Numero positivo")
elif digiteNumero == 0:
    print("Numero neutro")
else:
    print("Numero negativo")