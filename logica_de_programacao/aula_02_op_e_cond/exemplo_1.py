produto = 'Biscoito'
preco = 1.99
quantidade = int(input('Digite a quantidade de pacotes: '))

total = preco * quantidade

# Você comprou [PRODUTO] e o total é [TOTAL]

mensagem = f'Você comprou {produto} e o total é R$ {total}.'
print(mensagem)