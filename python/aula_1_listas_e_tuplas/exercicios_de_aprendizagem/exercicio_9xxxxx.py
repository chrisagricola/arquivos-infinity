lista = ['maçã', 'banana', 'cereja']
letras = []
numero = 0

for fruta in lista:
    for letra in fruta:
        numero -= 1
        letras.insert(numero,letra)
    print(letras)
    

# print(s1[-1:-34])
