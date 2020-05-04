arquivo = open('pessoas.csv')

try:
    for registro in arquivo:
        print("nome: {}, idade: {}".format(*registro.strip().split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print("Arquivo foi fechado")
