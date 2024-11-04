pares = 0
impares = 0

for i in range (1,11):
    i = int(input('Digite um número: '))
    if i % 2 == 0:
        pares += 1
    else: 
        impares += 1

print(f'Você digitou {pares} números pares e {impares} números ímpares.')