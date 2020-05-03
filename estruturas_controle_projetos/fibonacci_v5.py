def finbonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        # -2 =0 da lista e -1 = 1 da lista
        # pega o elemento -2 até o final --> do 1 ao zero
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in finbonacci(10000):
        print(fib, end=", ")
