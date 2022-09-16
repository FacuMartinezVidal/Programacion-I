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



#Datos que tengo
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
columnas=100
filas=4
matriz=[([0]*columnas)for f in range (filas)]

#En la fila 0, generar los tres valores aleatorios
from random import randint as r
matriz[0][0]=r(1,100)
matriz[0][1]=r(500,1000)
matriz[0][2]=r(1,26)
pos=matriz[0][2]
num1=matriz[0][0]
num2=matriz[0][1]
print (pos)

#concatenar el numero + letra
def repuesto(abc,pos):
    letra=abc[pos]
    datoNuevo=letra+ str(num1)+str(num2)
    abc[pos]=datoNuevo
    return abc[pos]
codigoRepuesto=repuesto(abc,pos)

#Lo cargo en la fila 0 de la matriz
matriz[0][3]=codigoRepuesto

#Cargo los valores pedidos para la fila 1,2,3
matriz[1][0]=r(1,200)
matriz[2][0]=r(10,30)
stock=matriz[1][0]
reposicion=[2][0]
if stock<reposicion:
    matriz[3][0]="reponer"
print(abc)