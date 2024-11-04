numero = int(input('Digite um número de 2 dígitos entre 10 e 99: '))
soma = 0

while numero >= 10:
    soma += numero % 10
    soma += numero // 10
    break


# Solução da Mari:
# while numero >= 10:
#     soma = 0
#     while numero > 0:
#         soma += numero % 10
#         numero //= 10
#         numero = soma

print(f'A soma dos dígitos até ser um único dígito é: {soma}')