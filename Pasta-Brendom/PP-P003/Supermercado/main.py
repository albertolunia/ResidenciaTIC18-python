from Produto import *
import os

def main():
    listaProdutos = []
    op = None
    while(op != 0):
        limparTerminal()
        print("==== MENU PRINCIPAL ====", end="\n\n")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")
        op = int(input("> "))

        match op:
            case 1:
                limparTerminal()
                inserirProduto(listaProdutos)
            case 2:
                limparTerminal()
                excluirProduto(listaProdutos)
            case 3:
                limparTerminal()
                listarProdutos(listaProdutos)
            case 4:
                limparTerminal()
                consultarPreco(listaProdutos)
            case 0:
                limparTerminal()
                print("Saindo...")
                break
            case _:
                print("Opcao nao existe! Tente novamente!")
def limparTerminal():
    sistema_operacional = os.name
    if sistema_operacional == 'posix':
        os.system('clear')
    else:
        os.system('cls')
def inserirProduto(lista):
    print("==== CADASTRAR PRODUTO ====")
    novoProduto = Produto(
        input("Nome do novo produto: "), 
        float(input("Preço do novo produto: "))
    )
    if not novoProduto.nome == "" and novoProduto.preco > 0:
        lista.append(novoProduto)
def listarProdutos(lista):
    print("==== LISTAR PRODUTOS ====")
    if(len(lista) == 0):
        print("Nenhum produto cadastrado!")
        input("\nPressione ENTER para voltar...")
    else:
        for cont, produto in enumerate(lista):
            print(produto.codigo, "-", produto.nome, "|", format(produto.preco, ".2f"))
            if(cont % 10 == 0 and cont != 0):
                input("\nPressione ENTER para mostrar mais...")
        input("\nPressione ENTER para voltar...")
def excluirProduto(lista):
    print("==== EXCLUIR PRODUTO ====")
    if(len(lista) == 0):
        print("Nenhum produto cadastrado!")
        input("\nPressione ENTER para voltar...")
    else:
        for produto in lista:
            print(produto.codigo, "-", produto.nome, "|", format(produto.preco, ".2f"))
        codigoExcluir = input("Código do produto a ser excluído: ")
        for cont, produto in enumerate(lista):
            if(codigoExcluir == produto.codigo):
                lista.pop(cont)
                print("Produto excluído com sucesso!")
                input("\nPressione ENTER para voltar...")
                break
def consultarPreco(lista):
    print("==== CONSULTAR PREÇO ====")
    if(len(lista) == 0):
        print("Nenhum produto cadastrado!")
        input("\nPressione ENTER para voltar...")
    else:
        codigoProduto = input("Digite o codigo do produto: ")
        for cont, produto in enumerate(lista):
            if(codigoProduto == produto.codigo):
                limparTerminal()
                print("Produto encontrado:")
                print(produto.nome, "|", format(produto.preco, ".2f"))
                input("\nPressione ENTER para voltar...")
                break

if __name__ == "__main__":
    main()
