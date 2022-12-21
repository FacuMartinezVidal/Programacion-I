archivo=open("patentesfinal.txt", "rt")
data= archivo.readlines()
lst_data=[]
for lineas in data:
    lst_data.append(lineas.split(';'))
lst_patentes=[]
lst_personas=[]
for linea in lst_data:
    lst_patentes.append(linea[0])
    lst_personas.append(linea[1])
patentes=set(lst_patentes)
personas=set(lst_personas)

#PATENTES
dic_patentes={}
multas_patentes=0
for patente in patentes:
    for linea in lst_data:
        if patente==linea[0]:
            multas_patentes+=int(linea[2])
    dic_patentes[patente]=multas_patentes
    multas_patentes=0
print(dic_patentes)

#PERSONAS
dic_personas={}
multas_personas=0
for persona in personas:
    for linea in lst_data:
        if persona == linea[1]:
            multas_personas+=int(linea[2])
    dic_personas[persona]=multas_personas
    multas_personas=0
print(dic_personas)

#AUTO POR PERSONA
dic_personaAutos={}
lst_personaPatentes=[]
for persona in personas:
    for linea in lst_data:
        if persona==linea[1]:
            lst_personaPatentes.append(linea[0])
    dic_personaAutos[persona]=len(set(lst_personaPatentes))
    lst_personaPatentes=[]

#DIC ORDENADO
valores=[]
orden=[]
for keys in sorted(dic_personaAutos, key=lambda k:dic_personaAutos[k], reverse=True):
    valores.append(keys)
    valores.append(dic_personaAutos[keys])
    orden.append(valores)
    valores=[]
print(orden)

def digitos(num):
    digito=num%10
    lst.append(digito)
    if num<10:
        return True
    else:
        digitos(num//10)
def promedio(num):
    digitos(num)
    suma=0
    for digito in lst:
        suma+=digito
    res= round(suma/len(lst), 2)
    return res

lst=[]
print(promedio(12345))
