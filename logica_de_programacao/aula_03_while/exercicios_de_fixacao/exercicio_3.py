usuario = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

while senha == usuario:
    print('Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.')
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

print('Cadastro realizado com sucesso!')
