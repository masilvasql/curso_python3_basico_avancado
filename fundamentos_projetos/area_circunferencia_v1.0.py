from string import Template


# 3.1415 * (raio ^ 2) --- área da circunferência


pi = 3.14159
raio = 15.3
areaCircunferencia = pi * raio ** 2

template = Template('A área da circunferência é $area')

#duas formas de interpolar strings
print(template.substitute(area = areaCircunferencia))

print(f'A área da circunferência é {areaCircunferencia}')
