n = int(input('Escreva um número: '))
fatorial = 1

for i in range (1,n+1):
    fatorial = fatorial * i

print(f'O fatorial do número {n} é: {fatorial}')