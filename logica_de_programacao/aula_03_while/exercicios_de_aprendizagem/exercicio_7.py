frase = input('Digite uma frase: ')
palavras = '.'

for letra in frase:
    if letra in palavras:
        continue
    print(letra, end='')
    palavras += letra