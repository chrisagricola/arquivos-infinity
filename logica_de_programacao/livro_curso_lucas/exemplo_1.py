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
# print(s1[0:6])
# print(s1[24:34])
# print(s1[:6])
# print(s1[24:])
# print(s1[:])
# print(s1[::-1])
# print(s1[-1:-34])

# Por que esse último não está dando certo? xxxxxxxxxxxxxx
# De acordo com o ChatGPT, para escrever a frase de trás para frente, eu devo usar o penúltimo código.

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

# ---------------------------------------------------------------------------------------------------------------------------------------

# While

# x = 10

# # while 10 <= x <= 1000:
# #     print(x)
# #     x = x + 10

# while x != 0:
#     print(x)
#     x = x - 1
#     if x == 0:
#         print('Fogo!')

# inicio = int(input('Digite um valor para iniciar a contagem: '))
# final = int(input('Digite um valor para terminar a contagem: '))
# x = inicio
# contador = 0
# while x != final:
#     if x % 3 == 0:
#         print(x)
#     x += 1
#     contador += 1
#     if contador == 30:
#         break

# x = int(input('Digite um número: ')) #2
# y = int(input('Digite outro número: ')) #3
# contador = 0
# soma = 0
# while contador != x:
#     soma += y
#     contador += 1
# print(f'A multiplicação de {x} por {y} é igual a {soma}')

# ----------------------------------------------------------------------------------------------------------------------------------------

# Valores Truthy e Falsy

# soma = 0
# contador = 0
# x = 0
# while True:
#     x = int(input('Digite um número inteiro positivo: '))
#     if x < 0:
#         continue
#     if not x:
#         break
#     soma += x
#     contador += 1
# media = soma / contador

# valores = [0, 1, "", "texto", [], [1, 2], None, False, True]
# for valor in valores:
#     if valor:
#         print(f"{valor} é Truthy")
#     else:
#         print(f"{valor} é Falsy")

# --------------------------------------------------------------------------------------------------------------------------------------------

# For

# for i in range (10, 1001):
#     print(i)

# x = 10

# for i in range (10, 0, -1):
#     print(x)
#     x = x - 1
#     if x == 0:
#         print('Fogo!')

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Varredura de string com for

# frase = "Lógica de Programação e Algoritmos" 

# for i in range(0, len(frase), 1): 
#     print(frase[i],end='')

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Aula 4: 5.1 - Exercícios:

# Exercício 4:

# frase = input('Digite uma frase de 10 a 30 caracteres: ')
# tamanho = len(frase)

# while tamanho < 10 or tamanho > 30:
#     frase = input('Digite uma frase de 10 a 30 caracteres: ')
#     tamanho = len(frase)
# print(f'Com espaços: {frase}')
# print(f'Sem espaços: ', end= '')
# for i in range (0, tamanho, 1):
#     if frase[i] != ' ':
#         print(frase[i], end='')
         
