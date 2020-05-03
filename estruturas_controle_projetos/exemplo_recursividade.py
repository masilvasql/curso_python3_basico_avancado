def imprimir(maximo, atual):
    # if(atual >= maximo):
    #     return
    # print(atual, end=', ')
    # imprimir(maximo, atual + 1)
    # ___OU____
    if(atual < maximo):
        print(atual, end=', ')
        imprimir(maximo, atual + 1)


imprimir(1000, 0)
