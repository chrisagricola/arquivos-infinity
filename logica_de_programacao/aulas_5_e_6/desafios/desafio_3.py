controle = ''
contador = 0
print('Conte de 1 a 35, de um em um. Se o número for múltiplo de 3, digitar "Fizz". Se for múltiplo de 5, digitar "Buzz". Se for múltiplo de 3 e 5, digitar "Fizzbuzz".')

for i in range (1,36):
    numero = input('Faça a contagem: ')
    if i % 3 == 0 and i % 5 == 0:
        controle = 'Fizzbuzz'
        if numero == controle:
            continue
        else:
            print('Você errou.')
            break
    elif i % 5 == 0:
        controle = 'Buzz'
        if numero == controle:
            continue
        else:
            print('Você errou.')
            break
    elif i % 3 == 0:
        controle = 'Fizz'
        if numero == controle:
            continue
        else:
            print('Você errou.')
            break
    else:
        inteiro = int(numero)
        if i == inteiro:
            continue
        else:
            print('Você errou.')
            break

print('Fim de jogo.')

