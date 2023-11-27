def reajusta_salario(empregados):
  for empregado in empregados:
    empregado['salario'] *= 1.1  
    
def listar_empregados(empregados):
  for empregado in empregados:
    print(f"Nome: {empregado['nome']} {empregado['sobrenome']}")
    print(f"Ano de Nascimento: {empregado['ano_nascimento']}")
    print(f"RG: {empregado['rg']}")
    print(f"Ano de Admissão: {empregado['ano_admissao']}")
    print(f"Salário: R${empregado['salario']:.2f}\n")


def main():
  empregados = []
  
  with open('dados_func.txt', 'r') as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(',')
      empregado = {
        'nome': dados[0],
        'sobrenome': dados[1],
        'ano_nascimento': int(dados[2]),
        'rg': dados[3],
        'ano_admissao': int(dados[4]),
        'salario': float(dados[5])
      }
      empregados.append(empregado)
  
  print("Lista de funcionários antes do reajuste:")
  listar_empregados(empregados)
  
  reajusta_salario(empregados)
  
  print("Lista de funcionários após reajuste:")
  listar_empregados(empregados)
    
    
    
if __name__ == "__main__":
  main()