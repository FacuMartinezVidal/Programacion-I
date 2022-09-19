from random import randint


abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lista_abc = abc.split()

# cuando no es por comprension creo la matriz antes, vacia.
matriz = []
filas = 4
# deben ser 100 pero para probar coloco 5
columnas = 100

# esta lista sirve para almacenar los codigos que hay qeu mostrar en una fila centrada
codigosRepuestos = []

nombre_empresa = 'La Vieja Heladera'
siglas = ' '
nombre_empresa_lista = nombre_empresa.split()

for i in nombre_empresa_lista:
    siglas = siglas + i[0]


# RELLENO MATRIZ CON 0
for f in range(filas):
    print()
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(0)


# generar valores aleatorios para la fila 0

def valoresAleatorios_fila0():
    n1 = randint(1, 100)
    n2 = randint(500, 1000)
    # coloco 25 en vez de 26 ya que al transformar el abecedario en lista pasamos a tener 25 valores y no 26 debido a que la lista se arranca a contabilizar desde 0
    n3 = randint(1, 25)
    letra = lista_abc[n3]
    return conviertoString(n1, n2, letra)

# FUNCION PARA CONVERTIR A STRING LOS VALORES NUMERICOS DE LA FILA 0


def conviertoString(n1, n2, letra):
    letra_n1 = str(n1)
    letra_n2 = str(n2)
    concatenacion = letra + letra_n1 + letra_n2
    return concatenacion


# GENERO COLUMNA 0

for c in range(columnas):
    matriz[0][c] = valoresAleatorios_fila0()


# FUNCION DE VALORES ALEATORIOS PARA LA FILA 1

def valoresAleatorios_fila1():
    n1 = randint(1, 200)
    return n1


# RELLENO FILA 1 - STOCK

for c in range(columnas):
    matriz[1][c] = valoresAleatorios_fila1()


# FUNCION DE VALORES ALEATORIOS PARA LA FILA 2

def valoresAleatorios_fila2():
    n1 = randint(10, 30)
    return n1


# RELLENO FILA 2 - PUNTO DE REPOSICION

for c in range(columnas):
    matriz[2][c] = valoresAleatorios_fila2()


# CONDICIONAL REPONER
for c in range(columnas):
    if matriz[1][c] < matriz[2][c]:
        codigosRepuestos.append(matriz[0][c])
        matriz[3][c] = 'REPONER'


# MUESTRA LA MATRIZ
for j in range(filas):
    print()
    for i in range(columnas):
        print("%s" % matriz[j][i], end=' ')


# recorro matriz que tiene los repuestos a mostrar
for i in range(len(codigosRepuestos)):
    print(codigosRepuestos[i].center(30, '-'))


# cantidad a reponer
print('CANTIDAD A REPONER: ', len(codigosRepuestos))

# PORCENTAJE CANTIDAD
porcentaje = (len(codigosRepuestos)*100) // len(matriz[1])

print('PORCENTAJE: ', porcentaje, '%')
