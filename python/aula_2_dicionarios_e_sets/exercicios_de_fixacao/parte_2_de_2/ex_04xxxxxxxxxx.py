notas_alunos = {
    "Ana": [8.5, 9.0, 7.5],
    "Pedro": [5.5, 6.0, 7.0],
    "Maria": [7.0, 7.5, 6.0]
}

media = 0

for notas in notas_alunos.values():
    for nota in notas:
        media += nota / 3
    for aluno in notas_alunos:
        print(f'O aluno {aluno} tem uma média de {media}.')
    continue                