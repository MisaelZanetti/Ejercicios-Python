'''5.2 Escribe un programa verifique si una fruta 
específica está en una lista de frutas y muestra
un mensaje correspondiente.'''

frutas = ["manzana", "banana", "naranja", "uva", "pera"]
print("Frutas en la lista:", frutas)

fruta_buscada = input('Ingrese fruta a buscar:  ')
if frutas.index(fruta_buscada) >= 0:
    print(f'Tu fruta esta en la posicion {frutas.index(fruta_buscada) + 1}')
else:
    print('Tu fruta no esta en la lista')