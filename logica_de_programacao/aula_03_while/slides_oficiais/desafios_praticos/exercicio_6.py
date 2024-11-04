numero = int(input('Digite um número para começar uma contagem regressiva: '))
             
while numero != 0:
    if numero % 2 == 0:
        print(f'{numero} - número par!')
        numero -= 1
    else:
        print(numero)
        numero -= 1
