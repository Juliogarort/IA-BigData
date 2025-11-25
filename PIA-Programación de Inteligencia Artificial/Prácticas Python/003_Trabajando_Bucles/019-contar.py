# Escribe un programa que cuente cuántas letras y cuántos dígitos hay en una cadena utilizando un bucle for

cadena = input("Introduce una cadena de texto: ")
contador_letras = 0
contador_digitos = 0

for caracter in cadena:
    if caracter.isalpha():
        contador_letras += 1
    elif caracter.isdigit():
        contador_digitos += 1
print(f"La cadena contiene {contador_letras} letras y {contador_digitos} dígitos.")
