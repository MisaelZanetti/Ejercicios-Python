'''4. Verificación de Palíndromos'''
import os
os.system('cls')

if __name__ == '__main__':
    palabra = str(input('Ingrese una palabra:  '))
    palabra_limpia = palabra.replace(' ', '').lower()
    
    es_palindromo = True
    for indice in range(len(palabra_limpia)):
        if palabra_limpia[indice] != palabra_limpia[-indice - 1]:
            es_palindromo = False
            break

    if es_palindromo:
        print('La palabra es un Palíndromo')
    else:
        print('La palabra no es un Palíndromo')