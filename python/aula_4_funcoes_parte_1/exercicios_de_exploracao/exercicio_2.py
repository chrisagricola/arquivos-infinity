def verificacao(ano_1: str, ano_2: str, mes_1: str, mes_2: str, dia_1: str, dia_2: str):
    ano_atual = int(ano_1)
    ano_vencimento = int(ano_2)
    mes_atual = int(mes_1)
    mes_vencimento = int(mes_2)
    dia_atual = int(dia_1)
    dia_vencimento = int(dia_2)    
    subtracao_ano = ano_vencimento - ano_atual 
    subtracao_mes = mes_vencimento - mes_atual 
    subtracao_dia = dia_vencimento - dia_atual 
    if subtracao_ano < 0 and subtracao_mes < 0 and subtracao_dia < 0:
        resultado = 'O produto está vencido!'
    elif subtracao_ano >= 0 and subtracao_mes < 0 and subtracao_dia < 0:
        resultado = 'O produto está vencido!'
    elif subtracao_ano >= 0 and subtracao_mes >= 0 and subtracao_dia < 0:
        resultado = 'O produto está vencido!'
    else:
        resultado = 'O produto ainda está bom para consumo!'
    return resultado

data_atual = '2024-11-12'
data_vencimento = '2024-11-13'
ano_1, mes_1, dia_1 = data_atual.split('-')
ano_2, mes_2, dia_2 = data_vencimento.split('-')
resposta = verificacao(ano_1, ano_2, mes_1, mes_2, dia_1, dia_2)
print(resposta)

