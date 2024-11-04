investimento_inicial = float(input('Digite o valor do investimento inicial (P): '))
juros = int(input('Digite a taxa de juros anual (%): '))
anos = int(input('Digite o número de anos (N): '))
total = 0
investimento = investimento_inicial
print('-----------------------------------------------------------------------')

for i in range (1,anos+1):
    rendimento = investimento * juros / 100
    total = investimento + rendimento
    investimento = total
    
print(f'Após {anos} anos, com um investimento inicial de R$ {investimento_inicial:.2f} e uma taxa de juros anual de {juros}%: O montante final é de R$ {total:.2f}.')