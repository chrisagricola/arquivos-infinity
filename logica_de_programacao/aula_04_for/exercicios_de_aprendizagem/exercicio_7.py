frase = input('Escreva uma frase: ')
palavra = ''

for letra in frase:
    if letra not in ' ':
        palavra += letra

print(palavra)
        


