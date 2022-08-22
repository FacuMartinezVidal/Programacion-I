# #Desempaquetado de una lista
# a=[3,6,9]
# a1,a2,a3= #var1,var2,var3=nombreLista#
# print(a)
# print(a1," ",a2," ",a3)

# #Suma de lista
# a=[4,6,8]
# b=[2,5,7,9,10]
# c=a+b
# c1=b+a
# print(c)

#Concatenar
# b=[2,5,7,9,10]
# b+=[6]
# print(b)

#Funcion max() Devuelve valor maximo de una lista 
# b=[2,5,7,9,10]
# print(max(b))

#Funcion min() Devuelve valor minimo de una lista 
# b=[2,5,7,9,10]
# print(min(b))

#Funcion max() Devuelve la suma de elementos de una lista
# b=[2,5,7,9,10]
# print(sum(b))

#operador in 
# b=[2,5,7,9,10]
# if 4 in b:
#     print("el dato se encuentra")
# else:
#     print("el dato no se encuentra")

#Metods
# b=[2,5,7,9,10]
#.append() agrega valores en la lista al final
#.insert(posicion,valor) agrega una valor en la posicion indicada
#.pop() elimina el ultimo valor de la lista
#.pop(posicion) elimina el valor de la posicion indicada
#.remove() elimina el valor de una lista, si hay dos valores en la lista, elimina al primero que encuentra
#.index() devuelve la posicion de un valor determinado, siempre devuelve el primero que este
#.index(valor,incio) busca un valor apartir de un posicion de inicio
#.index(valor,incio,fin) busca un valor apartir de un posicion de inicio y tambien le podes agregar una posicion final en la que busque 
#.count(valor) devuelve la cantidad de veces que se repite un valor 
#.clear() elimina todos los elementos de una lista
#.reverse() devuelve la lista invertida
#.sort() ordena la lista de manera ascendente 
#.sort(reverse=True) ordena la lista de manera descendente 
#for variable in nombreLista:
# for numero in b:
#     print (numero, end=" ")
#modulo
# import random
# for i in range (5):
#     print(random.randint(5,20))
# for i in range (5):
#     print(random.random()) #valores aleatorios entre 0 y 1
#from random import randint
# for i in range (5):
#     print(randint(5,20)) #no hace falta usar el from random
#from random import randint as azar 
# for i in range (5):
#     print(azar(5,20)) #le pones el nombre que vos quieras 

#Listas Rebanadas
#a=[4,5,6,6,7,9]
#print(a[1:4]) el primer valor es inclusive, en cambio el segundo valor es no inclusive
#print(a[::4]) el primer valor es inclusive, en cambio el segundo valor es no inclusive
#print(a[:4]) el primer valor es inclusive, en cambio el segundo valor es no inclusive

#Listas por comprension
#partiendo de una lista inicial, es una manera matematica de obtener una segunda lista 
#a=[4,5,6,6,7,9]
#cuadrado=[i**2 for i in lista] #eleva todos los elementos al cuadrado, sirve para todos los tipos de funciones aritmeticas 
#print(cuadrado)
#cuadrado2=[i**2 for i in lista if var%2==0] #tambien le podes agregar una condicion 
str="LearnPython"

length_str=len(str)

sliced_str=str[length_str::-1] 
print ("The sliced string is:",sliced_str)