tarefas = ['[ ] Lavar louça', '[ ] Lavar roupa', '[ ] Passar roupa', '[ ] Varrer o chão', '[ ] Limpar o fogão']
contador = 0
tamanho_da_lista = len(tarefas)
print(tamanho_da_lista)

while contador < tamanho_da_lista:
    remover_tarefa = int(input('Remova uma tarefa pendente pelo seu índice (até digitar 10): '))
    if remover_tarefa != 10:
        tarefas.pop(remover_tarefa)
        print(tarefas)
    else:
        print('Programa encerrado.')
        break
    contador += 1

