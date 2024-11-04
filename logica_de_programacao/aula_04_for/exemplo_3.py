carro = int(input('Quantos anos tem o seu carro? '))

if carro <= 3:
    print('Seu carro é novo!')
elif carro <= 5:
    print('Seu carro é seminovo!')
elif carro <= 10:
    print('Seu carro é velho!')
else:
    print('Seu carro é muito velho!')