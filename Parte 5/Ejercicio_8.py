'''Generador de contraseñas aleatorias:
Solicita al usuario que ingrese la longitud deseada para la contraseña.
Genera una contraseña aleatoria con la longitud especificada.
Utiliza caracteres alfanuméricos y caracteres especiales para mayor seguridad.
Muestra la contraseña generada al usuario.'''

import random

if __name__ == "__main__":
    longitud = int(input('Ingrese la longitud deseada para la contraseña: '))
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    letras_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caracteres_especiales = '!@#$%^&*_?'
    numeros = '0123456789'
    cantidad = longitud / 4
    
    letras_minusculas_aleatorias = random.sample(letras_minusculas, int(cantidad))
    letras_mayusculas_aleatorias = random.sample(letras_mayusculas, int(cantidad))
    caracteres_especiales_aleatorios = random.sample(caracteres_especiales, int(cantidad))
    numeros_aleatorios = random.sample(numeros, int(cantidad))
    # El random.sample me lo recomdo el chat gpt, 
    # me permite generar una muestra aleatoria de caracteres de un conjunto
    
    contraseña = letras_minusculas_aleatorias + letras_mayusculas_aleatorias + caracteres_especiales_aleatorios + numeros_aleatorios
    random.shuffle(contraseña)
    print(f'Contraseña generada: {contraseña}')
    # Al final me da los caracteres separados como una lista,
    # pero no se como hacer para que me los muestre como una sola cadena