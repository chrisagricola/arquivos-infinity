# palavra = input('Escreva uma palavra: ')

# for letra in palavra:
#     if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U":
#         continue
#     print(letra, end="")


palavra = input('Digite uma frase: ')
vogais = 'aeiou'

for letra in palavra:
    if letra in vogais:
        continue
    print(letra,end='')