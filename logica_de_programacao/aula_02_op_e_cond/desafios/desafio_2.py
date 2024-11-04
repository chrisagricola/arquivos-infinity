numero = int(input('Escolha um número até 1000: ')) #999

divisao_100 = int(numero / 100) #9
divisao_100_resto = int(numero % 100) #99
divisao_10 = int(divisao_100_resto / 10) #9
divisao_10_resto = int(divisao_100_resto % 10) #9
divisao_1 = int(divisao_10_resto / 1) #9

if 0 <= divisao_100 <= 10 or 1 <= divisao_10 <= 9 or 1 <= divisao_1 <= 4:
    print(f'Esse número é composto por {divisao_100} centena(s), {divisao_10} dezena(s) e {divisao_1} unidade(s).')