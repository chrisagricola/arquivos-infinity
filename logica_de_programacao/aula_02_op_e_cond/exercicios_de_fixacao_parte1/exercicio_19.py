hora = int(input('Digite a hora atual: '))
comparacao = hora < 12 or hora > 18
print(f'A hora atual é antes do meio dia ou depois das 18h? {comparacao}')