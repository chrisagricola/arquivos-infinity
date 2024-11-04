nota = int(input('Digite uma nota (até digitar uma negativa): '))
soma = 0
numero = 0

while nota >= 0:
    soma += nota
    numero += 1
    media = soma / numero
    nota = int(input('Digite uma nota (até digitar uma negativa): '))

print(f'A média das notas é: {media}')