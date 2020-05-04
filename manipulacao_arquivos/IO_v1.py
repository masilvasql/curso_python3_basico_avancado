arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()


for registro in dados.splitlines():
    # o asterísco, extrai N parâmetros que venham em uma lista
    print('Nome: {}, Idade {}'.format(*registro.split(",")))
