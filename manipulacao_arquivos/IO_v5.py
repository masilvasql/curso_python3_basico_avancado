
with open('pessoas.csv') as arquivo:  # implicitamente o WITH irá fechar o arquivo
    for registro in arquivo:
        print("nome: {}, idade: {}".format(*registro.strip().split(',')))


if arquivo.closed:
    print("Arquivo foi fechado")
