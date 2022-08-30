#Utilizando la forma habitual, partiendo de una lista inicial, obtener el cuadrado de los valores pares y cargarlos a una segunda lista

# lista=[8,1,-2,4,7,10]
# nLista=[]
# for x in range(len(lista)):
#     if (lista[x]%2)==0:
#         cuadrado=(lista[x])**2
#         nLista.append(cuadrado)
# print(nLista)

# Utilizando la forma de comprension de listas
# lst=[8,1,-2,4,7,10]
# cuadrado=[i**2 for i in lst if i%2==0]
# print(cuadrado)

#Utilizando la forma habitual, partiendo de una lista inicial, obtener el cuadrado de los valores pares y cargarlos a una segunda lista, los que no son pares pasarlos directamente
# lst=[8,1,-2,4,7,10]
# cuadrado=[i**2 if i%2==0 else i for i in lst  ]
# print(cuadrado)

#Utilizando la forma habitual, partiendo de una lista inicial, obtener el cuadrado de los valores pares y cargarlos a una segunda lista, los que no son pares pasarlos directamente
# lst=[8,1,-2,4,7,10]
# cuadrado=[i**2 if i%2==0 else "*" for i in lst  ]
# print(cuadrado)

#Cargar una lista con 5 valores ingresados por teclado, utlizando la comprension de listas
# lst=[int(input("Ingrese valor a cargar: " ))for i in range(5)]
# print(lst)

#Crear una lista por compresion de n elementos comprendidos entre 1 y 20
# from random import randint as az
# n=int(input("Ingrese valor n"))
# while n<=0:
#     n=int(input("Ingrese valor n"))

# lst=[az(1,20) for i in range (n) ]
# print(lst)

#Matrices de manera estatica
# a=[[1,2,4],[1,2,5]] #dos filas misma columna
# a[0][00]

#Matrices de manera dinamica (filas=3, columnas=4)
# matriz=[]
# for f in range(3):
#     matriz.append([])
#     for c in range(4):
#         matriz[f].append(0)
# print (matriz)

#Creaar la matriz por comprension 
# filas=2
# columnas=2
# matriz=[([0]*columnas) for f in range (filas)]
# #Rellenar la matriz
# for f in range (filas):
#     for c in range(columnas):
#         n=int(input("Ingrese valor:"))
#         matriz[f][c]=n
# #Mostramos la matriz
# for f in range (filas):
#     print()
#     for c in range(columnas):
#         print(matriz[f][c],end=" ")
#Formato a la matriz
# filas,columnas=2,2
# matriz=[[2,3],[4,3]]
# for f in range (filas):
#     print()
#     for c in range(columnas):
#         print("%2d" %matriz[f][c],end=" ")

# for f in range (filas):
#     print()
#     for c in range(columnas):
#         print("%.3f" %matriz[f][c],end=" ")