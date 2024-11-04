candidatos = {'A': {'votos': 0},
              'B': {'votos': 0},
              'C': {'votos': 0}}

voto = input('Em quem você quer votar, A, B ou C? ')
candidatos[voto]['votos'] += 1
print(candidatos)