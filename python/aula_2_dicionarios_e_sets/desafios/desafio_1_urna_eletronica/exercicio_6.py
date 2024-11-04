candidatos = {'A': {'votos': 0},
              'B': {'votos': 0},
              'C': {'votos': 0}}

print('Candidatos disponíveis: ') 

for candidato in candidatos:
    print(f'Candidato {candidato}')

voto = input('Digite o nome do candidato em quem você deseja votar (ou sair para encerrar): ')

while voto != 'sair':
    candidatos[voto]['votos'] += 1
    print(f'Você votou no candidato {voto}')
    voto = input('Digite o nome do candidato em quem você deseja votar (ou sair para encerrar): ')

for candidato, voto in candidatos.items():
    print(f'Resultado: Candidato {candidato} - {voto} votos.')

if candidatos['A']['votos'] > candidatos['B']['votos'] and candidatos['A']['votos'] > candidatos['C']['votos']:
    print('Vencedor da eleição: Candidato A')
elif candidatos['B']['votos'] > candidatos['A']['votos'] and candidatos['B']['votos'] > candidatos['C']['votos']:
    print('Vencedor da eleição: Candidato B')
elif candidatos['C']['votos'] > candidatos['A']['votos'] and candidatos['C']['votos'] > candidatos['A']['votos']:
    print('Vencedor da eleição: Candidato C')
elif candidatos['A']['votos'] == candidatos['B']['votos'] == candidatos['C']['votos']:
    print('Empate entre candidatos A, B e C')
elif candidatos['A']['votos'] == candidatos['B']['votos']:
    print('Empate entre candidatos A e B')
elif candidatos['A']['votos'] == candidatos['C']['votos']:
    print('Empate entre candidatos A e C')
elif candidatos['B']['votos'] == candidatos['C']['votos']:
    print('Empate entre candidatos B e C')   
