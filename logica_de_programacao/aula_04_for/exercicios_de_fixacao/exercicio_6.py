palavra = input('Digite uma palavra: ')
vogais = 'AaEeIiOoUu'
conta = 0

for letra in palavra:
    if letra in vogais:
        conta += 1
   
print(f'Total de vogais: {conta}')

# Usando o palavra.count():
# palavra = input('Digite uma palavra em letras minúsculas: ')
# soma = 0

# for letra in palavra:
#   soma += palavra.count('a')
#   soma += palavra.count('e')
#   soma += palavra.count('i')
#   soma += palavra.count('o')
#   soma += palavra.count('e')
#   break

# print(f'Total de vogais: {soma}')