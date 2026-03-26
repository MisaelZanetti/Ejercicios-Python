import os
os.system('cls')

def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada):
    nueva_tarea = {"Tarea": tarea, "Fecha limite": fecha_limite, "Prioridad": prioridad, "Completada": completada}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def marcar_completada(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["Completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Índice de tarea no válido.")

def mostrar_tareas(tareas, completada):
    tareas_filtradas = []
    if completada.lower() == "si":
        for tarea in tareas:
            if tarea["Completada"] == True:
                tareas_filtradas.append(tarea)
    elif completada.lower() == "no":
        for tarea in tareas:
            if tarea["Completada"] == False:
                tareas_filtradas.append(tarea)
    else:
        tareas_filtradas = tareas
    
    if not tareas_filtradas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas_filtradas, 1):
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")


if __name__ == "__main__":
    os.system('cls')
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha limite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            completada = False
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva, completada)

        elif opcion == "2":
            completada = input("¿Desea mostrar solo las tareas completadas? (si/no/none): ")
            mostrar_tareas(lista_tareas, completada)

        elif opcion == "3":
            indice_tarea = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
            marcar_completada(lista_tareas, indice_tarea)

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Intente nuevamente.")