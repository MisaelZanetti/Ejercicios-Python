'''4. Crear una lista de frutas y mostrar en consola
algunas frutas de la lista, también por rebanadas.'''

frutas = ["manzana", "banana", "naranja", "uva", "pera", "fresa", "kiwi", "mango", "piña", "cereza"]
print("Frutas en la lista:", frutas)
print('Opciones a mostrar:')
print('1. Primera fruta')
print('2. Última fruta')
print('3. Rebanadas de frutas')

opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    print(f'La primera fruta es: {frutas[0]}')
elif opcion == 2:
    print(f'La última fruta es: {frutas[4]}')
elif opcion == 3:
    cantidad = int(input('Ingrese la cantidad de rebanadas:  '))
    if cantidad > len(frutas):
        print('La cantidad de rebanadas excede la longitud de la lista.')
    else:
        print(f'Las primera rebanada de frutas son: {frutas[:len(frutas) // cantidad]}')