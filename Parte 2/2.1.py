'''2.1. Escribe un programa que solicita al usuario
que ingrese números enteros positivos y muestre
la suma de esos números. La entrada de números
continuará hasta que el usuario ingrese un 
número negativo, momento en el que el programa 
mostrará la suma total.'''

suma = 0
while True:
    numero = int(input("Ingresa un número entero positivo (o un número negativo para terminar): "))
    if numero < 0:
        break
    suma += numero

print("La suma total es:", suma)