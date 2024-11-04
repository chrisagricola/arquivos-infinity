dicionario = {
    "machado": {
        "dica_1": "é um sobrenome",
        "dica_2": "corta madeira",
        "dica_3": "de assis"
    },
    "são paulo": {
        "dica_1": "nome de santo",
        "dica_2": "nome de cidade",
        "dica_3": "nome de time"
    },
    "planeta": {
        "dica_1": "o sol não é",
        "dica_2": "a lua não é",
        "dica_3": "a terra é"
    },
    "sanfona": {
        "dica_1": "instrumento musical",
        "dica_2": "fole",
        "dica_3": "luiz gonzaga"
    },
    "águia": {
        "dica_1": "ave com bico",
        "dica_2": "carnivora",
        "dica_3": "garras"
    },
    "alergia": {
        "dica_1": "poeira",
        "dica_2": "tinta",
        "dica_3": "doença"
    },
    "açúcar": {
        "dica_1": "cana",
        "dica_2": "beterraba",
        "dica_3": "cristais"
    },
    "áfrica": {
        "dica_1": "antigo continente",
        "dica_2": "deserto do saara",
        "dica_3": "leões e elefantes"
    },
    "adolescente": {
        "dica_1": "rebelde",
        "dica_2": "irresponsável",
        "dica_3": "quase adulto"
    },
    "aeroporto": {
        "dica_1": "pista",
        "dica_2": "hangar",
        "dica_3": "avião"
    },
    "agricultura": {
        "dica_1": "terra",
        "dica_2": "cultivo",
        "dica_3": "camponês"
    },
    "neblina": {
        "dica_1": "nevoeiro",
        "dica_2": "trevas",
        "dica_3": "nuvens"
    },
    "edifício": {
        "dica_1": "construção",
        "dica_2": "apartamentos",
        "dica_3": "arranha-céu"
    },
    "flauta": {
        "dica_1": "instrumento musical",
        "dica_2": "buracos",
        "dica_3": "sopro"
    }
}

import random
palavra, dicas = random.choice(list(dicionario.items()))

print('Jogo das pistas: eu te dou dicas e você tenta adivinhar a palavra relacionada à dica.')

for palavra_secreta, dicas in dicionario.items():
    print(f'Dica: {dicas['dica_1']}')
    chute = input('Digite a palavra secreta: ')
    if chute == palavra_secreta:
        print('Parabéns! Você acertou!')
    else:
        print(f'Você errou! Nova dica: {dicas['dica_2']}')
        chute = input('Digite a palavra secreta: ')
        if chute == palavra_secreta:
            print('Parabéns! Você acertou!')
        else:
            print(f'Você errou! Última dica: {dicas['dica_3']}')
            chute = input('Digite a palavra secreta: ')
            if chute == palavra_secreta:
                print('Parabéns! Você acertou!')
            else:
                print(f'Você errou. Fim de jogo.')