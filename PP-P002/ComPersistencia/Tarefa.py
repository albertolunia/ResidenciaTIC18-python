class Tarefa:
  id = 1
  def __init__(self, descricao, status):
    self.id = Tarefa.id
    Tarefa.id += 1
    self.descricao = descricao.capitalize()
    if status:
      self.status = "[x]"
    else:
      self.status = "[]"
  