def main():
  listaFuncionarios = []

  carregaDados(listaFuncionarios)
  reajusteDez(listaFuncionarios)
  salvaDados(listaFuncionarios)

def carregaDados(dados):
  with open('Pasta-Brendom/PP-P003/Funcionarios/funcionarios.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        if len(data) == 6:
            funcionario = {
                'nome': data[0],
                'sobrenome': data[1],
                'ano de nascimento': data[2],
                'RG': data[3],
                'ano de admissão': data[4],
                'salário': data[5]
            }
            dados.append(funcionario)
        else:
            print(f"Erro ao ler linha: {line}.")

def salvaDados(dados):
  with open('Pasta-Brendom/PP-P003/Funcionarios/funcionarios.txt', 'w') as file:
    for funcionario in dados:
        salario = format(float(funcionario['salário']), '.2f')
        file.write(f"{funcionario['nome']},{funcionario['sobrenome']},{funcionario['ano de nascimento']},{funcionario['RG']},{funcionario['ano de admissão']},{salario}\n")

def reajusteDez(dados):
  for funcionario in dados:
      funcionario['salário'] = str(float(funcionario['salário']) * 1.1)

if __name__ == "__main__":
    main()
