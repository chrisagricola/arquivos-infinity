import random
palavras = ['gato', 'gato', 'cachorro', 'cachorro', 'pássaro', 'pássaro', 'cavalo', 'cavalo', 'boi', 'boi']
random.shuffle(palavras)
print('Tente adivinhar onde os pares de animais estão!')
tamanho = len(palavras)

while True:
    palpite = int(input(f'Digite o 1° palpite (de 0 a {tamanho-1}): '))
    print(f'Você escolheu {palavras[palpite]}.')
    palpite2 = int(input(f'Digite o 2° palpite (de 0 a {tamanho-1}): '))          
    print(f'Você escolheu {palavras[palpite2]}.')  
    if palavras[palpite] == palavras[palpite2]:
        print('Você acertou!')
        palavras.remove(palavras[palpite])
        palavras.remove(palavras[palpite2-1])
        tamanho = len(palavras)
    else:
        print('Você errou! Tente novamente!')
    if tamanho == 0:
        print('Você ganhou! Jogo encerrado.')
        break