'''7. Integrador: Crear programa que permita
al usuario agregar tareas con descripción, 
fecha límite y prioridad, así como mostrar 
la lista de tareas. 
Este menú se repite hasta que el usuario elige salir."'''

import os
os.system('cls')

if __name__ == '__main__':
    tareas = []
    while True:
        print('1. Agregar tarea')
        print('2. Mostrar tareas')
        print('3. Salir')
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            descripcion = input('Ingrese la descripción de la tarea: ')
            fecha_limite = input('Ingrese la fecha límite (dd/mm/yyyy): ')
            prioridad = input('Ingrese la prioridad (Alta, Media, Baja): ')
            tareas.append({'descripcion': descripcion, 'fecha_limite': fecha_limite, 'prioridad': prioridad})
            print('Tarea agregada exitosamente.')
        elif opcion == 2:
            print('\nLista de tareas:')
            for tarea in tareas:
                print(f"Descripción: {tarea['descripcion']}, Fecha límite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}\n")
        elif opcion == 3:
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, intente nuevamente.')