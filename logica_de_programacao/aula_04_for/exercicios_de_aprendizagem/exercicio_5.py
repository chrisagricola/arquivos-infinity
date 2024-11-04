string = input('Escreva uma palavra: ')
asterisco = "*"

for letra in string:
    if letra == 'a' or letra == 'A' or letra == 'b' or letra == 'B' or letra == 'c' or letra == 'C':
        print(asterisco,end='')
    else:
        print(letra,end='')

        