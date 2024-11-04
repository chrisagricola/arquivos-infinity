num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('[1] Somar')
print('[2] Multiplicar')
print('[3] Descobrir quem é o maior')
print('[4] Mudar os dois números')
print('[5] Sair do programa')

opcao = int(input('Escolha uma opção: '))

while 1 <= opcao <= 5:
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma dos dois números é: {soma}')
        break
    elif opcao == 2:
        multiplicacao = num1 * num2
        print(f'A multiplicação dos dois números é: {multiplicacao}')
        break
    elif opcao == 3:
        if num1 > num2:
            print('O primeiro número é maior!')
            break
        else: 
            print('O segundo número é maior!')
            break
    elif opcao == 4:
        print(f'O primeiro número é {num2} e o segundo número é {num1}.')
        break
    else:
        print('Programa terminado.')
        break
else:
    print('Opção inválida!')



    