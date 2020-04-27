from math import pi
import sys


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[Om'


def circulo(raio):
    areaCircunferencia = pi * float(raio) ** 2
    return areaCircunferencia


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        helpme()
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        print(TerminalColor.ERRO, "o valor precisa ser numérico",
              TerminalColor.NORMAL)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'A área da circunferência é {area}')


def helpme():
    print(f"""
            É necessário informar o raio do círculo.
            sintaxe é: {sys.argv[0]} <raio>""")
