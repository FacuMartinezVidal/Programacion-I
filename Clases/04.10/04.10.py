#Archivos 

#Apetura, hay distintos modos open
# arch=open"datos.txt", mode='w'
# arch=open
#r=lectura
#w=escritura
#a=append
#t=texto
#b=binario

#Cerrar, para cerrar un arhivo, se debe hacer esto sino aparecera que esta en uso .close

#Proceso de escritura, realiza operaciones sobre el archivo
#Ejemplo, crear un archivo con un legajo y nombre de cada alumno. Cada alumno es un registro y cada dato se separa por ";". Finaliza la carga con -1

# arhivo=open("datos.txt", mode='w')
# bandera=0
# while bandera!=-1:
#     alumno=input('Ingrese alumno: ')
#     legajo=input('Ingrese su numero de legajo: ')
#     bandera=int(input('Si desea terminar la operacion, oprima -1: '))
#     arhivo.write(alumno+';'+legajo+"\n")
# arhivo.close

#Readline, realiza la lectura del arhivo registro a registro. Cuando no hay mas lineas retorna una cadena vacia y te los lee y crea en una lista

# arch=open("/Users/facundomartinezvidal/Documents/UADE/Programacion-I/Clases/04.10/datos.txt",mode="r")
# linea=arch.readlines()
# print(linea)
#arch.close()

#Read, lo mismo que read linea pero no te crea una lista
# arch=open("/Users/facundomartinezvidal/Documents/UADE/Programacion-I/Clases/04.10/datos.txt",mode="r")
# linea=arch.read()
# print(linea)
# arch.close()

#Metodo de Seek, para poder volver el archivo permitiendo poner el cursor en la posicion que yo desee
# arch=open("/Users/facundomartinezvidal/Documents/UADE/Programacion-I/Clases/04.10/datos.txt",mode="r")
# linea=arch.read()
# print(linea)
# print('archivo leido')
# arch.seek(0)
# print('segundo lectura')
# linea=arch.read()
# arch.close()

#Ejemplo de ejercicio con while
# arch=open("/Users/facundomartinezvidal/Documents/UADE/Programacion-I/Clases/04.10/datos.txt",mode="r")
# linea=arch.read()
# print(linea)
# while linea:
#     legajo,nombre=linea.split(';')
#     print(legajo,nombre)
#     linea=arch.read()
# arch.close()
# print('fin')

#Otro ejemplo pero con for y try
# try:
#     arch=open("/Users/facundomartinezvidal/Documents/UADE/Programacion-I/Clases/04.10/datos.txt",mode="r")
#     linea=arch.read()
# except IOError:
#     print('Error de lectura del archivo')
# else:
#     try:
#         for linea in arch:
#             legajo,nombre=linea.split(";")
#             legajo=int(legajo)
#             if legajo<100:
#                 print(legajo,nombre)
#     finally:
#         arch.close()

print('hola')