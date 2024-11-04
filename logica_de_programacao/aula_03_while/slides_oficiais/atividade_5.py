numero = int(input('Digite um número: '))
contagem = 0

while contagem != numero:
    contagem += 1
    if contagem % 2 != 0:
        print(contagem)
    else:
        continue

