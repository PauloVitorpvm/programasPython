#Criando exceções

lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    # divisao = 10 / 1
    # numero = lista[1]
    # #x = a

    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[i]
    print('fechando arquivo')
   

except ZeroDivisionError:
    print('Não é pssivel realizar divisão por zero')
except ArithmeticError:
    print('Houve um erro aritmético')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')

except Exception as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quanto não ocorre exceção')
finally:
    print('Sempre executa')
    arquivo.close()
