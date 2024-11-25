def retornar_faltas(alimentos_desejados: list, subtracao: int, alimentos_no_estoque: list, alimentos_que_faltam: list):
    for i in range (0, len(alimentos_desejados)):
        subtracao = alimentos_no_estoque[i][1] - alimentos_desejados[i][1]
        if subtracao <= 0:
            alimentos_que_faltam.append(alimentos_desejados[i][0])
            alimentos_que_faltam.append(subtracao)
    return alimentos_que_faltam    

alimentos_desejados = [['arroz', 2], ['feijão', 3]]
alimentos_no_estoque = [['arroz', 3], ['feijão', 2], ['carne', 1]]
alimentos_que_faltam = []
resultado = retornar_faltas(alimentos_desejados, 0, alimentos_no_estoque, alimentos_que_faltam)
print(f'Faltam alimentos: {alimentos_que_faltam}')
        
        
            
