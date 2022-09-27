# Una casa de venta de repuestos de heladera, “La vieja heladera”, se maneja con los siguientes arreglos:
# Una lista con las letras del abecedario, sin LL y sin Ñ, o sea, abc=[‘a’, ´b´, ….]
# Una matriz de 4*100 (filas * columnas), donde:
# Para la fila 0, deberá generar 3 valores aleatorios
# El primero, es un nro entre 1 y 100, el segundo, entre 500 y 1000 y el 3cero entre 1 y 26,
# Con el 3cer valor obtenido, deberá ubicar la letra correspondiente en la lista respectiva, a esa letra deberá concatenarle, antes de ella, los dos valores numéricos obtenidos, o sea
# 1) 51 2) 625 3) 5 ---------> deberá obtener ‘e51625’
# Este dato, que deberá ser obtenido a través de una función, será el código del repuesto y deberá ir cargándolo en la fila 0, en la columna correspondiente
# En la fila 1, generar un valor aleatorio entre 1 y 200, correspondiente al stock de ese repuesto.
# En la fila 2, generar un valor aleatorio entre 10 y 30, siendo este dato el punto de reposición para el repuesto correspondiente
# En la fila 3, cargar la leyenda ‘reponer’, si el stk está por debajo del punto de reposición, para ese producto
# Por fin de carga generar un listado que contendrá:
# EL nombre de la empresa, con la primera letra de cada palabra en mayúscula y su sigla
# Mostrar los códigos de repuestos a reponer, mostrándolos en una fila, en un campo de 30 espacios, con formato centrado y completados el campo por guiones
# Cuantos son
# Qué porcentaje representa la cantidad a reponer sobre el total de los repuestos

from random import randint as r

#Genero la lista abc
abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lista_abc=abc.split()


#Creo la matriz sin comprension
filas=4
columnas=100
matriz=[]
for f in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(0)

#Para la fila 0...
def codigoRepuesto():
    v1_fila0=r(1,100)
    v2_fila0=r(500,1000)
    v3_fila0=r(1,25)
    letra=lista_abc[v3_fila0]
    repuesto=letra+ str(v1_fila0)+ str(v2_fila0)
    return repuesto

for c_fila0 in range(columnas):
    matriz[0][c_fila0]=codigoRepuesto()

#Para la fila 1...
def stock():
    v_fila1=r(1,200)
    return v_fila1

for c_fila1 in range(columnas):
    matriz[1][c_fila1]=stock()

#Para la fila 2...
def puntoReposicion():
    v_fila2=r(10,30)
    return v_fila2

for c_fila2 in range(columnas):
    matriz[2][c_fila2]=puntoReposicion()

#Para la fila 3...
repuestoReponer=[]
for c in range(columnas):
    if (matriz[1][c])<(matriz[2][c]):
        repuestoReponer.append(matriz[0][c])
        matriz[3][c]= 'reponer'

#Listado que me pide al final
#primera letra de la palabra en mayuscula
empresa= 'La vieja heladera'
empresa_upper=empresa.title()
#sigla
sigla=''
for x in range(len(empresa_upper)):
    if x==0:
        sigla+=empresa_upper[x]
    if empresa_upper[x]==' ':
        sigla+=empresa_upper[x+1]

#Matriz impresa
for j in range(filas):
    print()
    for i in range(columnas):
        print("%s" % matriz[j][i], end=' ')

#Repuesto a reponer centrado con guiones
for x in range(len(repuestoReponer)):
    print(repuestoReponer[x].center(30,'-'))

#Cuanto hay que reponer
print('Repuestos a reponer:',len(repuestoReponer))

#Porcentaje
porcentaje= len(repuestoReponer)*100 // len(matriz[1])
print('Representan el:',str(porcentaje)+'%','stock')