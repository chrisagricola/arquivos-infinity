def string_vazia(texto: str):
    resultado = None
    if texto == '':
        resultado = True
    else:
        resultado = False
    return resultado

texto = 'Christiane'
print(string_vazia(texto))