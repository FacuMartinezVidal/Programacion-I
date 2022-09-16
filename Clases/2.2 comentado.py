# La Universidad Argentina de la Empresa, para cada uno de sus materias dispone de la siguiente matriz, para poder cargar las notas de los parciales de cada alumno, y establecer su situación final
# La misma, tiene la siguiente disposición:
# Fila 0: LU (Libreta Universitaria) Es un valor aleatorio comprendido entre 1000000 y 10000000
# Fila 1: Nota parcial 1, valor aleatorio comprendido entre 1 y 10
# Fila 2: Nota parcial 2, valor aleatorio comprendido entre 1 y 10
# Fila 3: Situación Final, promedio entre ambas notas de parcial

# Al principio del proceso se solicita el ingreso del código del curso, siendo el mismo un entero de 5 dígitos, controlarlo; el nombre de la materia y la  cantidad de alumnos por curso, a fin de establecer la cantidad de columnas de la matriz
# Y se ingresa un código que indica si la materia se aprueba por promoción (1) o por examen final (2)
# Se solicita:
# A – Crear la matriz por comprensión y cargarla con los datos indicados
# B – Imprimir el nombre de la universidad y su logo
# C – Imprimir el nombre de la materia 
# D – Si la materia se promociona, mostrar la LU, en un campo de 15 posiciones, alienada a la derecha y completado con ceros, y el promedio, en un campo de 4 posiciones, completado con ceros a la izquierda
# E – Si la materia se aprueba por examen final, emitir un listado con los nros de LU y los promedios,  de aquellos alumnos que rinden el examen final, superiores o iguales a 7
# F – Por último, emitir un listado con los alumnos que deben recursar la materia (con los dos parciales aplazados), ordenado por LU, de manera descendente. Puede utilizar una lista auxiliar para no alterar la matriz principal
#  Los listados son independientes entre si

#Valores que se van a cargar
filas=4
coCurso=input('Ingrese el codigo del curso: ')
bandera=False
while bandera==False:
    if (len(coCurso))==5:
        bandera=True
    else:
        coCurso=input('Error debe tener 5 digitos, cargarlo nuevamente: ')
materia=input('Ingrese el nombre de la materia: ')
codigo=int(input('La materia se aprueba por promocion(1) o por examen final(2): '))
columnas=int(input('Ingrese la cantidad de alumnos que desea cargar: '))



#Logo de la universidad (B)
universidad='Universidad Argentina De Empresa'
logo=''
for x in range(len(universidad)):
    if x==0:
        logo+=universidad[x]
    if universidad[x]== ' ':
        logo+=universidad[x+1]

#Impresiones
print(universidad+' '+logo)
print(materia)

    

#Creo la matriz (A)
matriz=[([0]*columnas)for f in range(filas)]

#Cargo los valores en la matriz (A)
from random import randint as r
for c in range(columnas):
    lu=matriz[0][c]=r(1000000,10000000)
    nota1=matriz[1][c]=r(1,10)
    nota2=matriz[2][c]=r(1,10)
    promedio=matriz[3][c]= (nota1+nota2)//2


#Printeo en forma de matriz
for f in range(filas):
    print()
    for c in range(columnas):
        print("%2d" % matriz[f][c],end=" ")
print()

#Si la materia se promociona
if codigo==1:
    for c1 in range(columnas):
        if matriz[3][c1]>6:
            print(str((matriz[0][c1])).rjust(15,'0'))
            print((str(matriz[3][c1])).ljust(4,'0'))
        print()

#Si la materia se va a examen final
listado=[]
alumnos=[]
if codigo==2:
    for c2 in range(columnas):
        if matriz [3][c2]>=7:
            alumnos.append(matriz[0][c2])
            alumnos.append(matriz[3][c2])
            listado.append(alumnos)
            alumnos=[]
    print(listado)

#Para los alumnos aplazados
aplazados=[]
for c3 in range(columnas):
    if (matriz[1][c3]<4) and (matriz[2][c3]<4):
        aplazados.append(matriz[0][c3])
aplazados.sort(reverse=True)
print(aplazados)
