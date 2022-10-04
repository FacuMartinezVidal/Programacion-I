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
arch=open("/Users/facundomartinezvidal/Documents/UADE/Programacion-I/Clases/04.10/datos.txt",mode="r")
linea=arch.read()
print(linea)
arch.close()