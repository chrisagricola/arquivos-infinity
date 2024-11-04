lista = [[1, 2], [3, 4], [5, 6]]
soma = 0
tamanho = 0
nova_lista = []

for i in lista:
    for numero in i:
        soma += numero
        tamanho += 1
        if tamanho == 2:
            nova_lista.append(soma)
            soma = 0
            tamanho = 0
            continue

print(nova_lista)
