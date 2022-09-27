#Ruptura de Ciclos 

#Continue (sirve para saltar iteraciones, saltea todas las instrucciones que hay despues de el)
# cont=0
# cad='pildoras informaticas'
# for letras in cad:
#     if letras==' ':
#         continue
#     cont+=1

#Generar los numeros entre 1 y 20, mostrar solamente los pares
# for x in range(0,21):
#     if x%2!=0:
#         continue
#     print (x)

#Break (sale del ciclo directamente)

#Determinar si un numero es primo
# bandera=False
# nro=121
# for x in range(2,nro):
#     if nro%x==0:
#         bandera=True
#         break

# if bandera==True:
#     print('Es primo.')
# else:
#     print('No es primo.')


#ejemplo con while
# cont=1
# while cont<10:
#     print('cont',cont)
#     cont+=1
#     if cont==7:
#         break
# else:
#     print('Finalizacion Correcta')


#pass (sirve para facilitarnos en el armado de codigo)
# while True:
#     print('<<<  Menu >>>')
#     print('1 - Hamburguesa')
#     print('2 - Pizza')
#     print('3 - Pancho')
#     print('0 - Salir')
#     op=int(input('Ingrese su opcion:'))
#     if op==1:
#         pass
#     elif op==2:
#         pass
#     elif op==3:
#         pass
#     else:
#         break





#Exepciones (un error que se produce durante la ejecucion de un programa)

#try - except
nro=int(input('Ingrese un numero: '))
div=int(input('Ingrese un valor para dividirlo: '))
try:
    print(nro/div) #bloque protegido
except ZeroDivisionError: #puede haber varios expect
    print('El valor ingresado es erroneo')
