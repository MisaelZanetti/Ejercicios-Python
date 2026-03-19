'''6. Escribe un programa que recorra una lista
de números y muestre si cada número es par o impar.'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(f'El numero {numero} es par')
    else:
        print(f'El numero {numero} es impar')