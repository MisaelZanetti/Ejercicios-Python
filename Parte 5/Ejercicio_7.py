'''Calculadora de descuento de compra:
Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
Calcula el precio final después del descuento.
Muestra el precio final al usuario.'''

if __name__ == "__main__":
    precio_original = float(input('Ingrese el precio original del artículo: '))
    porcentaje_descuento = float(input('Ingrese el porcentaje de descuento: '))

    precio_final = precio_original - (precio_original * (porcentaje_descuento / 100))

    print(f'El precio final después del descuento es: ${precio_final}')