from random import randint

for i in range(1, 11):
    print(i)
else:
    print('Fim')

for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim')  # não será executado quando contem um break


# dado de 6 numeros entre 1 e 6
# for que vai percorrer de 1 a 6 (6 incluso)
# excluir números impares
# se for par e for = ao valor sorteado, imprimir a string "acertou " e depois chamar o break

def sortearDado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortearDado() == i:
        print(f'Acertou! {i}')
        break
else:
    print('Não acertou')
