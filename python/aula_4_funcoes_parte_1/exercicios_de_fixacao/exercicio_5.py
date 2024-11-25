calorias_por_alimento = [150, 100, 200]

def calcular(calorias_por_alimento: list):
    soma = 0
    for calorias in calorias_por_alimento:
        soma += calorias
    return soma

resultado = calcular(calorias_por_alimento)
print(f'O total de calorias nesses alimentos é: {resultado}')

        
