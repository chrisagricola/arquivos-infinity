lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = []

for numero in lista:
    if numero % 3 == 0 or numero % 5 == 0:
        nova_lista.append(numero)

print(nova_lista)
