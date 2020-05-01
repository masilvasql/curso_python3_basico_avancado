def get_dia_semana(dia):
    dias = {
        1: 'Fim de Semana',
        2: 'Dia de Semana',
        3: 'Dia de Semana',
        4: 'Dia de Semana',
        5: 'Dia de Semana',
        6: 'Dia de Semana',
        7: 'Fim de Semana'
    }
    return dias.get(dia, '**Inválido**')


for dia in range(1, 8):
    print(f'{get_dia_semana(dia)}')
