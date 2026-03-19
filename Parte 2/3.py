'''3.Escribe un programa que muestra la primer,
última u otra letra de una cadena de carcateres,
inclusive una rebanada.'''
import random

string = str(input('Ingrese una palabra:  '))
print('Opciones a mostrar:')
print('1. Primera letra')
print('2. Última letra')
print('3. Letra en posición aleatoria')
print('4. Rebanadas')

opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    print(f'La primera letra es: {string[0]}')
elif opcion == 2:
    print(f'La última letra es: {string[-1]}')
elif opcion == 3:
    numero = random.randint(1, len(string) - 1)
    print(f'La letra en la posición {numero + 1} es: {string[numero]}')
elif opcion == 4:
    cantidad = int(input('Ingrese la cantidad de rebanadas:  '))
    if cantidad > len(string):
        print('La cantidad de rebanadas excede la longitud de la cadena.')
    else:
        print(f'Las primeras {cantidad} letras son: {string[:cantidad]}')