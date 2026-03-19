'''3. Contar palabras'''
import os
os.system('cls')

def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

if __name__ == '__main__':
    frase = input("Ingrese una frase: ")
    print(f"La frase tiene {contar_palabras(frase)} palabras.")