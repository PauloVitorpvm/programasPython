nome = str(input("Digite seu nome: "))
while nome:
    if len(nome) >= 3:
        break
    else:
        print("Valor tem que ser mais de 3 caracteres")
        nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade:
    if idade < 150 and idade >= 0:
        #print("Idade: {}".format(idade))
        break
    else:
        print("Valor invalido!")
        idade = int(input("Digite sua idade: "))

salario = float(input("Sálario: "))
while salario:
    if salario > 0:
        #print("Salario: {}".format(salario))
        break
    else:
        print("valor invalido!")
        salario = float(input("Sálario: "))

sexo = input("'f' para feminino ou 'm' para masculino: ")
while sexo:
    if sexo == 'f':
        sexo = 'Feminino'
        #print("Sexo femino")
        break
    elif sexo == 'm':
        sexo = 'Masculino'
        #print("Sexo masculino")
        break
    else:
        print("valor invalido!")
        sexo = input("'f' para feminino ou 'm' para masculino: ")

estado_civil = input("Estado civil: \n's' para solteiro(a)\n'c' para casado(a)\n'v' para viuvo(a)\n'd' para divociado(a): ")
while estado_civil:
    if estado_civil == 's':
        estado_civil = 'Solteiro(a)'
        #print("Solteiro(a)")
        break
    elif estado_civil == 'c':
        estado_civil = 'Casado(a)'
        #print("Casado(a)!")
        break
    elif estado_civil == 'v':
        estado_civil = 'Viuvo(a)'
        #print("Viuvo(a)")
        break
    elif estado_civil == 'd':
        estado_civil = 'Divorciado(a)'
        #print("Divorciado(a)")
        break
    else:
        #print("Valor invalido!")
        estado_civil = input(
            "Estado civil: 's' para solteiro(a)\n'c' para casado(a)\n'v' para viuvo(a)\n'd' para divociado(a): ")





print("Nome: {}\nIdade: {}\nSalario: {}\nSexo: {}\nEstado civil: {}".format(nome, idade, salario, sexo, estado_civil))