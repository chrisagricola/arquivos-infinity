numero = 1
soma = 0

while numero <= 50:
    if numero % 2 == 0:
       numero += 1
       continue
    else:
        print(numero)
        soma += numero
        numero += 1
       


