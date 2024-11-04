soma = 0

for i in range (1,6):
    i = int(input('Digite um número: '))
    soma += i
    if soma > 100:
        soma -= 5 / 100 * soma
        break

print(f'O seu total é de R$ {soma}.')