mes = int(input('Em que mês você está (1 a 12)? '))
if mes in [12, 1, 2]:
    print('Estamos no verão!')
elif mes in [3, 4, 5]:
    print('Estamos no outono!')
elif mes in [6, 7, 8]:
    print('Estamos no inverno!')
elif mes in [9, 10, 11]:
    print('Estamos na primavera!')