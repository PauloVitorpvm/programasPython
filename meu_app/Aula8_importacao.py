from Aula7_televisao import Televisao
from Aula7_calculadora1 import Calculadora
from Aula8_contador_letras import contador_letras

if __name__ == '__main__':
    televisão = Televisao()
    print(televisão.ligada)
    televisão.power()
    print(televisão.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print('O valor é: {}'.format(contador_letras(lista)))