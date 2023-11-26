def criar_dicionario(nome, sobrenome, ano_nascimento, rg, ano_admissao, salario):
    return {
        'nome': nome,
        'sobrenome': sobrenome,
        'ano_nascimento': ano_nascimento,
        'rg': rg,
        'ano_admissao': ano_admissao,
        'salario': salario
    }

def ler_arquivo_e_armazenar_lista(caminho_arquivo):
    lista_empregados = []

    try:
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                empregado = criar_dicionario(*dados)
                lista_empregados.append(empregado)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

    return lista_empregados

def reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        salario_atual = float(empregado['salario'])
        novo_salario = salario_atual + (salario_atual * 0.1)  # Aumento de 10%
        empregado['salario'] = novo_salario

def aplicativo_teste():
    caminho_arquivo = "Pasta-Alessandro/PP-PP003/funcionarios.txt"
    lista_empregados = ler_arquivo_e_armazenar_lista(caminho_arquivo)

    if lista_empregados:
        print(">>> Lista de empregados antes do reajuste: <<<")
        for empregado in lista_empregados:
            print(f"Nome: {empregado.get('nome')}")
            print(f"Sobrenome: {empregado.get('sobrenome')}")
            print(f"Data de Nascimeto: {empregado.get('ano_nascimento')}")
            print(f"RG: {empregado.get('rg')}")
            print(f"Ano Admissao: {empregado.get('ano_admissao')}")
            print(f"Salario: {float(empregado.get('salario')):.2f}")
            print("-------------------------------------")

        reajusta_dez_porcento(lista_empregados)

        print("\nLista de empregados após o reajuste de 10%:")
        for empregado in lista_empregados:
            print(empregado)
    else:
        print("Não foi possível carregar a lista de empregados.")

def main():
    aplicativo_teste()

if __name__ == "__main__":
    main()
