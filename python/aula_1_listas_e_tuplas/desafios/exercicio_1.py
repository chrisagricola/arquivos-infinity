import random
tupla = tuple(range(1, 11))
numero_secreto = random.choice(tupla)
print('Bem vindo(a) ao jogo de adivinhação!')

for i in range (1, 11):
    palpite = int(input('Escolha um número de 1 a 10: '))
    if palpite == numero_secreto:
        print('Parabéns! Você acertou o número!')
        break
    elif palpite > numero_secreto:
        print('o número é menor que o seu palpite!')
        continue
    else: 
        print('O número é maior que o seu palpite!')
        continue
