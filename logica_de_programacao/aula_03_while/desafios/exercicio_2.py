termos = int(input('Digite o número de termos da série que deseja calcular: '))
dividendo = 1
divisor = 1
soma = 0

print('--------------------------------------------------------------')
print(f'Os primeiros {termos} termos da série são: ')

for i in range (1,termos+1): # (3,4)
    divisao = dividendo / divisor # 3/4 = 0,75 
    print(f'{dividendo}/{divisor} = %.4f' % divisao) # 3/4 = 0,75
    soma += divisao
    dividendo += 1 # 3+1 = 4
    divisor += 2 # 3+2 = 5

print(f'A soma da série é: %.4f' % soma)



