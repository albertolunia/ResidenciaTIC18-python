import os

# Lista de tarefas
tarefas = []

# Carregar tarefas do arquivo
if os.path.exists("tarefas.txt"):
    with open("tarefas.txt", "r") as arquivo:
        for linha in arquivo:
            if ";" in linha:
                descricao, realizada = linha.strip().split(";")
                tarefas.append([descricao, realizada == "True"])
            else:
                print(f"Linha inválida encontrada: {linha}")

# Função para listar as tarefas
def listar_tarefas():
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa[0]} [{'x' if tarefa[1] else ' '}]")

# Função para registrar uma nova tarefa
def registrar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append([descricao.capitalize(), False])
    print("Tarefa registrada!!!")

# Função para marcar uma tarefa como realizada
def marcar_tarefa():
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        id = int(input("Digite o ID da tarefa: ")) - 1
        if id >= 0 and id < len(tarefas) and not tarefas[id][1]:
            tarefa = tarefas.pop(id)
            tarefa[1] = True
            tarefas.insert(0, tarefa)
            print("Tarefa marcada como realizada!!!")

# Função para editar uma tarefa
def editar_tarefa():
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        id = int(input("Digite o ID da tarefa: ")) - 1
        if id >= 0 and id < len(tarefas):
            descricao = input("Digite a nova descrição da tarefa: ")
            tarefas[id][0] = descricao.capitalize()
            print("Tarefa editada!!!")

# Loop principal do aplicativo
while True:
    print("\n1. Listar tarefas")
    print("2. Registrar tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        listar_tarefas()
    elif opcao == 2:
        registrar_tarefa()
    elif opcao == 3:
        marcar_tarefa()
    elif opcao == 4:
        editar_tarefa()
    elif opcao == 5:
        break

# Salvar tarefas no arquivo ao sair
with open("tarefas.txt", "w") as arquivo:
    for tarefa in tarefas:
        arquivo.write(f"{tarefa[0]};{tarefa[1]}\n")
