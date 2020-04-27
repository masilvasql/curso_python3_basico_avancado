from math import pi


def circulo(raio):
    areaCircunferencia = pi * float(raio) ** 2
    return areaCircunferencia


if __name__ == '__main__':
    raio = input("Informe o raio : ")
    area = circulo(raio)
    print(f'A área da circunferência é {area}')
