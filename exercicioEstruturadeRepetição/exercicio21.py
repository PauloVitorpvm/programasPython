if __name__ == '__main__':
    n = int(input("Digite um numero: "))
    lista_primo = [2, 3, 5, 7, 11]

    for i in lista_primo:
        n = n % i
    if n == 0:
        print("O numero é primo")
    else:
        print("O numero não é primo")