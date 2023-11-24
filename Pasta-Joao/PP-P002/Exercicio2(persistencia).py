def carregar_tarefas():
  try:
    with open("tarefas.txt", "r") as arquivo:
      linhas = arquivo.readlines()
      return [linha.strip().split(",") for linha in linhas]
  except FileNotFoundError:
    return []

def salvar_tarefas(tarefas):
  with open("tarefas.txt", "w") as arquivo:
    for tarefa in tarefas:
      arquivo.write(",".join(tarefa) + "\n")
def criar_tarefa(tarefas):
  descricao = input("Informe a descrição da tarefa: ")
  if(descricao[0].islower()):
    descricao = descricao.capitalize()
    
  nova_tarefa = [str(len(tarefas) + 1),descricao, '[ ]']
  tarefas.append(nova_tarefa)
  print("A tarefa foi registrada com sucesso!")
  
def listar_tarefas(tarefas):
  print("\n===== Lista de tarefas =====\n")
  for tarefa in tarefas:
    print(f"{tarefa[0]}. {tarefa[1]} {tarefa[2]}")


def marcar_tarefa(tarefas):
  print("\n===== Marcar tarefa =====\n")
  for tarefa in tarefas:
    print(f"{tarefa[0]}. {tarefa[1]} {tarefa[2]}")

  id = input("Qual tarefa deseja marcar como concluída?(id) ")
  
  for tarefa in tarefas:
    if(tarefa[0] == id and tarefa[2] == '[ ]'):
      tarefa[2] = '[x]'
      tarefas.remove(tarefa)
      tarefas.insert(0, tarefa)
      print("Tarefa marcada com sucesso!")
      return
    
  print("Tarefa não encontrada!")
  
def editar_tarefa(tarefas):
  print("\n===== Editar tarefa =====\n")
  for tarefa in tarefas:
    print(f"{tarefa[0]}. {tarefa[1]} {tarefa[2]}")

  id = input("\nQual tarefa deseja editar?(id) ")
  
  for tarefa in tarefas:
    if tarefa[0] == id:
      nova_descricao = input("Digite a nova descrição da tarefa: ")
      if nova_descricao[0].islower():
        nova_descricao = nova_descricao.capitalize()

      tarefa[1] = nova_descricao
      print("Tarefa editada!!!")
      return
  print("Tarefa não encontrada.")
  


tarefas = carregar_tarefas()
while True:
  print("\n========Menu de tarefas========\n")
  print("1. Cadastrar tarefa")
  print("2. Listar tarefas")
  print("3. Marcar tarefa como concluída")
  print("4. Editar tarefa")
  print("5. Sair")
  
  opcao = int(input("Escolha uma opção: "))
  
  match opcao:
    case 1:
      criar_tarefa(tarefas)
    case 2:
      listar_tarefas(tarefas)
    case 3:
      marcar_tarefa(tarefas)
    case 4:
      editar_tarefa(tarefas)
    case 5:
      salvar_tarefas(tarefas)
      break
    case _:
      print("Opção inválida!")