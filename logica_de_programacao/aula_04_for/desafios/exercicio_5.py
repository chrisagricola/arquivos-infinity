peso1 = float(input('Qual é o seu peso? Pessoa 1: '))
peso2 = float(input('Qual é o seu peso? Pessoa 2: '))
peso3 = float(input('Qual é o seu peso? Pessoa 3: '))
peso4 = float(input('Qual é o seu peso? Pessoa 4: '))
peso5 = float(input('Qual é o seu peso? Pessoa 5: '))

if peso1 > peso2 and peso1 > peso3 and peso1 > peso4 and peso1 > peso5:
    print(f'O maior peso lido é o {peso1}')
elif peso2 > peso1 and peso2 > peso3 and peso2 > peso4 and peso2 > peso5:
    print(f'O maior peso lido é o {peso2}')
elif peso3 > peso1 and peso3 > peso2 and peso3 > peso4 and peso3 > peso5:
    print(f'O maior peso lido é o {peso3}')
elif peso4 > peso1 and peso4 > peso2 and peso4 > peso3 and peso4 > peso5:
    print(f'O maior peso lido é o {peso4}')
else:
    print(f'O maior peso lido é o {peso5}')

if peso1 < peso2 and peso1 < peso3 and peso1 < peso4 and peso1 < peso5:
    print(f'O menor peso lido é o {peso1}')
elif peso2 < peso1 and peso2 < peso3 and peso2 < peso4 and peso2 < peso5:
    print(f'O menor peso lido é o {peso2}')
elif peso3 < peso1 and peso3 < peso2 and peso3 < peso4 and peso3 < peso5:
    print(f'O menor peso lido é o {peso3}')
elif peso4 < peso1 and peso4 < peso2 and peso4 < peso3 and peso4 < peso5:
    print(f'O menor peso lido é o {peso4}')
else:
    print(f'O menor peso lido é o {peso5}')
