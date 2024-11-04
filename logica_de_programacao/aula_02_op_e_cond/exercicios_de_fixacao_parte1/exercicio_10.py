# condicao_1 = 10 == 10
# condicao_2 = 15 != 15
# print(condicao_1 and condicao_2)
 
idade = int(input('Digite sua idade: '))
comparacao = idade < 18 or idade > 65
mensagem = f'Sua idade é menor do que 18 anos ou maior que 65 anos? {comparacao}'
print(mensagem)