palavra = input('Digite uma palavra: ')
letra1 = '.'

for letra in palavra:
    if letra in letra1:
        print(f'O primeiro caractere que se repete é: {letra}')
    letra1 += letra


    
