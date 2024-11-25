frutas = {'maçã': 5, 'banana': 3, 'laranja': 0}

for fruta, quantidade in frutas.items():
    if quantidade == 0:
        del frutas[fruta]
        break

print(frutas)