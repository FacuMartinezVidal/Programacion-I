def azar():
    lst=[]
    from random import randint as r
    for x in range (50):
        lst.append(r(1,100))
    return lst

def repetido(lst):
    res='No hay repetidos'
    for x in range(len(lst)):
        for y in range(len(lst)):
            if x!=y:
                if lst[x]==lst[y]:
                    res='Hay repetidos'
    return res

#No entiendo el c

        

