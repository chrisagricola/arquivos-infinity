saque = int(input('Bom dia! Qual é o valor do saque (entre R$ 10 e R$ 600)? ')) #599

divisao_100 = int(saque / 100) #5
divisao_100_resto = int(saque % 100) #99
divisao_50 = int(divisao_100_resto / 50) #1
divisao_50_resto = int(divisao_100_resto % 50) #49
divisao_10 = int(divisao_50_resto / 10) #4
divisao_10_resto = int(divisao_50_resto % 10) #9
divisao_5 = int(divisao_10_resto / 5) #1
divisao_5_resto = int(divisao_10_resto % 5) #4
divisao_1 = int(divisao_5_resto / 1) #4

if 1 <= divisao_100 <= 6:
    print(f'Você receberá {divisao_100} nota(s) de R$ 100.')
if divisao_50 == 1:
    print(f'Você receberá {divisao_50} nota(s) de R$ 50')
if 1 <= divisao_10 <= 9:
    print(f'Você receberá {divisao_10} nota(s) de R$ 10.')
if divisao_5 == 1:
    print(f'Você receberá {divisao_5} nota(s) de R$ 5.')
if 1 <= divisao_1 <= 4:
    print(f'Você receberá {divisao_1} nota(s) de R$ 1.')




    

