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