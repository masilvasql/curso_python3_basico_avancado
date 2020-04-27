from math import pi


def circulo(raio):
    areaCircunferencia = pi * float(raio) ** 2
    print(f'A área da circunferência é {areaCircunferencia}')


if __name__ == '__main__':
    raio = input("Informe o raio : ")
    circulo(raio)
