import os
import platform
#Dicionário Vazio
produtos = {}

def limparTerminal():
    sistema_operacional = platform.system()

    if sistema_operacional == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def exluirProduto():
    id_produto_para_excluir = input("Digite o ID do produto que deseja excluir: ")

    if id_produto_para_excluir in produtos:
        del produtos[id_produto_para_excluir]
        print(f"Produto com ID {id_produto_para_excluir} removido.")
    else:
        print("ID do produto não encontrado no dicionário.")

def listarProdutos():
    for id_produto, detalhes_produto in produtos.items():
        print(f"ID do Produto: {id_produto}")
        print(f"Nome do Produto: {detalhes_produto['nome']}")
        print(f"Preço do Produto: {detalhes_produto['preco']}")
        print("-----------------------------")

def inserirProduto():
    id_produto = input("Informe o codigo do produto:")
    nome_produto = input("Informe o nome do produto:")
    preco_produto = float(input("Informe o preco do produto:"))

    produtos[id_produto] = {"nome": nome_produto, "preco": preco_produto}

def menu():
    while True:
        print("[1] INSERIR NOVO PRODUTO")
        print("[2] EXCLUIR PRODUTO")
        print("[3] LISTAR PRODUTOS")
        print("[4] CONSULTAR PRDOUTO")
        print("[0] SAIR")
        opcao = int (input("Informe a opcao: "))

        if opcao == 1:
            limparTerminal()
            inserirProduto()
        elif opcao == 2:
            limparTerminal()
            exluirProduto()
        elif opcao == 3:
            limparTerminal()
            listarProdutos()
        elif opcao == 4:
            limparTerminal()
            print("Em construcao")
        elif opcao == 0:
            break
        else:
            limparTerminal()
            print("Opcao invalida")



def main():
    menu()


if __name__ == "__main__":
    main()


