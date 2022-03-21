print("Programa que não pdoe senha igual o nome")

nome = input("Digite o nome: ")
senha = input("Digite a senha: ")
while nome == senha:
    print("Não pode colocar a senha igual o nome!")
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")

print("Nome diferente da senha!")