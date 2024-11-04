# Definindo os dois primeiros termos da sequência de Fibonacci
termo1 = 0
termo2 = 1

# Definindo o contador e o número de termos que queremos exibir
contador = 0
num_termos = 20

print("Sequência de Fibonacci:")

# Usando o laço while para gerar e exibir os 20 primeiros termos
while contador < num_termos:
    print(termo1)
    # Atualizando os termos
    proximo_termo = termo1 + termo2 # 1
    termo1 = termo2 # 1
    termo2 = proximo_termo 
    
    # Incrementando o contador
    contador += 1

