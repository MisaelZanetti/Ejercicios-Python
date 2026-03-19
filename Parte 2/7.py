'''7. Escribe un programa que recorra una cadena de 
texto y cuente cuántas veces aparece la letra 'a' en la cadena.'''

cadena = 'Palangana'
cantidad = 0

for letra in cadena:
    if letra.lower() == 'a':
        cantidad += 1

print(cantidad)