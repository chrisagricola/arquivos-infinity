nota_1 = float(input('Escreva sua 1ª nota: '))
nota_2 = float(input('Escreva sua 2ª nota: '))
media = (nota_1 + nota_2) / 2

if 0 <= media <= 4:
    print(f'Suas notas foram {nota_1} e {nota_2} e a média delas foi {media}. REPROVADO!')
elif 4.1 <= media <= 6:
    print(f'Suas notas foram {nota_1} e {nota_2} e a média delas foi {media}. REPROVADO!')
elif 6.1 <= media <= 7.5:
    print(f'Suas notas foram {nota_1} e {nota_2} e a média delas foi {media}. APROVADO!')
elif 7.6 <= media <= 9:
    print(f'Suas notas foram {nota_1} e {nota_2} e a média delas foi {media}. APROVADO!')
elif 9.1 <= media <= 10:
    print(f'Suas notas foram {nota_1} e {nota_2} e a média delas foi {media}. APROVADO!')
else: 
    print(f'Suas notas foram {nota_1} e {nota_2} e a média delas foi {media}. CONCEITO INDEFINIDO!')
