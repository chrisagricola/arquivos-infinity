palavra = str(input('Digite uma palavra: '))
vogais = 'AaEeIiOoUu'

for letra in palavra:
    if letra not in vogais:
       break

print(f'A primeira consoante dessa palavra é: {letra}.')



