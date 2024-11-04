numero = int(input('Digite um número (até digitar um negativo): '))
soma = 0

while numero >= 0:
    soma += numero
    numero = int(input('Digite números (até digitar um negativo): '))

print(f'A soma dos números positivos foi: {soma}')

