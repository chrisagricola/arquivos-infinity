resposta = 8

chute_usuario = int(input('Digite um número inteiro: '))

while chute_usuario != resposta:
    print('Você errou!')
    chute_usuario = int(input('Digite um número inteiro: '))

print('Você acertou!')