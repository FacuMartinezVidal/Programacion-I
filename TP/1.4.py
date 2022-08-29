# Debe generar el cambio que el vendedor le tiene que dar al cliente

billetes = [500, 100, 50, 20, 10, 5, 1]
dineroVuelto = []
# COSTO DE LA COMPRA
valorCompra = int(input('Valor de la compra: '))

while valorCompra < 0:
    print('error, ingresar dos digitos')
    valorCompra = int(input('Valor de la compra: '))

# DINERO QUE RECIBE
dineroRecibido = int(input('Dinero recibido: '))

while dineroRecibido < 0:
    print('error, ingresar dos digitos')
    dineroRecibido = int(input('Dinero recibido: '))

# VUELTO
vuelto = dineroRecibido - valorCompra
print(vuelto, 'soy resta')


def calcularVuelto(vuelto):
    i = 0
    # while recorre array

    while vuelto > 0:
        if i > 6:
            i = 0
        if billetes[i] <= vuelto:
            # restamos vuelto para que en la siguiente vuelta nos de un numero menor
            vuelto = vuelto - billetes[i]
            # appendeamos el billete
            dineroVuelto.append(billetes[i])
            # ordena de menor a mayor mientras appendea
            dineroVuelto.sort(reverse=True)
        i = i + 1
    return dineroVuelto


print(calcularVuelto(vuelto))