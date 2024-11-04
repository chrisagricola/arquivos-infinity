numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
if numero1 == numero2 == numero3:
    print('Seu triângulo é equilátero!')
elif numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
    print('Seu triângulo é isósceles!')
elif numero1 != numero2 and numero2 != numero3 and numero1 !=numero3:
    print('Seu triângulo é escaleno!')
    
