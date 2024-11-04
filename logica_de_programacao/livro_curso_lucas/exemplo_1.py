#print('O resultado da soma de 2 + 3 é: ',2+3)

#print(2+3*3)

#print(4**2/3)

# print((9**2+2)*6-1)

# disciplina = 'Lógica'
# nota = 8.5
# print('Disciplina: ',disciplina,'. Nota: ',nota)

# sentido = 42
# print(f'O sentido da vida é: {sentido}.')

# a = 1
# b = 5
# resposta = a != b
# print(resposta)

# nota = int(input('Qual foi a sua nota? '))
# comparacao = nota >= 7
# print(comparacao)

# ------------------------------------------------------------------------------------------------------------------------------------

# Concatenação
# print('Python'+' '+'-'*5+' '+'C'+' '+'-'*5+' '+'Java'+' '+'-'*5+' '+'PHP')

# ------------------------------------------------------------------------------------------------------------------------------------

# Composição com marcadores de posição
# nota = 8.5
# print('Sua nota é: %.2f' % nota)

# nota = 10.5
# disciplina = 'Algoritmos'
# s1 = 'Sua nota na disciplina %s foi: %.2f.' % (disciplina,nota)
# print(s1)

# ------------------------------------------------------------------------------------------------------------------------------------

# Composição moderna
# nota = 9.3
# disciplina = 'Algoritmos'
# s1 = 'Sua nota na disciplina {} é: {}.' .format(disciplina,nota)
# print(s1)

# ------------------------------------------------------------------------------------------------------------------------------------

# Composição com f-string
# nota = 4.5
# disciplina = 'Algoritmos'
# s1 = f'Sua nota na disciplina {disciplina} é {nota}.'
# # print(s1)

# comida = 'strogonoff'
# nascimento = 1985
# divisao = 1985 / 39
# s1 = f'A minha comida favorita é {comida}, meu ano de nascimento é {nascimento}, que, dividido pela minha idade, dá %.2f.' % (divisao)
# print(s1)

# -------------------------------------------------------------------------------------------------------------------------------------

# Fatiamento
# s1 = 'Lógica de Programação e Algoritmos'
# # print(s1[0:6])
# # print(s1[24:34])
# # print(s1[:6])
# # print(s1[24:])
# print(s1[:])
# print(s1[-1:-34])

# Por que esse último não está dando certo? Quero escrever a frase de trás para frente. xxxxxxxxxxxxxxxxxxxx

# --------------------------------------------------------------------------------------------------------------------------------------

# Tamanho

# nome = 'Christiane Vasconcelos Chaves Agrícola'
# tamanho = len(nome)
# print(f'O tamanho da variável nome é de {tamanho} espaços.')

# --------------------------------------------------------------------------------------------------------------------------------------

# Operadores lógicos/booleanos

# Operador not

# x = True
# y = False
# print(not x)
# print(not y)

# x = 10
# y = 1
# res = not x > y
# print(res)

# Operador and

# x = True
# y = False
# print(x and y)

# x = 10
# y = 1
# z = 5.5
# res = (x > y) and (y == z)
# print(res)

# Operador or

# x = True
# y = False
# print(x or y)

# x = 10
# y = 1
# z = 5.5
# res = (x > y) or (y == z)
# print(res)

# x = 10
# y = 1
# z = 5.5
# res = x > y or not z == y and y != y + z / x
# print(res)
