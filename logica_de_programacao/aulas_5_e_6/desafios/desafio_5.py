print('Escolha um número entre 1 e 100 e o computador vai tentar adivinhá-lo.')
import random
palpite = random.randint(1,100)

while True:
    resposta = input(f'O seu número é o {palpite} (maior/menor/correto)? ')
    if resposta == 'correto':
        print('Acertei!')
        break
    elif resposta == 'maior':
        palpite += 1
    else:
        palpite -= 1
