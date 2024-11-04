numeros = [2, 3, 4, 1, 5, 8, 7, 6, 10, 9]
nova_lista = []

for numero in numeros:
    if numero % 2 == 0:
        nova_lista.append(numero)

print(nova_lista)