comparacao = 0

def verificar_temperatura(temperatura: int, comparacao: bool):
    comparacao = 18 < temperatura < 25
    return comparacao

temperatura = 30
if comparacao == True:
    print('A temperatura está dentro da faixa de conforto.')
else:
    print('A temperatura está fora da faixa de conforto.')
    