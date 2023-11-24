import os
from Tarefa import *

def limparTerminal():
    sistema_operacional = os.name
    if sistema_operacional == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def salvarTarefas(listaTarefas):
    with open('Pasta-Brendom/PP-P002/ComPersistencia/tarefas.txt', 'w') as file:
        for tarefa in listaTarefas:
            file.write(f"{tarefa.id},{tarefa.descricao},{tarefa.status}\n")

def carregarTarefas():
    lista_tarefas = []
    try:
        with open('Pasta-Brendom/PP-P002/ComPersistencia/tarefas.txt', 'r') as file:
            for line in file:
                dados_tarefa = line.strip().split(',')
                if len(dados_tarefa) >= 3:
                    nova_tarefa = Tarefa(dados_tarefa[1], eval(dados_tarefa[2]))
                    nova_tarefa.id = int(dados_tarefa[0])
                    lista_tarefas.append(nova_tarefa)
                else:
                    print(f"Erro ao ler linha: {line}. Formato incorreto.")
    except FileNotFoundError:
        pass
    return lista_tarefas

# INICIO
listaTarefas = carregarTarefas()

while True:
    limparTerminal()
    print("Menu ToDo:")
    print("1. Criar Tarefa")
    print("2. Concluir Tarefa")
    print("3. Editar Tarefa")
    print("4. Listar Tarefa")
    print("5. Sair")
    opcao = 0
    while(opcao < 1 or opcao > 5):
      try:
        opcao = int(input("Escolha uma opção: "))
      except:
        print("AVISO: Digite um numero!")
      if opcao < 1 or opcao > 5:
        print("AVISO: Opção inválida! Digite entre 1 e 5")

    match opcao:
      case 1:
        limparTerminal()
        print("-- Criacao de Tarefa --")
        novaTarefa = Tarefa(input("Digite a descrição da tarefa: "), False)
        listaTarefas.append(novaTarefa)
        print("Tarefa criada!", end="\n\n")
        input("Pressione Enter para continuar...")
        salvarTarefas(listaTarefas)
      case 2:
        limparTerminal()
        print("-- Conclusão de Tarefa --")
        
        existeTarefaPendente = False
        for tarefa in listaTarefas:
          if tarefa.status == "[]":
            existeTarefaPendente = True
            break
        
        if not existeTarefaPendente:
          print("Nenhuma tarefa pendente!", end="\n\n")
          input("Pressione Enter para continuar...")
        else:
          print("Tarefas pendentes:")
          for tarefa in listaTarefas:
            if tarefa.status == "[]":
              print(f"{tarefa.id} - {tarefa.descricao} {tarefa.status}")
              
          tarefaConcluir = int(input("\nDigite o id da tarefa a ser concluída: "))
          
          for tarefa in listaTarefas:
            if tarefa.id == tarefaConcluir:
              novoStatus = "[x]"
              tarefa.status = novoStatus
              listaTarefas.insert(0, listaTarefas.pop(listaTarefas.index(tarefa)))
              print("Tarefa concluída!", end="\n\n")
              input("Pressione Enter para continuar...")
        salvarTarefas(listaTarefas)
      case 3:
        limparTerminal()
        print("-- Edição de Tarefa --")
        if len(listaTarefas) == 0:
          print("Nenhuma tarefa!", end="\n\n")
          input("Pressione Enter para continuar...")
        else:
          for tarefa in listaTarefas:
            print(f"{tarefa.id} - {tarefa.descricao} {tarefa.status}")
            
          tarefaEditar = int(input("\nDigite o id da tarefa a ser editada: "))
          
          for tarefa in listaTarefas:
            if tarefa.id == tarefaEditar:
              novaDescricao = input("Digite a nova descrição da tarefa: ")
              tarefa.descricao = novaDescricao
              print("Tarefa editada!", end="\n\n")
              input("Pressione Enter para continuar...")
        salvarTarefas(listaTarefas)

      case 4:
        limparTerminal()
        print("-- Lista de Tarefas --")
        if len(listaTarefas) == 0:
          print("Nenhuma tarefa!", end="\n\n")
          input("Pressione Enter para continuar...")
        else:
          for tarefa in listaTarefas:
            print(f"{tarefa.id} - {tarefa.descricao} {tarefa.status}")
          input("\nPressione Enter para continuar...")

      case 5:
        print("Encerrando app...")
        salvarTarefas(listaTarefas)
        break
      
      case _:
          print("AVISO: Opção inválida. Por favor, digite entre 1 e 5.")
