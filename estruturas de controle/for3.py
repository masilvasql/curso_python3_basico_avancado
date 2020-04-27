produto = {'nome': 'caneta chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto.keys():  # caso não coloque o .keys(), por padrão, irá percorrer as chaves
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():  # no python, após o término do laço for, as variáveis ainda são visíveis fora do escopo do laço
    print(chave, ' = ', valor)
