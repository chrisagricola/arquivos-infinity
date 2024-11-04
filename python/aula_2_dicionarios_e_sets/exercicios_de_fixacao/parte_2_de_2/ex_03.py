compras_clientes = {
    "Ana": ["leite", "pão", "maçã"],
    "Pedro": ["pão", "arroz", "leite", "maçã"],
    "Maria": ["maçã", "leite"]
}

for cliente, compras in compras_clientes.items():
    tamanho = len(compras)
    print(f'A {cliente} comprou {tamanho} itens.')