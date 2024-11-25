def validar_senha(senha: str):
    parametro = ''
    for caractere in senha:
        vogais = 'AaEeIiOoUu'
        consoantes = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvXxYyWwZz'
        numeros = '1234567890'
        if caractere in vogais:
            parametro = True
        elif caractere in consoantes:
            parametro = True
        elif caractere in numeros:
            parametro = True
        else:
            parametro = False
    if len(senha) >= 8:
        parametro = True
    else:
        parametro = False
    return parametro
        

senha = 'Chris0303'
resultado = validar_senha(senha)
print(resultado)
