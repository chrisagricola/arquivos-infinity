import random
opcoes = ['pedra', 'papel', 'tesoura']
escolha_computador = random.choice(opcoes)

while True:
    
    escolha_usuario = input('Escolha pedra, papel ou tesoura: ')
    
    if escolha_computador == 'pedra' and escolha_usuario == 'papel':
        print(f'A escolha do computador foi {escolha_computador}. Você ganhou!')
    elif escolha_computador == 'pedra' and escolha_usuario == 'tesoura':
        print(f'A escolha do computador foi {escolha_computador}. Você perdeu!')
    elif escolha_computador == 'pedra' and escolha_usuario == 'pedra':
        print(f'A escolha do computador foi {escolha_computador}. Deu empate!')
    elif escolha_computador == 'papel' and escolha_usuario == 'tesoura':
        print(f'A escolha do computador foi {escolha_computador}. Você ganhou!')
    elif escolha_computador == 'papel' and escolha_usuario == 'pedra':
        print(f'A escolha do computador foi {escolha_computador}. Você perdeu!')
    elif escolha_computador == 'papel' and escolha_usuario == 'papel':
        print(f'A escolha do computador foi {escolha_computador}. Deu empate!')
    elif escolha_computador == 'tesoura' and escolha_usuario == 'pedra':
        print(f'A escolha do computador foi {escolha_computador}. Você ganhou!')
    elif escolha_computador == 'tesoura' and escolha_usuario == 'papel':
        print(f'A escolha do computador foi {escolha_computador}. Você perdeu!')
    elif escolha_computador == 'tesoura' and escolha_usuario == 'tesoura':
        print(f'A escolha do computador foi {escolha_computador}. Deu empate!')
    
    novamente = input('Você quer jogar novamente (sim/não)? ')
    
    if novamente == 'sim':
        continue
    else:
        print('Jogo encerrado.')
        break
        
    
