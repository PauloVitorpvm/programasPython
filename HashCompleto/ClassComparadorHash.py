import hashlib

class ComparadorHash:
    def __init__(self, arquivo1, arquivo2):
        self.arquivo1 = ''
        self.arquivo2 = ''

        hash1 = hashlib.new('ripemd160')

        hash1.update(open(self.arquivo1, 'rb').read())  # comparação do hash, rb o modo de leitura binário

        hash2 = hashlib.new('ripemd160')

        hash1.update(open(self.arquivo2, 'rb').read())

        # Comparando hash1 com hash2
        # funcao digest resume os dados passado pro metodo update
        if hash1.digest() != hash2.digest():
            print(f'O arquivo: {self.arquivo1} é diferente do arquivo: {self.arquivo2}')
            print('O hash do arquivo a.txt é: ', hash1.hexdigest())
            print('O hash do arquivo b.txt é: ', hash2.hexdigest())
        else:
            print(f'O arquivo: {self.arquivo1} é igual ao arquivo: {self.arquivo2}')
            print('O hash do arquivo a.txt é: ', hash1.hexdigest())
            print('O hash do arquivo b.txt é: ', hash2.hexdigest())

    def setArquivo1(self, arquivo1):
        self.arquivo1 = arquivo1

    def setArquivo2(self, arquivo2):
        self.arquivo2 = arquivo2
    #
    # def setHash1(self, hash1):
    #     self.hash1 = hash1
    #
    # def setHash2(self, hash2):
    #     self.hash2 = hash2

    def getArquivo1(self):
        return self.arquivo1

    def getArquivo2(self):
        return self.arquivo2

    # def getHash1(self):
    #     return self.hash1
    #
    # def getHash2(self):
    #     return self.hash2

