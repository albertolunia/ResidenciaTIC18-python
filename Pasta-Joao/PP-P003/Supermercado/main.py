
produtos = []

def criar_produto():
    
  print("\n==== CADASTRAR PRODUTO ====\n")
  while(True):
    codigo = input("Digite o código do produto(13 caracteres numéricos): ")
    codigo = codigo.zfill(13)
    
    if produto_existe(codigo):
        print("Produto com este código já existe, tente novamente!")
        continue
    if len(codigo) != 13 or not codigo.isdigit():
        print("Código inválido! Deve ser uma string numérica de 13 caracteres. Tente novamente!")
        continue
        
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))
    
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco})
    print("Produto cadastrado com sucesso!")
    return
    
def produto_existe(codigo):
  for produto in produtos:
    if produto["codigo"] == codigo:
      return True
  return False
def excluir_produto():
    
  print("\n==== EXCLUIR PRODUTO ====\n")
  codigo = input("Digite o código do produto que deseja excluir: ")
  
  for produto in produtos:
    if produto["codigo"] == codigo:
      produtos.remove(produto)
      print("Produto excluído com sucesso!")
      return
      
  print("Produto não encontrado!")
    
def listar_produtos():
  
  print("\n==== LISTA DE PRODUTOS ====\n")
  
  produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
  paginas = (len(produtos_ordenados) + 9) // 10
  
  for pagina in range(paginas):
    print(f"\n=== Página {pagina + 1} ===")
    inicio = pagina * 10
    fim = inicio + 10
    for produto in produtos_ordenados[inicio:fim]:
      print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")


def consultar_produto():
  
  print("\n==== CONSULTAR PRODUTO ====\n")
  
  codigo = input("Digite o código do produto que deseja consultar: ")
  
  for produto in produtos:
    if produto["codigo"] == codigo:
      print(f"Preço do produto {produto['nome']}: R${produto['preco']:.2f}")
      return
    
  print("Produto não encontrado!")
  
        
def main():
  while(True):
    print("\n==== MENU PRINCIPAL ====\n")
    print("1. Inserir um novo produto")
    print("2. Excluir um produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar o preço de um produto")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    match opcao:
      case "1":
        criar_produto()
      case "2":
        excluir_produto()
      case "3":
        listar_produtos()
      case "4":
        consultar_produto()
      case "0":
        print("Saindo...")
        break
      case _:
        print("Opção inválida! Tente novamente!")

if __name__ == "__main__":
  main()


