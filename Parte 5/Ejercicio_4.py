'''Validador de contraseña:
Solicita al usuario que cree una contraseña.
Verifica si la contraseña cumple con los siguientes criterios:
Tiene al menos 8 caracteres de longitud.
Contiene al menos una letra mayúscula y una letra minúscula.
Tiene al menos un número.
Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
Informa al usuario si la contraseña es válida o no.
'''

if __name__ == "__main__":
    while True:
        mayuscula = False
        minuscula = False
        numero = False
        caracter_especial = False
        contraseña = input("Cree una contraseña: ")
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
        for digito in contraseña:
            if digito.isupper():
                mayuscula = True
            elif digito.islower():
                minuscula = True
            elif digito.isdigit():
                numero = True
            elif digito == "!" or digito == "@" or digito == "#" or digito == "$" or digito == "%":
                caracter_especial = True
        if not mayuscula:
            print("La contraseña debe contener al menos una letra mayúscula.")
        if not minuscula:
            print("La contraseña debe contener al menos una letra minúscula.")
        if not numero:
            print("La contraseña debe contener al menos un número.")
        if not caracter_especial:
            print("La contraseña debe contener al menos un carácter especial.")
        else:
            print("La contraseña es válida.")
            break