peso = 103.3
altura = 1.85
imc = peso/(altura*altura)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você tem o peso normal.')
elif 25 <= imc < 30:
    print('Você está de sobrepeso.')
elif imc >= 30:
    print('Você tem obesidade.')