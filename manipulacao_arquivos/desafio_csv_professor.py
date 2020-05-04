import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando CSV')
        dados = entrada.read().decode('latin1')
        print("Download completo!")
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # r, escreve de forma literarl por exemplo: print(\n\n\n), não ira quebrar linhas,
    # mas sim, escrever de froma literal, utilizado para evitar interpretar caracteres especiais de forma indevida
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
