soma = 0

for i in range (1,6):
    i = float(input('Digite uma nota: '))
    soma += i
    media = soma / 5

print(f'A soma das notas é: {soma:.2f}.')

if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')
