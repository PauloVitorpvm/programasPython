a = int (input('Entre com o primerio valor: '))
b = int (input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('soma: {soma}. '
      '\nsubtração: {sub}. '
      '\nMultiplicacao: {mult}. '
      '\nDivisao: {div}.'
      '\nResto: {res}'.format(soma=soma,
                              sub=subtracao,
                              mult=multiplicacao,
                              div=divisao,
                              res=resto))


# print('soma: ' + str(soma))
# print('subtracao' + str(subtracao))
# print(multiplicacao)
# print(int(divisao))
# print(resto)
