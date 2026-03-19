'''5. Lambda para sumar, potencia'''
import os
os.system('cls')

if __name__ == '__main__':
    sumar = lambda x, y: x + y
    resultado_suma = sumar(5, 3)
    print(f'La suma de 5 y 3 es: {resultado_suma}')

    potencia = lambda base, exponente: base ** exponente
    resultado_potencia = potencia(2, 4)
    print(f'2 elevado a la potencia de 4 es: {resultado_potencia}')