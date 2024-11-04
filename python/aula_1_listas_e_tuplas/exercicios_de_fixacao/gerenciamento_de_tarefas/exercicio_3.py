tarefas = ['Lavar louça', 'Lavar roupa', 'Passar roupa', 'Varrer o chão']

tirar_tarefa = int(input('Remova uma tarefa da lista (pelo seu índice): '))
tarefas.pop(tirar_tarefa)

print(tarefas)