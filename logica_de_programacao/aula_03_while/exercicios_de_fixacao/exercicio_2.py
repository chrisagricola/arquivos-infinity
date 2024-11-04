numero = float(input('Digite uma nota entre 0 e 10: '))

while numero < 0 or numero > 10:
    numero = float(input('Nota inválida. Por favor, digite uma nota de 0 a 10: '))

print(f'Você digitou uma nota válida, {numero}!')



