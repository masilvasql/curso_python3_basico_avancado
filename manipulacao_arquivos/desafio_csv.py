import csv

with open("desafio-ibge_.csv") as entrada:
    cont = 0
    for registro in csv.reader(entrada):
        if(cont > 0):
            print("Nono Registro: {8}, Quarto registro> {3}".format(*registro))
        cont = cont + 1
