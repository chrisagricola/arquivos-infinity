ano = int(input('Qual é o ano do seu nascimento? Pessoa 1: '))
ano2 = int(input('Qual é o ano do seu nascimento? Pessoa 2: '))
ano3 = int(input('Qual é o ano do seu nascimento? Pessoa 3: '))
ano4 = int(input('Qual é o ano do seu nascimento? Pessoa 4: '))
ano5 = int(input('Qual é o ano do seu nascimento? Pessoa 5: '))
ano6 = int(input('Qual é o ano do seu nascimento? Pessoa 6: '))
ano7 = int(input('Qual é o ano do seu nascimento? Pessoa 7: '))

maioridade = 0
menoridade = 0

if 2024 - ano >= 18:
    maioridade += 1
else:
    menoridade += 1

if 2024 - ano2 >= 18:
    maioridade += 1
else:
    menoridade += 1

if 2024 - ano3 >= 18:
    maioridade += 1
else:
    menoridade += 1

if 2024 - ano4 >= 18:
    maioridade += 1
else:
    menoridade += 1

if 2024 - ano5 >= 18:
    maioridade += 1
else:
    menoridade += 1

if 2024 - ano6 >= 18:
    maioridade += 1
else:
    menoridade += 1

if 2024 - ano7 >= 18:
    maioridade += 1
else:
    menoridade += 1

soma1 = maioridade
soma2 = menoridade

print(f'Pessoas maiores de idade: {maioridade}')
print(f'Pessoas menores de idade: {menoridade}')