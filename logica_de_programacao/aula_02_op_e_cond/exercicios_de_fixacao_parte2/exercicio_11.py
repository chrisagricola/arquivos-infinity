idade = int(input('Quantos anos você tem? '))
if idade < 16:
    print('Não vota')
elif 18 <= idade <= 70:
    print('Voto obrigatório')
else:
    print('Voto facultativo')
 