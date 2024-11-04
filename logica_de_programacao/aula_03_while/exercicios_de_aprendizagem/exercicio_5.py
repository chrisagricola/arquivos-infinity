numero = int(input('Digite um número de 3 algarismos: '))
soma = 0

soma += numero // 100 # 1
soma2 = numero % 100 # 23
soma3 = soma2 // 10 # 2
soma4 = soma2 % 10 # 3

print(f'O número com cada algarismo duplicado é: {soma}{soma}{soma3}{soma3}{soma4}{soma4}.')




