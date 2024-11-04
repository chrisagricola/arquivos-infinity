numero1 = int(input('Digite um número inteiro positivo: '))
numero2 = int(input('Digite um segundo número inteiro positivo que forme um intervalo com o primeiro: '))
soma = 0

for numero in range (numero1, numero2+1):
    if numero1 == numero2:
        if numero1 % 2 == 0:
            soma += numero
        else:
            print('Não há numeros pares neste intervalo.')
    else:
        if numero % 2 == 0:
            soma += numero

print(f'A soma dos números pares neste intervalo específico é de {soma}.')
