'''Administrador de tareas:
Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
Muestra la lista de tareas agregadas.
Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.'''

if __name__ == "__main__":
    tareas = []
    while True:
        print('\n\n1.Agregar tarea\n2.Mostrar la lista de tareas\n3.Marcar como completadas\n4.Eliminar tarea\n5.Salir')
        opcion = int(input('¿Qué opción queres hacer? '))
        if opcion == 1:
            titulo = input('Ingrese el título de la tarea: ')
            descripcion = input('Ingrese la descripción de la tarea: ')
            fecha_vencimiento = input('Ingrese la fecha de vencimiento (dd/mm/yyyy): ')
            tarea = {
                'titulo': titulo,
                'descripcion': descripcion,
                'fecha_vencimiento': fecha_vencimiento,
                'completada': False
            }
            tareas.append(tarea)
            print(f'\nTarea "{titulo}" con fecha de vencimiento {fecha_vencimiento} agregada a la lista.')
        elif opcion == 2:
            print('\nLista de tareas:')
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea['titulo']} - {tarea['descripcion']} (Vence: {tarea['fecha_vencimiento']}) - Estado: {tarea['completada']}")
        elif opcion == 3:
            numero_tarea = int(input('Ingrese el número de la tarea que desea marcar como completada: '))
            if 1 <= numero_tarea <= len(tareas):
                tareas[numero_tarea - 1]['completada'] = True
                print(f'\nTarea "{tareas[numero_tarea - 1]["titulo"]}" marcada como completada.')
            else:
                print('\nNúmero de tarea inválido.')
        elif opcion == 4:
            numero_tarea = int(input('Ingrese el número de la tarea que desea eliminar: '))
            if 1 <= numero_tarea <= len(tareas):
                tarea_eliminada = tareas[numero_tarea - 1]
                print(f'\nTarea "{tarea_eliminada["titulo"]}" eliminada de la lista.')
                tareas.pop(numero_tarea - 1)
            else:
                print('\nNúmero de tarea inválido.')
        elif opcion == 5:
            print('Cerrando programa')
            break
        else:
            print('Opción inválida. Por favor, ingrese un número del 1 al 5.')