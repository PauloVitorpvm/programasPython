if __name__ == '__main__':

    print("Imprimir a centena, dezena e unidade do numero digitaod")

    numero = int(input("Digite um numero inteiro menor que 1000: "))

    if numero < 1000:
        unidade = numero % 10
        numero = (numero - unidade) / 100

        dezena = numero % 10
        numero = (numero - dezena) / 10

        centena = numero % 10


        #milhar = numero % 10

        dezena = int(dezena)
        centena = int(centena)
        #milhar = int(milhar)

        print(centena, 'centena(s)', dezena, 'dezena(s)', unidade, 'unidade(s)')
