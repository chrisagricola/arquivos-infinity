import random
numero_secreto = random.randint(1,20)

while True:
    numero_chutado = int(input('Tente adivinhar o número secreto entre 1 e 20: '))
    if numero_secreto < numero_chutado:
        print('O número secreto é menor!')
    elif numero_secreto > numero_chutado:
        print('O número secreto é maior!')
    else:
        print('Você acertou!')
        break
    

