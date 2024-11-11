def converter_real_para_dolar(valor: float, taxa: float):
    resultado = valor / taxa
    return resultado

valor = 100
taxa = 5.50
print(f'A conversão de {valor} reais para dólares é de: USD {converter_real_para_dolar(valor, taxa):.2f}')