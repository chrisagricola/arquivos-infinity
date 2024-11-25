def somar_numeros(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

soma_1 = somar_numeros(2, 4, 6)
print(soma_1)