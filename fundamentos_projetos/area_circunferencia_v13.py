from math import pi
import sys
import errno


def circulo(raio):
    areaCircunferencia = pi * float(raio) ** 2
    return areaCircunferencia


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        help()
        sys.exit(errno.EPERM)

    raio = sys.argv[1]
    area = circulo(raio)
    print(f'A área da circunferência é {area}')


def help():
    print(f"""
            É necessário informar o raio do círculo.
            sintaxe é: {sys.argv[0]} <raio>""")
