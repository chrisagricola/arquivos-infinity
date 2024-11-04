numero1 = int(input('Digite um número: '))
fatorial = 1

while numero1 >= 1:
    fatorial = fatorial * numero1
    numero1 -= 1
    
print(f'O fatorial desse número é {fatorial}.')
