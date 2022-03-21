print("### CAIXA ELETRONICO ###")

numero = int(input("Digite o valor a ser sacado, sendo valor minimo 10,00R$ e maximo 600,00R$: "))
entrada = numero
notas = 100
total_notas = 0

if entrada <= 600 and entrada >= 10:
    while True:
        if entrada >= notas:
            entrada -= notas
            total_notas += 1
        else:
            if total_notas > 0:
                print('Total de {} notas de R$ {}'.format(total_notas, notas))
            if notas == 100:
                notas = 50
            elif notas == 50:
                notas = 10
            elif notas == 10:
                notas = 5
            elif notas == 5:
                notas = 1
            total_notas = 0
            if entrada == 0:
                break
else:
    print("Só é permitido valores entre 10 ate 600 reais")





