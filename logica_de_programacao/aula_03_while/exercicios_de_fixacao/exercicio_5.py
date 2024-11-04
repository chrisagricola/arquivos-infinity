numero = int(input('Digite um número inteiro positivo (digite um número negativo para encerrar): '))
soma = 0

while numero > 0:
    resultado = soma + numero #0+5
    soma = resultado #5
    numero = int(input('Digite um número inteiro positivo (digite um número negativo para encerrar): '))

print(f'Soma dos números positivos digitados: {soma}.')
