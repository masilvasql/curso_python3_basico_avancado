for i in range(1, 11):  # range vai de x até y -1
    print(f'i = {i}')

print("-------------")

for j in range(10):  # caso não informe o valor inicial do range, ele assume 0
    print(f'j = {j}')

# Taboada
for x in range(11):
    for y in range(11):
        print(f'{x} x {y} = {x * y}')
        if y == 10:
            print('---------------------')
