def calcular_desconto(preco: float, porcentagem: int):
    resultado = preco - (porcentagem / 100 * preco)
    return resultado

preco = 4.50
porcentagem = 10
print(f'O preço com desconto é: {calcular_desconto(preco, porcentagem)}')