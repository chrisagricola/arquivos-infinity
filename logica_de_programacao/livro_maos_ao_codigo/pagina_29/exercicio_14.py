preco = 10.50

if preco < 5:
    print('Preço barato.')
elif 5 <= preco <= 10:
    print('Preço razoável.') 
elif 10 < preco < 25:
    print('Sobrepreço.')
else:
    print('Preço caro.')