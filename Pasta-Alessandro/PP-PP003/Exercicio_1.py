import os
import platform

# Lista de produtos
produtos = []

def limparTerminal():
    sistema_operacional = platform.system()

    if sistema_operacional == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def consultarProduto():
    limparTerminal()
    print(">>> CONSULTAR PRODUTO <<<")
    id_produto_para_consultar = input("Digite o ID do produto que deseja consultar: ")

    produto_encontrado = next((produto for produto in produtos if produto['id'] == id_produto_para_consultar), None)

    if produto_encontrado:
        print(f"ID do Produto: {produto_encontrado['id']}")
        print(f"Nome do Produto: {produto_encontrado['nome']}")
        print(f"Preço do Produto: R$ {produto_encontrado['preco']:.2f}")
    else:
        print("ID do produto não encontrado na lista.")

def excluirProduto():
    limparTerminal()
    print(">>> EXCLUIR PRODUTO <<<")
    id_produto_para_excluir = input("Digite o ID do produto que deseja excluir: ")

    produto_encontrado = next((produto for produto in produtos if produto['id'] == id_produto_para_excluir), None)

    if produto_encontrado:
        produtos.remove(produto_encontrado)
        print(f"Produto com ID {id_produto_para_excluir} removido.")
    else:
        print("ID do produto não encontrado na lista.")

def listarProdutos():
    limparTerminal()
    print(">>> LISTANDO PRODUTOS <<<")

    # Ordena a lista de produtos pelo preço em ordem crescente
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])

    for produto in produtos_ordenados:
        print(f"ID do Produto: {produto['id']}")
        print(f"Nome do Produto: {produto['nome']}")
        print(f"Preço do Produto: R$ {produto['preco']:.2f}")
        print("-----------------------------")

def inserirProduto():
    limparTerminal()
    print(">>> INSERIR PRODUTO <<<")

    id_produto = input("Informe o ID do produto (13 caracteres numéricos): ")

    # Adiciona zero à esquerda se necessário
    id_produto = id_produto.zfill(13)

    if id_produto.isnumeric() and len(id_produto) == 13:
        nome_produto = input("Informe o nome do produto: ").capitalize()
        preco_produto = float(input("Informe o preço do produto: R$ "))

        produtos.append({"id": id_produto, "nome": nome_produto, "preco": preco_produto})
        limparTerminal()
        print("Produto inserido com sucesso!")
    else:
        print("ID do produto inválido.")

def menu():
    while True:
        print(">>> GERENCIAMENTO DE PRODUTOS <<<")
        print("[1] INSERIR NOVO PRODUTO")
        print("[2] EXCLUIR PRODUTO")
        print("[3] LISTAR PRODUTOS")
        print("[4] CONSULTAR PRODUTO")
        print("[0] SAIR")
        opcao = input("Informe a opção: ")

        if opcao == '1':
            limparTerminal()
            inserirProduto()
        elif opcao == '2':
            limparTerminal()
            excluirProduto()
        elif opcao == '3':
            limparTerminal()
            listarProdutos()
        elif opcao == '4':
            limparTerminal()
            consultarProduto()
        elif opcao == '0':
            limparTerminal()
            break
        else:
            limparTerminal()
            print("Opção inválida.")

def main():
    menu()

if __name__ == "__main__":
    main()
