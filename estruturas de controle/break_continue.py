for x in range(1, 11):
    if(x % 2 == 0):  # par
        continue  # interrompe a iteração e vai para próxima
    print(x)

for x in range(1, 11):
    if x == 5:
        break
    print(x)
