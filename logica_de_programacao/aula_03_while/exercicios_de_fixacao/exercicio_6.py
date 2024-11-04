# numero = int(input('Digite um número para exibir sua tabuada: ')) #5
# multiplicacao = 1
# resultado = 0

# while resultado != numero * numero:
#         print(f'{numero} X {multiplicacao} = {numero * multiplicacao}') #5 x 1 = 5
#         resultado = numero * multiplicacao
#         multiplicacao += 1


resultado = 0
multiplicacao = 1

numero = int(input('Digite um número para exibir sua tabuada: '))

while True:
        resposta = numero * numero
        if resultado != resposta:
            print(f'{numero} X {multiplicacao} = {numero * multiplicacao}')
            resultado = numero * multiplicacao
            multiplicacao += 1
    
    



        
        
    