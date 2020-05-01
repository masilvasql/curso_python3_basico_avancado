def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }
    return dias.get(dia, '**Inválido**')


diaSemana = get_dia_semana(8)
print(diaSemana)
