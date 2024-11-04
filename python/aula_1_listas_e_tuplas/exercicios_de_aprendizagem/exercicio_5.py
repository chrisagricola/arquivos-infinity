strings = ['Christiane', 'Andréa', 'Gisele', 'Agrícola']
palavra = ''

for nome in strings:
    print(nome.upper())
    for letra in nome:
        if letra == 'A':
            strings.remove(nome)
            continue


print(strings)

    


