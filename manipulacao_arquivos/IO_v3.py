arquivo = open('pessoas.csv')

for registro in arquivo:
    # strip sozinho retira os espaços, se colocar um parâmetro, retira o valor referente ao parâmetro
    print("nome: {}, idade: {}".format(*registro.strip().split(',')))

arquivo.close()
