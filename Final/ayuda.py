# import random


# def generar_patente():
#     letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     numeros = '0123456789'
#     patente = random.choice(letras) + random.choice(letras) + random.choice(
#         letras) + random.choice(numeros) + random.choice(numeros) + random.choice(numeros)
#     return patente


# def generar_nombre():
#     nombres = ['Juan', 'Ana', 'Pedro', 'Sandra', 'Pablo',
#                'Laura', 'Carlos', 'Marta', 'Alberto', 'Sara']
#     apellidos = ['González', 'Rodríguez', 'Martínez', 'Pérez',
#                  'García', 'Sánchez', 'Fernández', 'Ruiz', 'Díaz', 'López']
#     nombre = random.choice(nombres) + ' ' + random.choice(apellidos)
#     return nombre


# def generar_multa():
#     multa = random.randint(100, 1000)
#     return multa


# with open('patentesfinal.txt', 'w') as f:
#     for i in range(2000):
#         patente = generar_patente()
#         nombre = generar_nombre()
#         multa = generar_multa()
#         f.write(f'{patente};{nombre};{multa}\n')

# print('Archivo creado con éxito')