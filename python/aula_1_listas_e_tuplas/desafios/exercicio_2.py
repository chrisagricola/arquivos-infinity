lista = [['-','-', '-'], ['tesouro', '-', '-'], ['-', '-', '-']]

while True:
    linha = int(input('Digite a linha (0, 1 ou 2): '))
    coluna = int(input('Digite a coluna (0, 1 ou 2): '))
    if lista[linha][coluna] == 'tesouro':
        print('Você achou o tesouro!')
        break
    else:
        print('Tente novamente!')
        continue