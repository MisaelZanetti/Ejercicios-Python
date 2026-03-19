'''4. Verificación de Palíndromos'''
import os
os.system('cls')

if __name__ == '__main__':
    palabra = str(input('Ingrese una palabra:  '))
    invertida = palabra[::-1]

    if palabra == invertida:
        print('La palabra es un Palíndromo')
    else:
        print('La palabra no es un Palíndromo')