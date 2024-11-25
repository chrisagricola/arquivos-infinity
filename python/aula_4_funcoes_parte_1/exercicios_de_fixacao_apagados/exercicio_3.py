def e_positivo(numero: float):
    ele_e_positivo = None
    if numero > 0:
        ele_e_positivo = True
    else:
        ele_e_positivo = False
    return ele_e_positivo

print(e_positivo(2))
print(e_positivo(-40))