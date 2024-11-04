num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
numero = num1

while num1 <= numero <= num2:
    if numero % 2 == 0:
        print(numero)
        numero += 1
    else:
        numero += 1
        continue