
with open('pessoas.csv') as arquivo:  # implicitamente o WITH irá fechar o arquivo
    with open('pessoas.txt', 'w') as saida:  # w = WRITE, modo de escrita
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # fazendo print dentro de um arquivo
            print("nome: {1}, idade: {0}".format(*pessoa), file=saida)


if arquivo.closed:
    print("Arquivo foi fechado")

if saida.closed:
    print("Arquivo de saída está fechado")
