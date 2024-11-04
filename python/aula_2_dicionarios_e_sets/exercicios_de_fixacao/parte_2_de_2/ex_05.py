contatos = {
    "Ana": "1234-5678",
    "Pedro": "8765-4321",
    "Maria": "1357-2468"
}

pergunta = input('Quer adicionar mais um contato (sim/não)? ')
if pergunta == 'sim':
    nome = input('Digite o nome que quer adicionar: ')
    numero = input('Digite o número que quer adicionar: ')
    contatos[nome] = numero
else:
    print('Programa encerrado.')

print(contatos)