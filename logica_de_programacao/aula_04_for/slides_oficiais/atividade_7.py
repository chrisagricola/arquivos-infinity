palavra = input('Digite uma palavra qualquer: ')
vogais = 'AaEeIiOoUu'
soma = 0

for letra in palavra:
    if letra in vogais:
        soma += 1

print(f'A palavra {palavra} tem {soma} vogais.')
