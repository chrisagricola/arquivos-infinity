strings = ['sol', 'lua', 'estrela', 'galaxia']
nova_lista = []
contador = 0

for palavra in strings:
    contador = 0
    for letra in palavra:
        contador += 1
        if contador > 4:
            nova_lista.append(palavra)
            break
        else:
            continue
        

print(nova_lista)