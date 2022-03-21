#criando arquivos
#arquivo = open('teste.txt', 'w') #Esccreve, mas sobreescreve quando usar novamente
import shutil

def escrever_arquivo(texto):
    #diretorio = '~/PycharmProjects/teste.txt'
    arquivo = open('aluno.txt' 'w') #Escreve, mas não sobreescreve
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open('aluno.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #insere em uma lista
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)  # Separa as notas do nome para fazer a conversao de string para int
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int (i) for i in notas]) / 4 #Função lambda para retornar media
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        #print(lista_notas)

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '~\PycharmProjects\notasAlunos.txt')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '~\PycharmProjects\notasAlunos.txt')

if __name__ == '__main__':
    copia_arquivo('aluno.txt')
    mover_arquivo('aluno.txt')
    #lista_media = media_notas('aluno.txt')
    #print(lista_media)
    # #escrever_arquivo('Primeira linha.\n')
    # aluno = '\nCesar, 9, 5, 5, 9'
    # atualizar_arquivo('aluno.txt', aluno)
    # #ler_arquivo('teste.txt')