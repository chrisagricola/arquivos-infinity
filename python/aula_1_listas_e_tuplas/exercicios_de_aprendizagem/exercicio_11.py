soma = 0
alunos = ['A', 'B', 'C']
vetor = []
numero = 0

for aluno in alunos:
    for nota in range (1, 5):
        notas = float(input(f'Digite a nota {nota} do aluno {aluno}: '))
        soma += notas
        media = soma / nota
    vetor.append(media)
    if media >= 7:
        numero += 1    

print(f'O número de alunos com média maior ou igual a sete foi: {numero}')
