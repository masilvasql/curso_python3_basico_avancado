def finbonacci(quantidade):
    resultado = [0, 1]
    # _ usar o underline quando precisar da variável mas não for utilizar
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros nº da sequência
    for fib in finbonacci(20):
        print(fib, end=", ")
