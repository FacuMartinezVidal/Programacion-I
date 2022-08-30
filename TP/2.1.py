def azar():
    lst=[]
    from random import randint as r
    len_azar=r(10,99)
    for x in range (len_azar):
        lst.append(r(1000,9999))
    return lst

def suma(lst):
    suma=0
    for x in lst:
        suma+=x
    return suma

def pop(lst):
    valor=int(input('Valor a eliminar de la lista: '))
    lst.remove(valor)
    return lst

def capicua(lst):
    lst_r=list(reversed(lst))
    if lst == lst_r:
        print ('Es capicua')
    else:
        print('No es capicua')
# numbers = [66, 78, 2, 45, 97, 17, 34, 105, 44, 52]
# lst_r = list(reversed(numbers))
# newList = numbers[::-1]
lst=azar()
print(suma(lst))
print(pop(lst))
print(capicua(lst))

