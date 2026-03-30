'''Generador de secuencia Fibonacci:
Pide al usuario que ingrese un número entero positivo.
Genera los primeros n números de la secuencia Fibonacci, donde n es el número ingresado por el usuario.
Muestra la secuencia Fibonacci resultante.
'''

if __name__ == "__main__":
    n = int(input("Ingrese un número entero positivo: "))
    sequencia_fibonacci = []
    a = 0
    b = 1
    for i in range(n):
        sequencia_fibonacci.append(a)
        b = a + b
        a = b - a
    
    print(f"Los primeros {n} números de la secuencia Fibonacci son: {sequencia_fibonacci}")