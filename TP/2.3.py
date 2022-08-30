def cuadrados():
    from random import randint as r
    lst=[]
    n=int(input('Ingrese el valor de N: '))
    for x in range (1,n+1):
        lst.append(r(1,n))
    print(lst)
    lst_cuad=[i**2 for i in lst]
    return lst_cuad [0:10]
print(cuadrados())
