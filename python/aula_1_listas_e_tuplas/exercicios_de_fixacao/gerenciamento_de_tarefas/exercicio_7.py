tarefas = ['Lavar louça', 'Lavar roupa', 'Passar roupa', 'Varrer o chão', 'Limpar o fogão']
opcao = int(input('(1) Adicionar item (2) Remover item (3) Mostrar tarefas pendentes (4) Escolher tarefa concluída (5) Contar tarefas pendentes - Escolha uma opção: '))

if opcao == 1:
    adicionar = input('Escreva uma tarefa para adicioná-la à lista: ')
    tarefas.append(adicionar)
    print(tarefas)
elif opcao == 2:
    remover = int(input('Escolha pelo índice a tarefa que quer remover: '))
    tarefas.pop(remover)
    print(tarefas)
elif opcao == 3:
    print(tarefas)
elif opcao == 4:
    concluida = int(input('Escolha pelo índice uma tarefa para marcá-la como concluída: '))
    print(f'A tarefa {tarefas[concluida]} foi concluída.')
else:
    tamanho = len(tarefas)
    print(f'Número de tarefas pendentes: {tamanho}')
