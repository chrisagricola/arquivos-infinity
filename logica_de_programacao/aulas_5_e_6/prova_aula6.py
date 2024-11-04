usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite sua senha: ')
usuario_correto = 'cvca'
senha_correta = '1234'

for i in range (1,3):
    if usuario == usuario_correto:
        print('Seja bem vindo(a)!')
        break
    else:
        print(f'Restam {3-i} tentativa(s)!')
        usuario = input('Digite o seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        if i == 2:
            for i in range (0,3):
                print('Acesso bloqueado!')


