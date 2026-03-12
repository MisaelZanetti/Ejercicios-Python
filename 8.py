'''8.  crearemos un programa que verifica si
un número ingresado por el usuario es positivo,
negativo o cero, y también si es un número par o impar.'''

num = int(input("Ingresa un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")