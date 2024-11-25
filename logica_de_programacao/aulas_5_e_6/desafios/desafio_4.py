import random
operador = random.choice(['+', '-', '*', '/'])
contador = 0

print('Resolva 5 problemas matemáticos!')

while contador <= 4:
    if operador == '/':
        num2 = random.randint(1,10)
        num1 = num2*random.randint(1,10)
        print(f'O computador escolheu: {num1} e {num2}, com operador "{operador}".')
        resposta = float(input('Qual é a resposta da conta? '))
        divisao = num1/num2
        if divisao == resposta:
            print('Você acertou!')
        else:
            print('Você errou!')
    elif operador == '+':
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(f'O computador escolheu: {num1} e {num2}, com operador "{operador}".')
        resposta = float(input('Qual é a resposta da conta? '))
        soma = num1 + num2
        if soma == resposta:
            print('Você acertou!')
        else:
            print('Você errou!')
    elif operador == '*':
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(f'O computador escolheu: {num1} e {num2}, com operador "{operador}".')
        resposta = float(input('Qual é a resposta da conta? '))
        multiplicacao = num1 * num2
        if multiplicacao == resposta:
            print('Você acertou!')
        else:
            print('Você errou!')
    else:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(f'O computador escolheu: {num1} e {num2}, com operador "{operador}".')
        resposta = float(input('Qual é a resposta da conta? '))
        subtracao = num1 - num2
        if subtracao == resposta:
            print('Você acertou!')
        else:
            print('Você errou!')
    contador += 1
     

# Aqui, o problema é a divisão, que pode ter n casas decimais. Aí, quando a pessoa insere a resposta da divisão, não dá pra...
# ...especificar o número de casas decimais que ela tem que inserir. Outra coisa, o Prata sugeriu um modelo de código para...
# ... fazer essa divisão dar certo, mas quando eu o uso, a conta não funciona.