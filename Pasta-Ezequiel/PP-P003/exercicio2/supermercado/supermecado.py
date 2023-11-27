# supermercado.py

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Supermercado:
    def __init__(self, file_path):
        self.produtos = []
        try:   
            with open(file_path, 'r') as fd:
                for line in fd.readlines():  
                    produto = line.replace('\n', '').split(',')
                    produto = [value.strip() for value in produto]
                    produto = Produto(*produto)  
                    self.produtos.append(produto)
        except FileNotFoundError as e:
            print('aqui')
            file = open(file_path, 'w')
            file.close()

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
        print("\nLista de Produtos:")
        print(self.produtos[0].nome)
        #for produto in self.produtos:
            #print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: R${produto.preco:.2f}")

    def consultar_preco(self):
        codigo = input("Digite o código do produto para consulta de preço: ")
        # Procura o produto pelo código e exibe o preço
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(f"O preço do produto {produto.nome} é R${produto.preco:.2f}")
                return
        print(f"Produto com código {codigo} não encontrado.")