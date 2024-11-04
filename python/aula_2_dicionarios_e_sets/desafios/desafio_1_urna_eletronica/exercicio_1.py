candidatos = {'A': {'votos': 0},
              'B': {'votos': 0},
              'C': {'votos': 0}}

voto = input('Digite seu candidato: ')
candidatos[voto]['votos'] += 1
print(candidatos)