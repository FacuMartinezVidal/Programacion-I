from turtle import xcor


lst1=['jauni','facu','nino','beto','nacho','pepe']
lst2=['nacho','juani','harry']

def eliminar1 (lst1,lst2):
    for i in range(len(lst2)):
        while lst2 in lst1:
            lst1.remove(lst2[i])
    return lst1

def eliminar2 (lst1,lst2):
    print(lst1)
    n_lst1=[i for i in lst1 if i not in lst2]
    repetidas=[a for a in lst1 if a in lst2]
    print(n_lst1)
    print(repetidas)

#PREGUNTAR