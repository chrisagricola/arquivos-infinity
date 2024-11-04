string = input('Escreva uma frase com letras e números: ')
algarismos = '0123456789'
conta = 0

for caractere in string:
    if caractere in algarismos:
        conta += 1

print(f'O número de algarismos nesta frase é: {conta}')