itens = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
lista = []

dicionario = {
    'maçã': 0,
    'banana': 0,
    'laranja': 0
}
for item in itens:
    # for fruta, valor in dicionario.items():
        if item in itens:
            print(item in itens)
            dicionario[item] += 1
    
print(dicionario)

