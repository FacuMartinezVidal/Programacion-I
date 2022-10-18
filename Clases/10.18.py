dic={}
frase=input('Ingrese la frase: ')
lst=[]
contador=0
for x in frase:
    dic[x]=''
    if x in frase:
        lst.append(x)
lst.sort()
for x in frase:
    for y in lst:
        if x==y:
            contador+=1
    dic[x]=contador
    contador=0             
print(dic)
print(lst)