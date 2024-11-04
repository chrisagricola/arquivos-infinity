numero = int(input('Digite um número para ver sua tabuada (de 1 a 10): '))
multiplicacao = 0
algarismo = 1

while multiplicacao != 10 * numero: 
    multiplicacao = numero * algarismo
    print(f'{numero} x {algarismo} = {multiplicacao}')
    algarismo += 1


