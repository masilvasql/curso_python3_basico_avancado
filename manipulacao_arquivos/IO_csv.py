import csv

with open('pessoas.csv') as entrada:
    with open("texto2.txt", 'w') as saida:
        for pessoa in csv.reader(entrada):
            print("nome: {}, idade: {}".format(*pessoa))
            print("nome: {}, idade: {}".format(*pessoa), file=saida)
