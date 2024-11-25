notas = {'Ana': 8, 'Pedro': 5, 'Luiza': 9, 'João': 4}
novo_dicionario = {}

for nome, valor in notas.items():
    if valor >= 7:
        novo_dicionario[nome] = valor

print(novo_dicionario)