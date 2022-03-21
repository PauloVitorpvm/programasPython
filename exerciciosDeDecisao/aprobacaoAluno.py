if __name__ == '__main__':
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 9:
        print("PARABENS APROVADO! \nMedia de: {}\nNota: A".format(media))
    elif media >= 7.5 and media < 9:
        print("PARABENS APROVADO! \nMedia de: {}\nNota: B".format(media))
    elif media >= 6 and media < 7.5:
        print("PARABENS APROVADO! \nMedia de: {}\nNota: C".format(media))
    elif media >= 4 and media < 6:
        print("REPROVADO! \nMedia de: {}\nNota: D".format(media))
    elif media <= 4:
        print("REPROVADO! \nMedia de: {}\nNota: E".format(media))
