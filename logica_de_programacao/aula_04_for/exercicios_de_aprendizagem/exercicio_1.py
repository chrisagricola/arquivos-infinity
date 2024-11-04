num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

for numero in range (1,2):
    media = (num1 + num2 + num3) / 3
    print(f'Média: {media}')

# soma = 0
# for i in range (0,3):
#     nota = float(input(f'Digite a nota {i + 1}: '))
#     soma = soma + nota
# media = soma / 3
# print(f'A média das notas é: {media}')