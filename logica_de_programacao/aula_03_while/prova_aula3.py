numero_escolhido = 3
tentativas = 0

while tentativas < 3:
    chute_usuario = int(input('Tente adivinhar o número que eu escolhi: '))
    if chute_usuario != numero_escolhido:
        print('Não foi desta vez!')
    else:
        print('Acertou, parabéns!')
        break
    tentativas += 1
