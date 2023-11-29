from supermercado.supermecado import Supermercado

def main():
    supermercado = Supermercado('./banco.txt')

    while True:
        print("\nMenu de Opções:")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            supermercado.inserir_produto()
        elif opcao == "2":
            supermercado.excluir_produto()
        elif opcao == "3":
            supermercado.listar_produtos()
        elif opcao == "4":
            supermercado.consultar_preco()
        elif opcao == "0":
            supermercado.salvar_produtos()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
