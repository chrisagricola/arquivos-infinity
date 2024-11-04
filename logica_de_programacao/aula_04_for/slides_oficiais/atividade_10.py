positivos = 0
negativos = 0

for i in range (1,11):
    i = int(input('Digite um número: '))
    if i > 0:
        positivos += 1
    elif i < 0:
        negativos += 1
    else:
        break

print(f'Você digitou {positivos} números positivos e {negativos} números negativos.')