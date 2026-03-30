'''Calculadora de índice de masa corporal (IMC):
- Solicita al usuario que ingrese su peso en kg y su altura en metros.
- Calcula el IMC utilizando la fórmula: IMC = peso / (altura * altura).
- Muestra el IMC calculado y una categoría de peso según el IMC (talla s, talla m, talla l, talla xl).
'''

if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = peso / (altura * altura)

    print(f"Su índice de masa corporal (IMC) es: {imc}")

    if imc < 18.5:
        print("Categoría de peso: Talla S")
    elif 18.5 <= imc < 25:
        print("Categoría de peso: Talla M")
    elif 25 <= imc < 30:
        print("Categoría de peso: Talla L")
    else:
        print("Categoría de peso: Talla XL")