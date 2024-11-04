alunos = int(input('De quantos alunos estamos falando? '))
media_soma = 0
media_geral = 0

for i in range (1,alunos+1):
    nome = input(f'Qual o nome do aluno {i}? ')
    nota1 = float(input(f'Digite a 1ª nota de {nome}: '))
    nota2 = float(input(f'Digite a 1ª nota de {nome}: '))
    nota3 = float(input(f'Digite a 1ª nota de {nome}: '))
    media = (nota1 + nota2 + nota3) / 3
    media_soma += nota1 + nota2 + nota3
    media_geral = media_soma / alunos
    if media >= 7:
        print(f'{nome} foi aprovado(a)!')
    else:
        print(f'{nome} foi reprovado(a)!')
    print(f'Suas notas foram {nota1:.2f}, {nota2:.2f} e {nota3:.2f} e sua média de notas foi de {media:.2f}.')
    
print(f'A média geral da turma foi de {media_geral}.')
