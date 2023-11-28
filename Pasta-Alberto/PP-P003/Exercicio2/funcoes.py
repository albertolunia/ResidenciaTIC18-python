import os
from datetime import datetime as dt

ARQUIVO_COLABORES = "Pasta-Alberto\PP-P003\Exercicio2\colaboradores.txt"

def carregar_colaboradores():
    colaboradores = []
    if os.path.exists(ARQUIVO_COLABORES):
        with open(ARQUIVO_COLABORES, "r") as arquivo:
            for linha in arquivo:
                print(linha)
                dados = linha.strip().split(",")
                codigo = int(dados[0].strip())
                nome = dados[1].strip()
                data_nascimento = dados[2].strip()
                rg = dados[3].strip()
                data_admissao = dados[4].strip()
                salario = float(dados[5].strip())
                
                colaborador = {
                    "codigo": codigo,
                    "nome": nome,
                    "data_nascimento": data_nascimento,
                    "rg": rg,
                    "data_admissao": data_admissao,
                    "salario": salario
                }
                
                colaboradores.append(colaborador)
    return colaboradores

def salvar_colaboradores(lista_colaboradores):
    with open(ARQUIVO_COLABORES, "w") as arquivo:
        for colaborador in lista_colaboradores:
            arquivo.write(f"{colaborador['codigo']},{colaborador['nome']},{colaborador['data_nascimento']},{colaborador['rg']},{colaborador['data_admissao']},{colaborador['salario']}\n")

def limparTerminal():
    sistema_operacional = os.name
    if sistema_operacional == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def menu():
    lista_colaboradores = carregar_colaboradores()
    if len(lista_colaboradores) > 0:
        codigo = lista_colaboradores[-1]["codigo"]
    else:
        codigo = 0
        
    while True:
        salvar_colaboradores(lista_colaboradores)
        exibir_menu()
        opcao = int(input("\nDigite a opção desejada: "))
        
        match opcao:
            case 1:
                print("\nInsira o nome do colaborador: ", end="")
                nome = input().capitalize()
                print("Insira a data de nascimento do colaborador(dd/mm/yyyy): ", end="")
                try:
                    data_nascimento = dt.strptime(input(), "%d/%m/%Y").strftime("%d/%m/%Y")
                except ValueError:
                    print("\nData inválida!")
                    input("\nPressione ENTER para continuar...")
                    continue
                print("Insira o rg do colaborador ", end="")
                rg = input()
                print("Insira a data de admissão do colaborador(dd/mm/yyyy): ", end="")
                try:
                    data_admissao = dt.strptime(input(), "%d/%m/%Y").strftime("%d/%m/%Y")
                except ValueError:
                    print("\nData inválida!")
                    input("\nPressione ENTER para continuar...")
                    continue
                print("Insira o salario do colaborador: ", end="")
                salario = float(input())
                codigo = codigo + 1
                colaborador = {
                    "codigo": codigo,
                    "nome": nome,
                    "data_nascimento": data_nascimento,
                    "rg": rg,
                    "data_admissao": data_admissao,
                    "salario": salario
                }
                inserir_colaborador(lista_colaboradores, colaborador)
            case 2:
                print("\nInsira o codigo do colaborador que deseja excluir: ", end="")
                codigo = int(input())
                excluir_colaborador(codigo, lista_colaboradores)
            case 3:
                listar_colaboradores(lista_colaboradores)
            case 4:
                print("\nInsira o codigo do colaborador que deseja procurar: ", end="")
                codigo = int(input())
                consultar_colaborador(codigo, lista_colaboradores)
            case 5:
                if vericar_lista_vazia(lista_colaboradores):
                    continue
                reajusta_dez_porcento(lista_colaboradores)
            case 6:
                limparTerminal()
                print("\nSaindo do programa\n")
                break
            case _:
                print("\nOpção inválida!")
                input("\nPressione ENTER para continuar...")

def exibir_menu():
    limparTerminal()
    print("1 - Inserir colaborador")
    print("2 - Excluir colaborador")
    print("3 - Listar colaboradores")
    print("4 - Consultar colaborador")
    print("5 - Reajustar salário de todos os colaboradores em 10%")
    print("6 - Sair")

def inserir_colaborador(lista_colaboradores, colaborador):
    lista_colaboradores.append(colaborador)
    print("\nColaborador inserido com sucesso!")
    input("\nPressione ENTER para continuar...")
    
def excluir_colaborador(codigo, lista_colaboradores):
    limparTerminal()
    if vericar_lista_vazia(lista_colaboradores):
        return
    
    for colaborador in lista_colaboradores:
        if(colaborador["codigo"] == codigo):
            lista_colaboradores.remove(colaborador)
            print("\nColaborador removido com sucesso!")
            input("\nPressione ENTER para continuar...")
            return
    
    print("\nColaborador não encontrado!")
    input("\nPressione ENTER para continuar...")

def listar_colaboradores(lista_colaboradores):
    
    limparTerminal()
    
    if vericar_lista_vazia(lista_colaboradores):
        return
    
    print("\nLista de colaboradores:")
    produtos_exibidos = 0
    
    for colaborador in lista_colaboradores:
        print(f"\nCódigo: {colaborador['codigo']}")
        print(f"Nome: {colaborador['nome']}")
        print(f"Data de nascimento: {colaborador['data_nascimento']}")
        print(f"RG: {colaborador['rg']}")
        print(f"Data de admissão: {colaborador['data_admissao']}")
        print(f"Salário: {colaborador['salario']}")
        produtos_exibidos += 1
        
        if produtos_exibidos % 10 == 0:
            input("\nPressione ENTER para continuar...")
            limparTerminal()
            print("Lista de colaboradores:\n")
            
    input("\nPressione ENTER para continuar...")
    
def consultar_colaborador(codigo, lista_colaboradores):
    limparTerminal()
    
    if vericar_lista_vazia(lista_colaboradores):
        return

    for colaborador in lista_colaboradores:
        if(colaborador['codigo'] == codigo):
            print(f"\nCódigo: {colaborador['codigo']}")
            print(f"Nome: {colaborador['nome']}")
            print(f"Data de nascimento: {colaborador['data_nascimento']}")
            print(f"RG: {colaborador['rg']}")
            print(f"Data de admissão: {colaborador['data_admissao']}")
            print(f"Salário: {colaborador['salario']}")
            input("\nPressione ENTER para continuar...")
            return
    
    print("\nColaborador não encontrado!")
    input("\nPressione ENTER para continuar...")

def reajusta_dez_porcento(lista_colaboradores):
    limparTerminal()
    for index, colaborador in enumerate(lista_colaboradores):
        lista_colaboradores[index]["salario"] *= 1.1
    print("\nSalários reajustados com sucesso!")
    input("\nPressione ENTER para continuar...")
    
def vericar_lista_vazia(lista):
    if len(lista) == 0:
        print("Lista de produtos vazia")
        input("\nPressione ENTER para continuar...")
        return True
    return False