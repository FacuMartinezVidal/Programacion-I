#Cargar una lista con 20 valores aleaotrios, comprendidos entre 15 y 60
# import random
# import string
# lst=[]

# for x in range(0,20):
#   lst.append(random.randint(15,60))
#print(lst)

#Mostrar la lista, en una linea, con los valores separados 5 espacios
#for y in range(0,len(lst)):
#   print(lst[y],end="     ")
#print()

#dadas las listas, unir ambas en una nueva lista en la medida que se va creando
# a=[2,6,8,9]
# b=[1,4,5,19,23]
# c=[]
# j=0
# i=0
# while i<len(a) and j<len(b):
#     if b[j]<a[i]:
#         c.append(b[j])
#         j=j+1
#     else:
#         c.append(a[i])
#         i=i+1
# if i==len(a):
#     while j<len(b):
#         c.append(b[j])
#         j=j+1
# else:
#     while i<len(a):
#         c.append(a[i])
#         i=i+1
# print(c)
#
#Ingresar por teclado la base y la altura de un triangulo. Con una funcion calcular su superficie. Mostrar el resultado en el programa principal

# def supTriangulo(base,altura):
#     sup= (base*altura//2)
#     return sup

# def main():
#     base=int(input("Ingrese la base: "))
#     altura=int(input("Ingrese la altura: "))
#     area=lambda b,h: (b*h)//2
#     print("La superficie es de:",area(base,altura))
# main()

#Ingresar un valor y obtener su cubo utlizando lambda

# def main():
#     valor=int(input("Ingrese el valor: "))
#     cubo=lambda valor: pow(valor,3)
#     print("valor elvado al cubo:",cubo(valor))
# main()