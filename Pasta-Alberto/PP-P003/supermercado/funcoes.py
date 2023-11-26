import os

def limparTerminal():
    sistema_operacional = os.name
    if sistema_operacional == 'posix':
        os.system('clear')
    else:
        os.system('cls')
        
def exibir_menu():
    limparTerminal()
    print("Escolha uma das opções abaixo:")
    print("1 - Inserir novo produto")
    print("2 - Excluir produto")
    print("3 - Listar produtos")
    print("4 - Consultar produto")
    print("5 - Sair do programa")

def menu(lista_produtos):
    while True:
        
        exibir_menu()
        
        opcao = int(input("Digite a opção desejada: "))
        
        match opcao:
            case 1:
                print("Insira o código do produto: ", end="")
                codigo = input()
                print("Insira o nome do produto: ", end="")
                nome = input()
                print("Insira o preço do produto: ", end="")
                preco = float(input())
                produto = {
                    "codigo": codigo,
                    "nome": nome,
                    "preco": preco
                }
                inserir_produto(lista_produtos, produto)
            case 2:
                print("Excluir produto")
            case 3:
                listar_produtos(lista_produtos)
            case 4:
                print("Consultar produto")
            case 5:
                print("Saindo do programa")
                break
            case _:
                print("Opção inválida")

def inserir_produto(lista_produtos, produto):
    lista_produtos.append(produto)
    print("\nProduto inserido com sucesso!")
    input()
    
def excluir_produto(codigo):
    pass

def listar_produtos(lista_produtos):
    limparTerminal()
    print("Lista de produtos:")
    for produto in lista_produtos:
        print(produto["codigo"], produto["nome"], produto["preco"])
    input()

def consultar_produto(codigo):
    pass