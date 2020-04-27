palavra = 'paralelepipedo'

for letra in palavra:
    # end = final de cada print, imprime a vírgula ou outro caractere que vc decidir
    print(letra, end=',')
print('Fim')


aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']  # lista

for nome in aprovados:
    print(nome)

# enumerate acessa o índice do array
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1 }) {nome}')

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta',
               'Quinta', 'Sexta', 'Sábado')  # tupla

for dia in dias_semana:
    print(f'Hoje é dia :{dia}')

for letra in set('Muito Legal'):  # set não garante a ordem e não possui índice
    print(letra)
