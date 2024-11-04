usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite sua senha: ')
if 'admin' in usuario and '1234' in senha:
    print('Login realizado com sucesso!')
else: 
    print('Nome de usuário ou senha incorretos.')
