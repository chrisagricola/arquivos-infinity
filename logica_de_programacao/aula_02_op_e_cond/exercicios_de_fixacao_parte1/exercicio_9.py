# condicao_1 = 10 == 10
# condicao_2 = 15 != 15
# print(condicao_1 and condicao_2)
 
idade = int(input('Digite sua idade: '))
comparacao = 18 <= idade <= 65 and idade > 21
mensagem = f'Sua idade está entre 18 e 65 anos e é maior que 21 anos? {comparacao}'
print(mensagem)