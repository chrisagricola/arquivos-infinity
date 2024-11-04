contagem = {'a': 3, 'b': 5, 'c': 2}
soma = 0

for valor in contagem.values():
    soma += valor

print(f'A soma dos valores é {soma}.')