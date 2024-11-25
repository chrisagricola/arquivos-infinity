def procurar_tamanho(busto: int, cintura: int, quadril: int):
    if busto <= 88 and cintura <= 68 and quadril <= 94:
        tamanho = 'P'
    elif 89 < busto <= 94 and 69 < cintura <= 74 and 95 < quadril <= 100:
        tamanho = 'M'
    elif busto >= 95 and cintura >= 75 and quadril >= 101:
        tamanho = 'G'
    return tamanho

resultado = procurar_tamanho(98, 80, 105)
print(f'O tamanho recomendado é: {resultado}')
    