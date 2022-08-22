def positiveNumber(n1, n2, n3):
    if n1 >= n2:
        if n1 == n2:
            return -1
        else:
            if n1 > n3:
                return n1
            if n1 == n3:
                return -1
            else:
                return n3
    else:
        if n2 > n3:
            return n2
        if n2 == n3:
            return -1
        else:
            return n3


# Funcion que ingresa valores
def ingresarValor():
    n1 = int(input('Ingresa el primer numero: '))
    n2 = int(input('Ingresa el segundo numero: '))
    n3 = int(input('Ingresa el tercer numero: '))
    print(positiveNumber(n1, n2, n3))


ingresarValor()

