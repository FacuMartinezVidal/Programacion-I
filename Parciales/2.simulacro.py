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


coCurso=input('Ingrese el codigo del curso: ')
bandera=True
while bandera!=False:
    if len(coCurso)==5:
        bandera=False
    else:
        coCurso=input('El codigo debe tener 5  digitos, Ingrese codigo de curso nuevamente: ')

aprobacion=int(input('Ingrese como se aprueba la materia: '))
nombreMateria=input('Ingrese el nombre de la materia: ')

columnas=int(input('Cantidad deseada de alumnos que se desea cargar: '))
filas=4
matriz=[([0]*columnas) for f in range (filas)]

uade='Universidad Argentina de Empresas'
logo=''
for x in range(0,len(uade)):
    if x==0:
        logo+=uade[x]
    if uade[x]==" ":
         logo+=uade[x+1]
logo_fix=logo.upper()
print(uade+" "+logo_fix)
print('Nombre de la Materia: ',nombreMateria)
from random import randint as r
for c in range(columnas):
    legajo=r(1000000,10000000)
    nota1=r(1,10)
    nota2=r(1,10)
    sFinal= (nota1+nota2)/2
    matriz[0][c]=legajo
    matriz[1][c]=nota1
    matriz[2][c]=nota2
    matriz[3][c]=sFinal

for f in range(filas):
    print()
    for c in range(columnas):
        print("%2d" % matriz[f][c],end=" ")
print()

if aprobacion==1:
    print('Alumnos Promocionados')
    for c in range(columnas):
        if matriz[1][c]>4 and matriz[2][c]>4 and matriz[3][c]>=7:
            lu=str(matriz[0][c])
            print(lu.rjust(15,"0"))

if aprobacion==2:
    print('Alumnos que rinden Final y Promedio>=7')
    for c in range(columnas):
        if matriz[1][c]>4 and matriz[2][c]>4 and matriz[3][c]>=7:
            lu=str(matriz[0][c])
            promedio=str(matriz[3][c])
            print(lu+(promedio.rjust(4,'0')))


lst_r=[]
for c in range(columnas):
    if matriz[1][c]<4 and matriz[2][c]<4:
        lst_r.append(matriz[0][c])
lst_r.sort()
print('Alumnos que recursan:')
print(lst_r)

z=''
           

        





