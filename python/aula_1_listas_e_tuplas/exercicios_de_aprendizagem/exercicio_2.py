lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
segunda_lista = []
terceira_lista = []

for numero in lista:
    if numero in segunda_lista:
        segunda_lista.remove(numero)
        terceira_lista.append(numero)
        continue
    if numero in terceira_lista:
        continue
    segunda_lista.append(numero)
       
print(segunda_lista)