'''6. map() con lambda'''
import os
os.system('cls')

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)