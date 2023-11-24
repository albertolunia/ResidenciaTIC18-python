tarefas = []

def criar_tarefa():
  descricao = input("Informe a descrição da tarefa: ")
  if(descricao[0].islower()):
    descricao = descricao.capitalize()
    
  nova_tarefa = {
        'id': len(tarefas) + 1,
        'descricao': descricao,
        'status': '[ ]'
    }
  tarefas.append(nova_tarefa)
  print("A tarefa foi registrada com sucesso!")
  
def listar_tarefas():
  print("\n===== Lista de tarefas =====\n")
  for tarefa in tarefas:
    print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")


def marcar_tarefa():
  print("\n===== Marcar tarefa =====\n")
  for tarefa in tarefas:
    print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")

  id_tarefa = int(input("Qual tarefa deseja marcar como concluída?(id) "))
  
  for tarefa in tarefas:
    if(tarefa['id'] == id_tarefa and tarefa['status'] == '[ ]'):
      tarefa['status'] = '[x]'
      tarefas.remove(tarefa)
      tarefas.insert(0, tarefa)
      print("Tarefa marcada com sucesso!")
      return
    
  print("Tarefa não encontrada!")
  
def editar_tarefa():
  print("\n===== Editar tarefa =====\n")
  for tarefa in tarefas:
    print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")

  id_tarefa = int(input("Qual tarefa deseja editar?(id) "))
  
  for tarefa in tarefas:
    if(tarefa['id'] == id_tarefa):
      
      nova_descricao = input("Nova descrição: ")
      if(nova_descricao[0].islower()):
        nova_descricao = nova_descricao.capitalize()
        
      tarefa['descricao'] = nova_descricao
      print("Tarefa editada com sucesso!")
      return  
  print("Tarefa não encontrada!")
  

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
      criar_tarefa()
    case 2:
      listar_tarefas()
    case 3:
      marcar_tarefa()
    case 4:
      editar_tarefa()
    case 5:
      break
    case _:
      print("Opção inválida!")