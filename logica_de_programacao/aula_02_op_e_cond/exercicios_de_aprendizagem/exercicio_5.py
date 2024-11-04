# salario = float(input('Digite seu salário: '))
# reajuste5 = salario * 5 / 100
# reajuste10 = salario * 10 / 100
# reajuste15 = salario * 15 / 100
# reajuste20 = salario * 20 / 100
# novo_salario5 = salario + reajuste5
# novo_salario10 = salario + reajuste10
# novo_salario15 = salario + reajuste15
# novo_salario20 = salario + reajuste20

# if salario <= 280.00:
#     print(f'O seu salário é: R$ {salario}. O percentual de aumento aplicado será de 20%. O valor do aumento do seu salário é de R$ {reajuste20:.2f}. Seu novo salário será de R$ {novo_salario20:.2f}.')
# elif 280.01 <= salario <=  700.00:
#     print(f'O seu salário é: R$ {salario}. O percentual de aumento aplicado será de 15%. O valor do aumento do seu salário é de R$ {reajuste15:.2f}. Seu novo salário será de R$ {novo_salario15:.2f}.')
# elif 700.01 <= salario <=  1500.00:
#     print(f'O seu salário é: R$ {salario}. O percentual de aumento aplicado será de 10%. O valor do aumento do seu salário é de R$ {reajuste10:.2f}. Seu novo salário será de R$ {novo_salario10:.2f}.')
# else: 
#     print(f'O seu salário é: R$ {salario}. O percentual de aumento aplicado será de 5%. O valor do aumento do seu salário é de R$ {reajuste5:.2f}. Seu novo salário será de R$ {novo_salario5:.2f}.')
# 
# PARA ESPECIFICAR O N° DE CASAS DECIMAIS: COLOCAR {(:) + (.) + (n° de casas decimais)} DEPOIS DA VARIÁVEL QUE VOCÊ QUER ESPECIFICAR.


salario = float(input('Digite seu salário: '))

if salario <= 280.00:
  percentual_aumento = 20
elif salario <= 700.00:
  percentual_aumento = 15
elif salario <= 1500.00:
  percentual_aumento = 10
else:
  percentual_aumento = 5

valor_aumento = salario * percentual_aumento / 100
novo_salario = salario + valor_aumento

print(f'O seu salário é de R$: {salario:.2f}')
print(f'O percentual de aumento aplicado será de {percentual_aumento}%.')
print(f'O valor do aumento do seu salário será de R$: {valor_aumento:.2f}.')
print(f'Seu novo salário será de R$ {novo_salario:.2f}.')