# Calcule 3 áreas:

# 1) 3 * 4
# 2) 19 * 13
# 3) 4 * 10

def calcular_area(altura: float, largura: float):
    area = altura * largura
    return area

altura_1 = 3
largura_1 = 4
area_1 = calcular_area(altura_1, largura_1)
print(f'Área 1: {area_1} m²')

altura_2 = 19
largura_2 = 13
area_2 = calcular_area(19, 13)
print(f'Área 2: {area_2} m²')

altura_3 = 4
largura_3 = 10
area_3 = calcular_area(altura_3, largura_3)
print(f'Área 3: {area_3} m²')