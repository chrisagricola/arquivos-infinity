import random
numero_secreto = random.randint(1,100)

print('O computador escolhe um número aleatório entre 1 e 100. Tente adivinhar qual é!')
chute = int(input('Digite um número: '))

while chute != numero_secreto:
    if chute > numero_secreto:
        print(f'O número é menor que {chute}.')
        chute = int(input('Digite um número: '))
    elif chute < numero_secreto:
        print(f'O número é maior que {chute}.')
        chute = int(input('Digite um número: '))
    else:
        print(f'Parabéns! Você acertou o número secreto: {numero_secreto}!')

        