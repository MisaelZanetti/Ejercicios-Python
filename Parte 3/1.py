'''1. Define una lista de diccionarios que 
represente información personal.
nombre,edad. Luego, accede a
elementos específicos de la lista, 
como el primer diccionario, el nombre 
de la primera persona y la edad de la 
segunda persona, para finalmente imprimir
los resultados en la consola.'''
import os
os.system('cls')

lista_personas = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "Ana", "edad": 28}
]

for i in lista_personas:
    print(f'Mi nombre es {i['nombre']} y tengo {i['edad']} años')