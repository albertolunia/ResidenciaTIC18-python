import os

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Supermercado:
    def __init__(self, file_path):
        self.file_path = file_path
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        produtos = []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as fd:
                for line in fd.readlines():
                    produto = line.replace('\n', '').split(',')
                    produto = [value.strip() for value in produto]
                    produto = Produto(*produto)
                    produtos.append(produto)
        except FileNotFoundError:
            # Create an empty file if it doesn't exist
            open(self.file_path, 'w').close()

        return produtos

    def inserir_produto(self):
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ").capitalize()
        preco = float(input("Digite o preço do produto: "))

        # Verifica se o código já existe
        codigos_existentes = [produto.codigo for produto in self.produtos]
        if codigo in codigos_existentes:
            print("Erro: Código já existente. Produto não adicionado.")
        else:
            produto = Produto(codigo, nome, preco)
            self.produtos.append(produto)
            print("Produto adicionado com sucesso.")

    def excluir_produto(self):
        codigo = input("Digite o código do produto a ser excluído: ")
        # Filtra os produtos que não têm o código fornecido
        self.produtos = [produto for produto in self.produtos if produto.codigo != codigo]
        print(f"Produto com código {codigo} excluído com sucesso.")

    def listar_produtos(self):
        if not self.produtos:
          print("Nenhum produto cadastrado.")
        else:
          print("\nLista de Produtos:")
          for produto in self.produtos:
            # Ensure that preco is a float
            preco = float(produto.preco) if isinstance(produto.preco, str) else produto.preco
            print("Código: {}, Nome: {}, Preço: R${:.2f}".format(produto.codigo, produto.nome, preco))


    def consultar_preco(self):
        codigo = input("Digite o código do produto para consulta de preço: ")
        # Procura o produto pelo código e exibe o preço
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(f"O preço do produto {produto.nome} é R${produto.preco:.2f}")
                return
        print(f"Produto com código {codigo} não encontrado.")

    def salvar_produtos(self):
        with open(self.file_path, 'w') as fd:
            for produto in self.produtos:
                fd.write(f"{produto.codigo},{produto.nome},{produto.preco}\n")
