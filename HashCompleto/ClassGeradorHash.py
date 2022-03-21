import hashlib

class GeradorHash:

    def __init__(self, menu):
        string = input('Digite o texto a ser gerado a hash: ')

        self.menu = int(input('''### MENU = ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o numero do hash a ser gerado: '''))

        if self.menu == 1:
            resultado = hashlib.md5(string.encode('utf-8'))
            print('O hash da string: ', string, 'é', resultado.hexdigest())
        elif self.menu == 2:
            resultado = hashlib.sha1(string.encode('utf-8'))
            print('O hash da string: ', string, 'é', resultado.hexdigest())
        elif self.menu == 3:
            resultado = hashlib.sha256(string.encode('utf-8'))
            print('O hash da string: ', string, 'é', resultado.hexdigest())
        elif self.menu == 4:
            resultado = hashlib.sha512(string.encode('utf-8'))
            print('O hash da string: ', string, 'é', resultado.hexdigest())
        else:
            print('Deu erro, tente novamente')

    def setMenu(self, menu):
        self.menu = menu

    def getMenu(self, menu):
        return self.menu
