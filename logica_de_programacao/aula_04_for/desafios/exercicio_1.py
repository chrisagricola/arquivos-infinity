conta = 0

for numero in range (1,51):
    if numero % 2 == 0:
        continue
    else:
        conta += numero

print(f'A soma de todos os números ímpares entre 1 e 50 é: {conta}')