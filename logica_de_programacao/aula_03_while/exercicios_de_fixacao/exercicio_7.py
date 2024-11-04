usuario_resposta = 'chrisagricola'
senha_resposta = '12345'

while True:
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')
    if usuario == usuario_resposta and senha == senha_resposta:
        print('Acesso concedido.')
        break
    print('Usuário ou senha incorretos. Tente novamente.')
    


