frase = input('Escreva uma frase que termine com ponto final, ponto de exclamação ou ponto de interrogação: ')
palavra = ''

for letra in frase:
    if letra in ' .?!':
        print(palavra)
        palavra = ''
    else:
        palavra += letra