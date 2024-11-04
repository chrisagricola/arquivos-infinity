lista = [
    ('A', 6.5, 2.4, 8.9),
    ('B', 7.4, 3.1, 1.5),
    ('C', 5.5, 3, 6.7)
    ]

media_A = (6.5 + 2.4 + 8.9) / 3
media_B = (7.4 + 3.1 + 1.5) / 3
media_C = (5.5 + 3 + 6.7) / 3

# print(f'Média de A: {media_A:.2f}')
# print(f'Média de B: {media_B:.2f}')
# print(f'Média de C: {media_C:.2f}')

# medias = [media_A, media_B, media_C]

# print(medias)
# print(medias[-1])
# print(medias[-2])
# print(medias[-3])

tuplas = (['A', media_A], ['B', media_B], ['C', media_C])

print(f'Classificação: 1° - {tuplas[0]}, 2° - {tuplas[2]}, 3° - {tuplas[1]}.')

