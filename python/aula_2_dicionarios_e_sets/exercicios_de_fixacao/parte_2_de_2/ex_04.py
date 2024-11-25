notas_alunos = {
    "Ana": [8.5, 9.0, 7.5],
    "Pedro": [5.5, 6.0, 7.0],
    "Maria": [7.0, 7.5, 6.0]
}

media = 0
soma = 0
contador = 0

for aluno, nota in notas_alunos.items():
    for valor in nota:
        soma += valor
        media = soma / 3
        contador += 1
        if contador == len(notas_alunos[aluno]):
            if media >= 7:
                print(f'O aluno {aluno} tem média {media:.2f} e está aprovado!')
            else:
                print(f'O aluno {aluno} tem média {media:.2f} e está reprovado!')
            media = 0
            soma = 0
            contador = 0    

        
        

    
    

               