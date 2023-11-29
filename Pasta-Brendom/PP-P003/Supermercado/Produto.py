class Produto:
    codigo = 1

    def __init__(self, nome, preco):
        self.nome = nome.capitalize()
        self.preco = preco
        self.codigo = str(Produto.codigo).zfill(13)
        Produto.codigo += 1