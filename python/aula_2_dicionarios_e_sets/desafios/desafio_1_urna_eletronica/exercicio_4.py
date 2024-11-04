candidatos = {'A': {'votos': 0},
              'B': {'votos': 0},
              'C': {'votos': 0}}

print('Candidatos disponíveis: ') 

for candidato in candidatos:
    print(f'Candidato {candidato}')

while True:
    voto = input('Digite o nome do candidato em quem você deseja votar (ou sair para encerrar): ')
    if voto == 'A':
        candidatos[voto]['votos'] += 1
        print(f'Você votou no candidato {voto}')
        continue
    elif voto == 'B':
        candidatos[voto]['votos'] += 1
        print(f'Você votou no candidato {voto}')
        continue
    elif voto == 'C':
        candidatos[voto]['votos'] += 1
        print(f'Você votou no candidato {voto}')
        continue
    elif voto == 'sair':
        print('Votação encerrada.')
        break
    
