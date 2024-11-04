def validar_senha(senha: str):
    calculo = 0
    for letra in senha:
        calculo += 1
        if calculo >= 8:
            for letra in senha:
                if letra in 'AaEeIiOoUu':
                    for letra in senha:
                        if letra not in 'AaEeIiOoUu':
                            for letra in senha:
                                if letra / 1 == letra:
                                    variavel = True
                                    return variavel

print(validar_senha('Chris0303'))