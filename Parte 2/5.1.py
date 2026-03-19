'''5.1 Agregar otras frutas a la lista.'''

frutas = ["manzana", "banana", "naranja", "uva", "pera"]
print("Frutas en la lista:", frutas)

while True:
    print('1. Mostrar frutas')
    print('2. Agregar fruta')
    opcion = int(input('Ingrese la opción:  '))
    if opcion == 1:
        for fruta in frutas:
            print(fruta)
    elif opcion == 2:
        fruta_nueva = input('Nombre de la fruta nueva: ')
        frutas.append(fruta_nueva)
        print('\nListo, fruta agregada \n')
    elif opcion == 0:
        print('Sistema cerrado')
        break
