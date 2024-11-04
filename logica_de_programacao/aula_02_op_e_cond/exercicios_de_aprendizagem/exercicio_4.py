produto1 = float(input('Qual o preço do 1° produto? '))
produto2 = float(input('Qual o preço do 2° produto? '))
produto3 = float(input('Qual o preço do 3° produto? '))

if produto1 < produto2 and produto1 < produto3:
    print('Você deve comprar o 1° produto!')
elif produto2 < produto1 and produto2 < produto3:
    print('Você deve comprar o 2° produto!')
elif produto3 < produto1 and produto3 < produto2:
    print('Você deve comprar o 3° produto!')