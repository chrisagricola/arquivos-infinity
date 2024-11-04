import random
palavras = ['elefante', 'pássaro', 'peixe', 'cachorro', 'gato']
random.choice(palavras)
contador = 0
palavra_escolhida = random.choice(palavras)
tentativa = ''

while contador <=6:
    chute = input('Tente adivinhar a palavra: ')
    if chute in palavra_escolhida:
        print('Você acertou! A palavra é: ')
        for letra in palavra_escolhida:
            if letra == chute:
                print(letra,end='')
            else:
                letra = '_'
                print(letra,end='')
    else: 
        print('Você errou!')
        continue
    contador += 1