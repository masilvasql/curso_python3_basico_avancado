from math import pi
import sys


def circulo(raio):
    areaCircunferencia = pi * float(raio) ** 2
    return areaCircunferencia


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'A área da circunferência é {area}')
