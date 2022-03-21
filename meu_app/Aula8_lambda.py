contado_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contado_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(8, 4))


calculadora = {
    'soma': lambda a, b: a + b,A
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}
print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print(soma(1, 50))
print((multiplicacao(10, 2)))