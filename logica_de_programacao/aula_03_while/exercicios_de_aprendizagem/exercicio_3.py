# numero = int(input('Digite um número inteiro (999 para parar): '))
# soma = 0
# total = 0

# while numero != 999:
#     soma += numero
#     total += 1
#     numero = int(input('Digite um número inteiro (999 para parar): '))

# print(f'Total de números digitados: {total}')
# print(f'Soma dos números digitados: %i' % soma)

numero = int(input('Digite um número: '))

while numero != 999:
    soma = 0
    soma = soma + numero
    numero = int(input('Digite um número: '))

print(soma)

