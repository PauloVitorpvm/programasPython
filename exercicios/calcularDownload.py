
if __name__ == '__main__':

    print("### TEMPO DOWNLOAD ###")

    entrada = int(input("Digite o tamanho do arquivo em MB: "))
    velocidade = int(input("Digite a velocidade de sua internet em MB: "))


    tempoAproximado = entrada / (velocidade / 8)

    print("tempo aproximado: {}".format(tempoAproximado))