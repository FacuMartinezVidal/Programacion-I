# Desarrollar una funcion que reciba tres numeros enteros positivos y verifique si corresponden a una fecha valida (dia, mes, año). Devolver True o False segun la fecha sea correcta o no. Realizar tambien un programa para verificar el comportamiento de la funcion


def verificarFecha(n1, n2, n3):
    if n1 <= 31 and n1 > 0:
        if n2 <= 12 and n2 > 0:
            if n2 == 2 and n1 > 28:
                return False
            if n3 > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def recibirNumeros():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    n3 = int(input('Numero 3: '))
    print(verificarFecha(n1, n2, n3))


recibirNumeros()