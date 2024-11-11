def calcular_calorias(alimento: int, alimentos: str, soma: int):
    soma = 0
    for alimento in alimentos:
        soma += alimentos[alimento]
    return soma

alimentos = {'arroz': 150, 'feijao': 100, 'carne': 200}
resultado = (calcular_calorias(alimentos))
print(resultado)
