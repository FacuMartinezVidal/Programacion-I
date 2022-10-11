#Crear la matriz por comprension 
# filas=5
# columnas=5
# matriz=[([0]*columnas) for f in range (filas)]
# #Rellenar la matriz
# from random import randint as r
# for f in range (filas):
#     print()
#     for c in range(columnas):
#         n=r(1,15)
#         matriz[f][c]=n
#         print("%2d" % matriz[f][c],end=" ")
# suma=0
# #Valores de la los elementos de la diagonal principal
# for f in range (filas):
#     for c in range(columnas):
#         if c==f:
#             suma+=matriz[f][c]
# promedio=suma//filas

#Cadena de caracteres
#Secuencia de caracteres. Es case Sensitive, o sea, distingue entre mayusculas y minusculas 
#Operadores:
#Concatenar [string1] * [string2]
#Replicar [string]*5
#Buscar  if palabra in string
#Comparar if string1 == string2
#str() transforma cualquier cosa a string 
#iterar una cadena 
# cad="Hoy es martes"
# for letra in cad:
#     print(letra,edad="")
#Se puede acceder a la cadena utilizando subindicies
# cad="Me gusta Programacion I"
# print(cad[5])
#Una cadena de string no se la puede modificar usando subindices
#se la puede manipular usando rebanadas
# cad="Me gusta la clase"
# print(cad[0:5])

#Funciones 
#len() longitud de la cadena
#max() el caracter que tiene el valor mas alto en ascii
#min() el caracter que tiene el valor menos alto en ascii

#Metodos
# cad="Me gusta el paddle"
# print(cad.count("a")) devuelve en este caso la cantidad de a
# index () a donde arranca una porcion del string 
# replace(parte del string que quieras cambiar, string que quieras poner)
# isalpha() te determina si todos los caracteres son alfabeticos, retorna true or false
# isdigit() te determina si todos los caracteres son numeros
# isalnum() te determina si todos los caracteres son numeros y letras 
# isupper() te determina si todas son mayusculas 
# islower() te determina si todas son minusculas
# upper() pasa todo a mayuscula
# lower() pasa todo a miniscula 
# capitalize() pone la primera letra en mayuscula 
# title() sube a mayusucla la primera letra de cada palabra
# split() crea una lista con cada palabra 
# join() le pones un parametro y lo pone entre las letras

#Ingresar por teclado el nombre de una instutitucion o entidad, y generar su sigla
# palabra="Club Atletico de Boca Juniors"
# sigla=""
# for x in range(0,len(palabra)):
#     if x==0:
#         sigla+=palabra[x]
#     if palabra[x]==" ":
#         sigla+=palabra[x+1]
# print (sigla.upper())

#center() te centra la palabra, el primer parametro son el tamaño en cada lado del centrado y el segundo parametro lo queres que haya
#ljust() justificaba a la izquierda y los esapacios lo rellena con lo que queiras 
#rjust() idem de arriba pero a la derecha en vez de la izquierda
#zfill() rellena con ceros, dentro del parametro para poner el largo de la palabra con los ceros incluidos
#lstrip() elimina el caracater indicado a la izquierda 
#rstrip() elimina el caracter indicado pero a la derecha
#strip() elimina de ambos lados

#format
# a=123
# print("%4d" %a) #te da cuatro digitos
# print("%4f"%a) #te da la cantidad de numeros que quieras despues de la coma
# nombre="Maria"
# nota=9
# print("Legajo {} Nombre {} Nota {}" .format(a,nombre,nota))


