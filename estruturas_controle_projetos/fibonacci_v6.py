def finbonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros nº da sequência
    for fib in finbonacci(30):
        print(fib, end=", ")
