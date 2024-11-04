numero = 1
soma = 0

while numero <= 100:
    if numero % 2 == 0:
        soma += numero
        numero += 1
    else:
        numero += 1
        continue
    
print(f'A soma dos números é: {soma}')
