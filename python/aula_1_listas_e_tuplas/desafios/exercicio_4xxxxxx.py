import random
palavras = ['python', 'gentil', 'programacao', 'computador', 'algoritmo', 'nobre', 'afeto']
palavra_secreta = random.choice(palavras)
palavra = []

while True:
    palpite = input('Tente adivinhar uma letra da palavra secreta: ')
    if palpite in palavra_secreta:
        for letra in palavra_secreta:
            if letra == palpite:
                print(letra)
                palavra.append(letra)
            else:
                print('_')
                palavra.append('_')   
            print(palavra)   
