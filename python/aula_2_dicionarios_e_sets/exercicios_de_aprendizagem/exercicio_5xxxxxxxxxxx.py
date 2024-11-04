notas = {'Ana': 8, 'Pedro': 5, 'Luiza': 9, 'João': 4}
novo_dicionario = {}

for valor in notas.values():
    if valor >= 7:
        for nome, nota in notas.items():
            novo_dicionario[nome] = nota
            break


print(novo_dicionario)