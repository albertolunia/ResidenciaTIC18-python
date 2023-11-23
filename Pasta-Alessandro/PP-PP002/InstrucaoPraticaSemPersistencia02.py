# Inicializa a lista de tarefas
tarefas = []

def listar_tarefas():
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}.{tarefa[0]} {'[x]' if tarefa[1] else '[ ]'}")

def registrar_tarefa():
    descricao = input("Digite a descrição da nova tarefa: ")
    if descricao[0].islower():
        descricao = descricao.capitalize()

    tarefas.append([descricao, False])
    print("Tarefa registrada!!!")

def marcar_tarefa_realizada():
    listar_tarefas()
    id_tarefa = int(input("Digite o ID da tarefa a ser marcada como realizada: ")) - 1

    if 0 <= id_tarefa < len(tarefas):
        tarefas[id_tarefa][1] = True
        tarefas.insert(0, tarefas.pop(id_tarefa))
        print("Tarefa marcada como realizada!!!")
    else:
        print("ID de tarefa inválido ou tarefa já realizada.")

def editar_tarefa():
    listar_tarefas()
    id_tarefa = int(input("Digite o ID da tarefa a ser editada: ")) - 1

    if 0 <= id_tarefa < len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        if nova_descricao[0].islower():
            nova_descricao = nova_descricao.capitalize()

        tarefas[id_tarefa][0] = nova_descricao
        print("Tarefa editada com sucesso!!!")
    else:
        print("ID de tarefa inválido.")

#Carrega a lista de tarefas do arquivo
while True:
    print("\nOpções:")
    print("[1] Listar Tarefas")
    print("[2] Registrar Nova Tarefa")
    print("[3] Marcar Tarefa como Realizada")
    print("[4] Editar Tarefa")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_tarefas()
    elif opcao == "2":
        registrar_tarefa()
    elif opcao == "3":
        marcar_tarefa_realizada()
    elif opcao == "4":
        editar_tarefa()
    elif opcao == "0":
        print("Saindo do aplicativo ToDoList. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
