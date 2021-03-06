import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!!')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso')

    Hostalvo = input('Digite o Host ou ip a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((Hostalvo, int(PortaAlvo)))
        print('Cliente TCP conectado com Sucesso no Host: ' + Hostalvo + 'e na Porta: ' + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possivel conectar no Host: ', + Hostalvo + 'e na Porta' + PortaAlvo)
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == "__main__":
    main()
