frutas = {'maçã': 5, 'banana': 3, 'laranja': 0}

for quantidade in frutas.values():
    if quantidade == 0:
        for fruta in frutas:
            del frutas[fruta]

print(frutas)