def celsius_para_fahrenheit(celsius: int):
    fahrenheit = int((celsius * 9/5) + 32)
    return fahrenheit

celsius = 25
resultado = celsius_para_fahrenheit(celsius)
print(f'A temperatura em Fahrenheit é de: {resultado}°')