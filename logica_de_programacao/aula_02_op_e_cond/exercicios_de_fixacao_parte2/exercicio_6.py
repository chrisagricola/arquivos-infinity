idade = int(input('Quantos anos você tem? '))
if idade <= 11:
    print('Você é uma criança!')
elif 12 <= idade <= 17:
    print('Você é um adolescente!')
elif 18 <= idade <= 59:
    print('Você é um adulto!')
else: print('Você é um idoso!') 