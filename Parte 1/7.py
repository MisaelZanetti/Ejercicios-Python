'''7. crear un programa que le pida al usuario
nombre, edad y ciudad de residencia, realizar
cálculos basados en la edad, y luego mostrará
la información en pantalla 
(# Pedir al usuario que ingrese su nombre
# Pedir al usuario que ingrese su edad
# Pedir al usuario que ingrese su ciudad de residencia
# Calcular el año de nacimiento
# Saludar al usuario y mostrar la información
# Comprobar si la edad es mayor de 18 años
# Comprobar si la edad es un múltiplo de 5).'''

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad de residencia: ")

año_nacimiento = 2026 - edad
print(f"¡Hola, {nombre}! Bienvenido al programa.")
print(f"Tu edad es: {edad} años.")
print(f"Tu ciudad de residencia es: {ciudad}.")
print(f"Tu año de nacimiento es: {año_nacimiento}.")

if edad > 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

if edad % 5 == 0:
    print("Tu edad es un múltiplo de 5.")
else:
    print("Tu edad no es un múltiplo de 5.")