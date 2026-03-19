'''Del punto 1, recorrer y mostrar k,v'''
import os
os.system('cls')

lista_personas = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "Ana", "edad": 28}
]

while True:
    print('1. Mostrar todas las edades')
    print('2. Mostrar todos los nombres')
    print('3. Agregar una persona')
    opcion = int(input('Ingrese la opción:  '))
    if opcion == 1:
        print(f'Las edades de las personas son:')
        for i in lista_personas:
            print(f'- {i['edad']}')
    elif opcion == 2:
        print(f'Los nombres de las personas son:')
        for i in lista_personas:
            print(f'- {i['nombre']}')
    elif opcion == 3:
        nombre = input('Ingresa nombre de la persona: ')
        edad = input('Ingresa la edad: ')
        lista_personas.append({'nombre': nombre, 'edad': edad})
        print(f'\nListo! Persona agregada\n{lista_personas[-1]}\n')
    elif opcion == 0:
        print('Sistema cerrado')
        break