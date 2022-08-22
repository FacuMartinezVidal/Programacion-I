valor = 100


def gastosRealizados():
    viajes = int(input('Cantidad de viajes mensuales: '))
    if viajes >= 1 and viajes <= 20:
        return valor
    if viajes > 20 and viajes < 31:
        return valor - valor0.2
    if viajes > 30 and viajes < 41:
        return valor - valor0.3
    if viajes > 40:
        return valor - valor*0.4


print('El total gastado es: $', int(gastosRealizados()))