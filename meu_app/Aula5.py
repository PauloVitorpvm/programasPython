lista = [12, 10, 5, 7]
lista_animal= ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal) #Passando uma lista para uma tupla
print(type(tupla_animal))
print(tupla_animal)
listaNumerica = list(tupla) #Passando uma tupla para uma lista
print(type(listaNumerica))
listaNumerica[0] = 100
print(listaNumerica)
#Tupla imutavel não consegue alterar
#lista mutavel consegue mudar e alterar valores
# #print(lista_animal[1])
# # nova_lista = lista_animal * 3
# # print(nova_lista)
# lista.sort() #ordenar a lista
# lista_animal.sort() #ordenar a lista
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal) #Ordena de forma reversa

# if 'lobo' in lista_animal:
#     print('Existe um gato')
# else:
#     print('Não existe, será incluido na lista')
#     lista_animal.append('lobo') #inseri na lista
#     print(lista_animal)
#
# #lista_animal.pop() #Remove a ultima coisa inserida
# lista_animal.remove('elefante') #Remove passando o nome
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)