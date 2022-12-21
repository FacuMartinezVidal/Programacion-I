#ORGANIZO LA INFORMACION 
def fixData():
    data=[]
    archivo = open('patentesfinal.txt', 'rt')
    lineas = archivo.readlines()
    for linea in lineas:
        linea_reformada=linea.split(';')
        data.append(linea_reformada)
    archivo.close()
    return data
        
data = fixData()

#LISTA DE PATENTES (SIN REPETIR) Y PERSONAS (SIN REPETIR)
lst_patentes=[]
lst_personas=[]
for linea in data:
    lst_patentes.append(linea[0])
    lst_personas.append(linea[1])
patentes=set(lst_patentes)
personas=set(lst_personas)

#TOTAL POR VEHICULO
multa_patentes=0
dic_patentes={}
for x in patentes:
    for linea in data:
        if x == linea[0]:
            multa_patentes+= int(linea[2])
    dic_patentes[x]=multa_patentes
    multa_patentes=0
# print (dic_patentes)

#TOTAL POR PERSONA
multa_personas=0
dic_personas={}
for y in personas:
    for linea in data:
        if y == linea[1]:
            multa_personas+= int(linea[2])
    dic_personas[y]=multa_personas
    multa_personas=0
# print(dic_personas)

#TOTAL CANTIDAD DE VEHICULOS DE UNA PERSONA
dic_autosPersona={}
autos=[]
for z in personas:
    for linea in data:
        if z == linea[1]:
            autos.append(linea[0])
            autosFix=set(autos)
            dic_autosPersona[z]=len(autosFix)
            
    autos=[]

    
#ORDENARLOS EN LISTA DE MANERA DESCENDENTE
lst=[] 
lst_aux=[]
for a in sorted(dic_autosPersona, key=lambda k:dic_autosPersona[k], reverse=True):
    lst_aux.append(a)
    lst_aux.append(dic_autosPersona[a])
    lst.append(lst_aux)
    lst_aux=[]
# print(lst)

#EJERCICIO 2
def digitos(num):
    digito=num%10
    if num==0:
        return lst
    lst.append(digito)
    if num<1:
        lst.append(num)
        return lst
    else:
        digitos(num//10)

def promedio(num):
    digito=digitos(num)
    suma=0
    for digito in lst:
        suma+=digito
    promedio = round(suma/len(lst),2)
    return promedio

lst=[]
print(promedio(1234))
