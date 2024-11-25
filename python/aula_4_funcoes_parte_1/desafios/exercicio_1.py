def gerar_senha(repeticoes: int):
    senha = ''
    import random
    caracteres = 'aeiou'
    numeros = '1234567890'
    for i in range (0, repeticoes):
        random.choice(caracteres)
        random.choice(numeros)
        senha += random.choice(caracteres)
        senha += random.choice(numeros)
    return senha

repeticoes = 6
resultado = gerar_senha(repeticoes)
print(f'A senha será: {resultado}')