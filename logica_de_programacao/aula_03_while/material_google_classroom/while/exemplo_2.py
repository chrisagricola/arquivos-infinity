numero_secreto = 7

adivinhar = int(input('Adivinhe o número (entre 1 e 10): '))

while numero_secreto != adivinhar:
    print('Errado, tente novamente!')
    adivinhar = int(input('Adivinhe o número (entre 1 e 10): '))
    
print('Parabéns! Você adivinhou o número secreto!')

