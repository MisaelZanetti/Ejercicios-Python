'''Juego de adivinanza de números:
Genera un número aleatorio entre 1 y 100.
Pide al usuario que adivine el número.
Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
Muestra el número de intentos necesarios para adivinar.
'''

import random

if __name__ == "__main__":
    numero_random = random.randint(0, 100)
    intentos = 0
    
    while True:
        numero_ingresado = int(input('Cual crees que es el numero? '))
        if numero_ingresado == numero_random:
            print("¡Felicidades! ¡Adivinaste el número!")
            print(f"El número era: {numero_random}")
            print(f"Lo adivinaste en {intentos} intentos")
            break
        if numero_ingresado < numero_random:
            print("El número random es mas alto. Intenta de nuevo.")
        if numero_ingresado > numero_random:
            print("El número random es mas bajo. Intenta de nuevo.")
        intentos += 1