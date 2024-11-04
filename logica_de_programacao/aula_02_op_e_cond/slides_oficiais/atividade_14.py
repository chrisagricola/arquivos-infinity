preco = float(input('Qual é o preço original do produto? '))
quantidade = int(input('Qual a quantidade comprada do produto? '))

if quantidade > 10:
    preco -= 10 / 100
    print(f'O preço com desconto é de R$ {preco}')
else:
    print('Você não receberá desconto!')
