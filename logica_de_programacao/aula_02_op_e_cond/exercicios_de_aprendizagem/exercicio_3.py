pergunta1 = input('Telefonou para a vítima? ')
pergunta2 = input('Esteve no local do crime? ')
pergunta3 = input('Mora perto da vítima? ')
pergunta4 = input('Devia para a vítima? ')
pergunta5 = input('Já trabalhou com a vítima? ')

if pergunta1 == 'Sim':
    pergunta1 = int(1)
else:
    pergunta1 = int(0)

if pergunta2 == 'Sim':
    pergunta2 = int(1)
else:
    pergunta2 = int(0)

if pergunta3 == 'Sim':
    pergunta3 = int(1)
else:
    pergunta3 = int(0)

if pergunta4 == 'Sim':
    pergunta4 = int(1)
else:
    pergunta4 = int(0)

if pergunta5 == 'Sim':
    pergunta5 = int(1)
else:
    pergunta5 = int(0)

if pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5 == 2:
    print('Essa pessoa é suspeita!')
elif 3 <= pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5 <= 4:
    print('Essa pessoa é cúmplice!')
elif  pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5 == 5:
    print('Essa pessoa é assassina!')
else:
    print('Essa pessoa é inocente!')




