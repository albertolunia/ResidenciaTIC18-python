import os
import random

def vericar_lista_vazia(lista):
    if len(lista) == 0:
        print("Lista de produtos vazia")
        input("\nPressione ENTER para continuar...")
        return True
    return False

def generate_codigo():
        codigo = ''.join(random.choices('0123456789', k=13))
        return codigo

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

def menu():
    lista_produtos = []
    while True:
        codigo = generate_codigo()
        exibir_menu()
        
        opcao = int(input("\nDigite a opção desejada: "))
        
        match opcao:
            case 1:
                print("\nInsira o nome do produto: ", end="")
                nome = input().capitalize()
                print("Insira o preço do produto: ", end="")
                preco = float(input())
                produto = {
                    "codigo": codigo,
                    "nome": nome,
                    "preco": preco
                }
                inserir_produto(lista_produtos, produto)
            case 2:
                print("\nInsira o codigo do produto que deseja excluir: ", end="")
                codigo = input()
                excluir_produto(codigo, lista_produtos)
            case 3:
                listar_produtos(lista_produtos)
            case 4:
                if vericar_lista_vazia(lista_produtos):
                    continue
                print("\nInsira o codigo do produto que deseja procurar: ", end="")
                codigo = input()
                consultar_produto(codigo, lista_produtos)
            case 5:
                limparTerminal()
                print("\nSaindo do programa\n")
                break
            case _:
                limparTerminal()
                print("\nOpção inválida")
                input("\nPressione ENTER para continuar...")

def inserir_produto(lista_produtos, produto):
    lista_produtos.append(produto)
    print("\nProduto inserido com sucesso!")
    input("\nPressione ENTER para continuar...")

    
def excluir_produto(codigo, lista_produtos):
    limparTerminal()
    if vericar_lista_vazia(lista_produtos):
        return
    
    for produto in lista_produtos:
        if(produto["codigo"] == codigo):
            lista_produtos.remove(produto)
            print("\nProduto removido com sucesso!")
            input("\nPressione ENTER para continuar...")
            return
    
    print("\nProduto não encontrado")
    input("\nPressione ENTER para continuar...")

def listar_produtos(lista_produtos):
    limparTerminal()
    
    if vericar_lista_vazia(lista_produtos):
        return
    
    print("Lista de produtos:\n")
    
    lista_produtos_ordenados = sorted(lista_produtos, key=lambda produto: produto["preco"])
    produtos_exibidos = 0
    
    for produto in lista_produtos_ordenados:
        codigo = produto["codigo"]
        nome = produto["nome"]
        preco = "{:.2f}".format(produto["preco"])
        print(f"Codigo: {codigo}\t| Nome: {nome}\t| Preço: {preco}")
        
        produtos_exibidos += 1
        if produtos_exibidos % 10 == 0:
            input("\nPressione ENTER para continuar...")
            limparTerminal()
            print("Lista de produtos:\n")
    
    input("\nPressione ENTER para continuar...")
    

def consultar_produto(codigo, lista_produtos):
    limparTerminal()
    
    for produto in lista_produtos:
        if(produto["codigo"] == codigo):
            print("\nProduto encontrado\n")
            nome = produto["nome"]
            preco = "{:.2f}".format(produto["preco"])
            print(f"Codigo: {codigo}\t| Nome: {nome}\t| Preço: {preco}")
            input("\nPressione ENTER para continuar...")
            return
    
    print("\nProduto não encontrado")
    input("\nPressione ENTER para continuar...")