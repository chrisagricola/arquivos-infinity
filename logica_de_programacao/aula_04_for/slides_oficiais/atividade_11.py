for i in range (1,31):
    i = int(input('Digite um número: '))
    if i > 0 and i % 5 == 0:
        print(f'O número {i} é múltiplo de 5.')
    elif i > 20:
        print('Programa encerrado.')
        break