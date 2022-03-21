horasTrabalhadas = float(input("Quanto você ganha por hora?: "))
numeroHorasMes = float(input("Quantas horas você trabalhou?: "))

salarioBruto = horasTrabalhadas * numeroHorasMes
inss =  salarioBruto * 0.08
ir = salarioBruto * 0.11
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto -(inss + ir + sindicato)

print("### DESCONTOS ###\n")
print("Inss: {}\nIR: {}\nSindicato: {}\n".format(inss, ir, sindicato))
print("### SEU SALÁRIO ###\n")
print("Seu salário bruto: {}".format(salarioBruto))
print("Seu salario liquido: {}".format(salarioLiquido))
