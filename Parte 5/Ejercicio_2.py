'''Conversor de temperaturas:
Pide al usuario que ingrese una temperatura en grados Celsius.
Convierte la temperatura a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
Imprime la temperatura en grados Fahrenheit.
'''

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")