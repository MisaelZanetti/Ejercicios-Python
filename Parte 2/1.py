'''1. Escribe un programa que identifique el color
de un objeto y muestre un mensaje según el color.'''

color = input("Ingresa el color del objeto: ").lower()
if color == "rojo":
    print("El objeto es rojo.")
elif color == "azul":
    print("El objeto es azul.")
elif color == "verde":
    print("El objeto es verde.")
else:
    print("Color no reconocido.")