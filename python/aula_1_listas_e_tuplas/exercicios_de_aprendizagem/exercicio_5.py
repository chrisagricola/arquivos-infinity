strings = ['Christiane', 'Andréa', 'Gisele', 'Agrícola']
strings_upper = []

for nome in strings:
    nome = nome.upper()
    print(nome)
    strings_upper.append(nome)
    if nome[0] == 'A':
        strings_upper.remove(nome)

print(f'A lista sem os nomes que começam com A é: {strings_upper}')    
    
    
    

    


